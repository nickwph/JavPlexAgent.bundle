import argparse
import os
import platform
import re
import tarfile
from os.path import expanduser
from shutil import rmtree, copyfile, copytree

import colorama
import psutil
from termcolor import cprint

from build_replacement import extract_replacements_from_filenames

# parse arguments
parser = argparse.ArgumentParser("build")
parser.add_argument('-d', "--deploy", help="Deploy the generated bundle into Plex Server Plugin location", type=bool, default=False)
args = parser.parse_args()

# allow command line coloring
colorama.init()

# build information
version = '1.2.0'
build_number = 'local'

# variables
src_dir = 'src'
build_dir = 'build'
outputs_dir = 'outputs'
bundle_name = "JavPlexAgent.bundle"
contents_dir = os.path.join(build_dir, bundle_name, 'Contents')
code_dir = os.path.join(contents_dir, 'Code')
assets_dir = 'assets'
libraries_dir = os.path.join(contents_dir, 'Libraries')

# reset the build directory
if os.path.exists(build_dir): rmtree(build_dir)
os.makedirs(code_dir)

# scan all files for import code replacements
cprint("> setting up global replacements")
global_replacements = []
for dir_name, subdir_names, file_names in os.walk(src_dir):
    global_replacements += extract_replacements_from_filenames(src_dir, dir_name, file_names)

# copy files and fix up the imports
for dir_name, subdir_names, file_names in os.walk(src_dir):
    cprint("> setting up local replacements for directory {}".format(dir_name))
    local_replacements = extract_replacements_from_filenames(src_dir, dir_name, file_names, True)
    for file_name in file_names:
        if not file_name.endswith("_test.py") and (
                dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            source_path = os.path.join(dir_name, file_name)
            build_file = "{}_{}".format(dir_name.replace(src_dir, "").replace(os.path.sep, "_"), file_name).replace("_", "", 1)
            build_path = os.path.join(code_dir, build_file)
            cprint("> compiling {} to {}".format(source_path, build_path))
            code = open(source_path).read()
            code = re.sub(r"^(\s*version = '0\.0\.0'.*?\n)", "version = '{}'\n".format(version), code, flags=re.MULTILINE)
            code = re.sub(r"^(\s*build = 'local'.*?\n)", "build = '{}'\n".format(build_number), code, flags=re.MULTILINE)
            code = re.sub(r'(\s*from Framework.*?\n)', "\n", code, flags=re.MULTILINE)
            code = re.sub(r'(\s*from plex.*?\n)', "\n", code, flags=re.MULTILINE)
            for replacement in local_replacements: code = replacement.replace(code)
            for replacement in global_replacements: code = replacement.replace(code)
            open(build_path, 'w').write(code)

# setup basic bundle structure
cprint("> copying assets")
assets_info_plist = os.path.join(assets_dir, 'Info.plist')
assets_default_prefs = os.path.join(assets_dir, 'DefaultPrefs.json')
build_info_plist = os.path.join(contents_dir, 'Info.plist')
build_default_prefs = os.path.join(contents_dir, 'DefaultPrefs.json')
copyfile(assets_info_plist, build_info_plist)
copyfile(assets_default_prefs, build_default_prefs)

# install the python libraries
cprint("> installing libraries")
common_flags = "--no-python-version-warning --disable-pip-version-check --ignore-installed --force-reinstall --no-cache-dir --upgrade --quiet"
target_dir = os.path.join(libraries_dir, 'Shared')
os.system('pip install {} --target {} --requirement requirements.txt'.format(common_flags, target_dir))

# need some system info
cprint("> gathering build information")
platform_system = platform.system().lower()
cprint("system: {}".format(platform_system), 'yellow')

cprint("> generating artifact")
if not os.path.exists(outputs_dir): os.makedirs(outputs_dir)
artifact_name = "javplexagent-{}-{}-{}.tar.gz".format(version, build_number, platform_system)
artifact_path = os.path.join(outputs_dir, artifact_name)
artifact_add_path = os.path.join(build_dir, bundle_name)
cprint("compressing directory: {}".format(artifact_add_path), 'yellow')
artifact = tarfile.open(artifact_path, mode='w:gz')
artifact.add(artifact_add_path, arcname=bundle_name)
artifact.close()
cprint("artifact: {}".format(artifact_path), 'yellow')

# some platform specific actions
if not args.deploy:
    # all set
    cprint("> done")
    exit(0)

elif platform_system == 'darwin':

    # the python host needs to be unsigned to be able to use pillow and numpy
    cprint("> making sure python host is unsigned")
    os.system("codesign --remove-signature /Applications/Plex\ Media\ Server.app/Contents/MacOS/Plex\ Script\ Host")

    # replacing the one in plugins
    cprint("> replacing plugin locally")
    from_path = "build/JavPlexAgent.bundle"
    to_path = expanduser("~/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle")
    cprint("from path: {}".format(from_path), 'yellow')
    cprint("to path:   {}".format(to_path), 'yellow')
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # restart the server
    cprint("> restarting server")
    for proc in psutil.process_iter():
        if proc.name() == "Plex Media Server": proc.kill()
    os.system("open /Applications/Plex\ Media\ Server.app")


elif platform_system == 'linux':  # ubuntu

    # replacing the one in plugins
    cprint("> replacing plugin locally")
    from_path = "build/JavPlexAgent.bundle"
    to_path = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle"
    cprint("from path: {}".format(from_path), 'yellow')
    cprint("to path:   {}".format(to_path), 'yellow')
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # restart the server
    cprint("> restarting server, please enter password if asked")
    os.system("sudo service plexmediaserver restart")

    # follow logs
    cprint("> view log")
    os.system("tail -F /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Logs/PMS\ Plugin\ Logs/com.nicholasworkshop.javplexagent.log")

elif platform_system == 'windows':

    # killing the server
    cprint("> killing server")
    for proc in psutil.process_iter():
        try:
            if proc.name() == "Plex Media Server.exe": proc.kill()
        except psutil.AccessDenied:
            print "killing failed, permission denied"

    # replacing the one in plugins
    cprint("> replacing plugin locally")
    from_path = "build/JavPlexAgent.bundle"
    to_path = os.path.expandvars("%LOCALAPPDATA%\Plex Media Server\Plug-ins\JavPlexAgent.bundle")
    cprint("from path: {}".format(from_path), 'yellow')
    cprint("to path:   {}".format(to_path), 'yellow')
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # killing the server
    cprint("> starting server")
    os.startfile("C:\Program Files (x86)\Plex\Plex Media Server\Plex Media Server.exe")  # noqa

    cprint("> to view logs run this in powershell")
    cprint('Get-Content $Env:LOCALAPPDATA\"Plex Media Server"\Logs\"PMS Plugin Logs"\com.nicholasworkshop.javplexagent -Wait -Tail 30')

# all set
cprint("> done")
exit(0)
