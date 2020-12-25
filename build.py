import colorama
import os
import platform
import psutil
import re
import tarfile
from os.path import expanduser
from shutil import rmtree, copyfile, copytree
from termcolor import cprint

from build_replacement import extract_replacements_from_filenames

# allow command line coloring
colorama.init()

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
cprint("> setting up global replacements", "grey")
global_replacements = []
for dir_name, subdir_names, file_names in os.walk(src_dir):
    global_replacements += extract_replacements_from_filenames(src_dir, dir_name, file_names)

# copy files and fix up the imports
for dir_name, subdir_names, file_names in os.walk(src_dir):
    cprint("> setting up local replacements for directory {}".format(dir_name), "grey")
    local_replacements = extract_replacements_from_filenames(src_dir, dir_name, file_names, True)
    for file_name in file_names:
        if not file_name.endswith("_test.py") and (
                dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            source_path = os.path.join(dir_name, file_name)
            build_file = "{}_{}".format(dir_name.replace(src_dir, "").replace(os.path.sep, "_"), file_name).replace("_",
                                                                                                                    "",
                                                                                                                    1)
            build_path = os.path.join(code_dir, build_file)
            cprint("> compiling {0} to {1}".format(source_path, build_path), "grey")
            code = open(source_path).read()
            code = re.sub(r'(\s*from Framework.*?\n)', "\n", code)
            code = re.sub(r'(\s*from plex.*?\n)', "\n", code)
            for replacement in local_replacements: code = replacement.replace(code)
            for replacement in global_replacements: code = replacement.replace(code)
            open(build_path, 'w').write(code)

# setup basic bundle structure
cprint("> copying assets", "grey")
assets_info_plist = os.path.join(assets_dir, 'Info.plist')
assets_default_prefs = os.path.join(assets_dir, 'DefaultPrefs.json')
build_info_plist = os.path.join(contents_dir, 'Info.plist')
build_default_prefs = os.path.join(contents_dir, 'DefaultPrefs.json')
copyfile(assets_info_plist, build_info_plist)
copyfile(assets_default_prefs, build_default_prefs)

# install the python libraries
cprint("> installing libraries", "grey")
common_flags = "--no-python-version-warning --disable-pip-version-check --upgrade"
target_dir = os.path.join(libraries_dir, 'Shared')
os.system('pip install {} --target {} --requirement requirements.txt'.format(common_flags, target_dir))

# need some system info
cprint("> gathering build information", "grey")
platform_system = platform.system().lower()
# platform_arch = platform.architecture()[0].lower()
cprint("system: {}".format(platform_system), 'yellow')
# cprint("architecture: {}".format(platform_arch), 'yellow')

cprint("> generating artifact", "grey")
if not os.path.exists(outputs_dir): os.makedirs(outputs_dir)
artifact_name = "javplexagent-1.2.0-{}.tar.gz".format(platform_system)
artifact_path = os.path.join(outputs_dir, artifact_name)
artifact_add_path = os.path.join(build_dir, bundle_name)
cprint("compressing directory: {}".format(artifact_add_path), 'yellow')
artifact = tarfile.open(artifact_path, mode='w:gz')
artifact.add(artifact_add_path, arcname=bundle_name)
artifact.close()
cprint("artifact: {}".format(artifact_path), 'yellow')
# zip: javplexagent-1.2.0-macos-x86_64
# zip: javplexagent-1.2.0-macos-arch64
# zip: javplexagent-1.2.0-ubuntu-arm64
# zip: javplexagent-1.2.0-windows-x86_64

# some platform specific actions
if platform_system == 'darwin':

    # the python host needs to be unsigned to be able to use pillow and numpy
    cprint("> making sure python host is unsigned", "grey")
    os.system("codesign --remove-signature /Applications/Plex\ Media\ Server.app/Contents/MacOS/Plex\ Script\ Host")

    # replacing the one in plugins
    cprint("> replacing plugin locally", "grey")
    from_path = "build/JavPlexAgent.bundle"
    to_path = expanduser("~/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle")
    cprint("from path: {}".format(from_path), 'yellow')
    cprint("to path:   {}".format(to_path), 'yellow')
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # restart the server
    cprint("> restarting server", "grey")
    for proc in psutil.process_iter():
        if proc.name() == "Plex Media Server": proc.kill()
    os.system("open /Applications/Plex\ Media\ Server.app")

elif platform_system == 'windows':

    # killing the server
    cprint("> killing server", "grey")
    for proc in psutil.process_iter():
        try:
            if proc.name() == "Plex Media Server.exe": proc.kill()
        except psutil.AccessDenied:
            print "killing failed, permission denied"

    # replacing the one in plugins
    cprint("> replacing plugin locally", "grey")
    from_path = "build/JavPlexAgent.bundle"
    to_path = os.path.expandvars("%LOCALAPPDATA%\Plex Media Server\Plug-ins\JavPlexAgent.bundle")
    cprint("from path: {}".format(from_path), 'yellow')
    cprint("to path:   {}".format(to_path), 'yellow')
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # killing the server
    cprint("> starting server", "grey")
    os.startfile("C:\Program Files (x86)\Plex\Plex Media Server\Plex Media Server.exe")

    cprint("> to view logs run this in powershell")
    cprint('Get-Content $Env:LOCALAPPDATA\"Plex Media Server"\Logs\"PMS Plugin Logs"\com.nicholasworkshop.javplexagent -Wait -Tail 30')

# all set
cprint("> done", "grey")
