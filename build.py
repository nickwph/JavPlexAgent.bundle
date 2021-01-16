import argparse
import datetime
import os
import platform
import re
import subprocess
import sys
import tarfile
from os.path import expanduser
from shutil import rmtree, copyfile, copytree

import colorama
import psutil
from termcolor import cprint

from build_log import tail_log
from build_patch import patch_image_file, patch_windows_pillow
from build_replacement import extract_replacements_from_filenames

# parse arguments
parser = argparse.ArgumentParser("build.py")
parser.add_argument('-d', "--deploy", help="deploy the generated bundle into plex server", action='store_true')
parser.add_argument('-a', "--artifact", help="gzip the built bundle into outputs directory", action='store_true')
parser.add_argument('-r', "--reinstall_libs", help="force reinstalling libraries", action='store_true')
parser.add_argument('-s', "--skip_lib_check", help="skip libraries change checking", action='store_true')
parser.add_argument('-t', "--tail_log", help="tail log file immediately after deployment", action='store_true')
parser.add_argument('-c', "--clear_data", help="clear media and metadata from plex server", action='store_true')
args = parser.parse_args()

# allow command line coloring
colorama.init()

# build information
version = '1.3.0'
git_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
build_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
build_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
is_release = (build_number != 'local')
environment = 'release' if is_release else 'debug'
sentry_project_id = "5576704" if is_release else "5574876"
sentry_project_key = "81a6a4b2981a4d7487660950d8324bd7" if is_release else "331eb7edb13b4011a21b86ff4c956c7b"
sentry_dsn = "https://{}@o148305.ingest.sentry.io/{}".format(sentry_project_key, sentry_project_id)
cprint("> build information")
cprint("version: {}".format(version), 'yellow')
cprint("git hash: {}".format(git_hash), 'yellow')
cprint("build number: {}".format(build_number), 'yellow')
cprint("build datetime: {}".format(build_datetime), 'yellow')
cprint("sentry dsn: {}".format(sentry_dsn), 'yellow')

# variables
src_dir = 'src'
build_dir = 'build'
outputs_dir = 'outputs'
bundle_name = "JavPlexAgent.bundle"
contents_dir = os.path.join(build_dir, bundle_name, 'Contents')
code_dir = os.path.join(contents_dir, 'Code')
assets_dir = 'assets'
libraries_dir = os.path.join(contents_dir, 'Libraries')

# need some system info
cprint("> gathering build information")
platform_system = platform.system().lower()
cprint("platform_system: {}".format(platform_system), 'yellow')

# sanity check
cprint("> sanity check")
cprint("python_version: {}".format(platform.python_version()), 'yellow')
cprint("ucs2_enabled: {}".format(sys.maxunicode == 65535), 'yellow')
cprint("sys_platform: {}".format(sys.platform), 'yellow')
if not sys.version_info.major == 2 and sys.version_info.minor == 7:
    cprint("python needs to be 2.7, build failed", 'red')
    exit(1)
if platform_system == 'linux' and sys.maxunicode != 65535:
    cprint("python in linux needs to be compiled with ucs-2, build failed", 'red')
    exit(1)
if platform_system == 'windows' and sys.platform != 'win32':
    cprint("python in windows must to be compiled in 32-bit, build failed", 'red')
    exit(1)

