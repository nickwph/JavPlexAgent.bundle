import os
import platform
import re
from os.path import expanduser
from shutil import rmtree, copyfile, copytree
import tarfile

import psutil
from termcolor import cprint

from build_replacement import extract_replacements_from_filenames

# variables
src_dir = 'src'
build_dir = 'build'
outputs_dir = 'outputs'
bundle_name = "JavPlexAgent.bundle"
content_dir = "{}/{}/Contents".format(build_dir, bundle_name)
code_dir = "{}/Code".format(content_dir)
libraries_dir = "{}/Libraries".format(content_dir)

# reset the build directory
rmtree(build_dir)
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
        if not file_name.endswith("_test.py") and (dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            source_path = "{0}/{1}".format(dir_name, file_name)
            build_path = "{0}/{1}_{2}".format(code_dir, dir_name.replace(src_dir, "").replace("/", "_"), file_name).replace("_", "", 1)
            cprint("> compiling {0} to {1}".format(source_path, build_path), "grey")
            code = open(source_path).read()
            code = re.sub(r'(\s*from Framework.*?\n)', "\n", code)
            code = re.sub(r'(\s*from plex.*?\n)', "\n", code)
            for replacement in local_replacements: code = replacement.replace(code)
            for replacement in global_replacements: code = replacement.replace(code)
            open(build_path, 'w').write(code)

# setup basic bundle structure
cprint("> copying assets", "grey")
copyfile('assets/Info.plist', "{}/Info.plist".format(content_dir))
copyfile('assets/DefaultPrefs.json', "{}/DefaultPrefs.plist".format(content_dir))

# install the python libraries
cprint("> installing libraries", "grey")
common_flags = "--no-python-version-warning --disable-pip-version-check --upgrade --quiet"
os.system('pip install {} --target {}/Shared --requirement requirements.txt'.format(common_flags, libraries_dir))

# need some system info
cprint("> gathering build information", "grey")
platform_system = platform.system().lower()
platform_arch = platform.machine().lower()
cprint("system: {}".format(platform_system), 'yellow')
cprint("architecture: {}".format(platform_arch), 'yellow')

cprint("> generating artifact", "grey")
os.makedirs(outputs_dir)
artifact_name = "javplexagent-1.2.0-{}-{}".format(platform_system, platform_arch)
archive = tarfile.open("{}/{}.tar.gz".format(outputs_dir, artifact_name), mode='w:gz')
archive.add('{}/{}'.format(build_dir, bundle_name), arcname=bundle_name)
archive.close()
cprint("artifact: {}".format(artifact_name), 'yellow')
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
    if os.path.exists(to_path): rmtree(to_path)
    copytree(from_path, to_path)

    # restart the server
    cprint("> restarting server", "grey")
    for proc in psutil.process_iter():
        if proc.name() == "Plex Media Server": proc.kill()
    os.system("open /Applications/Plex\ Media\ Server.app")

cprint("> done", "grey")