# reset the build directory
if os.path.exists(code_dir): rmtree(code_dir)
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
        if not file_name.endswith("_test.py") and (dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            source_path = os.path.join(dir_name, file_name)
            build_file = "{}_{}".format(dir_name.replace(src_dir, "").replace(os.path.sep, "_"), file_name).replace("_", "", 1)
            build_path = os.path.join(code_dir, build_file)
            cprint("> compiling {} to {}".format(source_path, build_path))
            code = open(source_path).read()
            code = re.sub(r"^(version = '')$", "version = '{}'".format(version), code, flags=re.MULTILINE)
            code = re.sub(r"^(git_hash = '')$", "git_hash = '{}'".format(git_hash), code, flags=re.MULTILINE)
            code = re.sub(r"^(build_number = '')$", "build_number = '{}'".format(build_number), code, flags=re.MULTILINE)
            code = re.sub(r"^(build_datetime = '')$", "build_datetime = '{}'".format(build_datetime), code, flags=re.MULTILINE)
            code = re.sub(r"^(environment = '')$", "environment = '{}'".format(environment), code, flags=re.MULTILINE)
            code = re.sub(r"^(sentry_dsn = '')$", "sentry_dsn = '{}'".format(sentry_dsn), code, flags=re.MULTILINE)
            code = re.sub(r'^(from Framework.*?)$', "", code, flags=re.MULTILINE)
            code = re.sub(r'^(from plex.*?)$', "", code, flags=re.MULTILINE)
            code = re.sub(r'^(from sentry_sdk.integrations.logging.*?)$', "", code, flags=re.MULTILINE)
            code = re.sub(r'^(from sentry_sdk._types.*?)$', "\n", code, flags=re.MULTILINE)
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
if args.reinstall_libs:
    # remove old libraries
    if os.path.exists(libraries_dir):
        cprint("> removing old libraries")
        rmtree(libraries_dir)

# do libraries check
if not args.skip_lib_check:
    # pip install new libraries
    cprint("> installing libraries")
    common_flags = "--no-python-version-warning --disable-pip-version-check --no-cache-dir --upgrade"
    target_dir = os.path.join(libraries_dir, 'Shared')
    print colorama.Fore.YELLOW,
    colored_pip = '' if platform_system == 'windows' else 'printf {}'.format(colorama.Fore.YELLOW)
    os.system('{}; pip install {} --target {} --requirement requirements.txt'.format(colored_pip, common_flags, target_dir))
    print colorama.Fore.RESET,

    # patch pillow in windows
    if platform_system == 'windows':
        pillow_dir = os.path.join(target_dir, 'PIL')
        patch_windows_pillow(pillow_dir)

    # patch image file in pillow
    image_file_path = os.path.join(target_dir, 'PIL', 'ImageFile.py')
    patch_image_file(image_file_path)

# generate the name
cprint("> generating build name file")
build_name = "javplexagent-{}-{}-{}-{}-{}".format(version, build_number, git_hash, platform_system, build_datetime)
build_name_path = os.path.join(build_dir, 'name')
open(build_name_path, 'w').write(build_name)

# generate artifact
if args.artifact:
    cprint("> generating artifact")
    if not os.path.exists(outputs_dir): os.makedirs(outputs_dir)
    artifact_name = "{}.tar.gz".format(build_name)
    artifact_path = os.path.join(outputs_dir, artifact_name)
    artifact_add_path = os.path.join(build_dir, bundle_name)
    cprint("compressing directory: {}".format(artifact_add_path), 'yellow')
    artifact = tarfile.open(artifact_path, mode='w:gz')
    artifact.add(artifact_add_path, arcname=bundle_name)
    artifact.close()
    cprint("artifact: {}".format(artifact_path), 'yellow')

# clear media metadata in mac
if args.clear_data and platform_system == 'darwin':
    cprint("> removing media and metadata dir from plex server")
    media_path = expanduser("~/Library/Application Support/Plex Media Server/Media")
    metadata_path = expanduser("~/Library/Application Support/Plex Media Server/Metadata")
    if os.path.exists(media_path): rmtree(media_path)
    if os.path.exists(metadata_path): rmtree(metadata_path)

# clear media metadata in ubuntu
if args.clear_data and platform_system == 'linux':
    cprint("> removing media and metadata dir from plex server")
    media_path = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Media"
    metadata_path = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Metadata"
    if os.path.exists(media_path): rmtree(media_path)
    if os.path.exists(metadata_path): rmtree(metadata_path)

# clear media metadata in ubuntu
if args.clear_data and platform_system == 'windows':
    cprint("> removing media and metadata dir from plex server")
    cprint("sorry it is not available yet, remove these directories by yourself", 'yellow')
    cprint("%LOCALAPPDATA%\Plex Media Server\Media", 'yellow')
    cprint("%LOCALAPPDATA%\Plex Media Server\Metadata", 'yellow')

# mac deployment
if args.deploy and platform_system == 'darwin':
    # the python host needs to be unsigned to be able to use pillow and numpy
    cprint("> making sure python host is unsigned")
    host_path = "/Applications/Plex Media Server.app/Contents/MacOS/Plex Script Host".replace(" ", "\ ")
    os.system("codesign --remove-signature {}".format(host_path))

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
    app_path = "/Applications/Plex Media Server.app".replace(" ", "\ ")
    os.system("open {}".format(app_path))

    # tail the log as dessert
    if args.tail_log: tail_log()

# ubuntu deployment
elif args.deploy and platform_system == 'linux':
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

    # tail the log as dessert
    if args.tail_log: tail_log()

# windows deployment
elif args.deploy and platform_system == 'windows':
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

    # tail the log as dessert
    if args.tail_log: tail_log()

# all set
cprint("> done")
