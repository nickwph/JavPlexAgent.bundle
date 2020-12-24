import os
import re
from shutil import rmtree, copyfile, copytree
from os.path import expanduser
import platform
from build_replacement import extract_replacements_from_filenames

# variables
src_dir = 'src'
build_dir = 'build'
bundle_name = "JavPlexAgent.bundle"
content_dir = "{}/{}/Contents".format(build_dir, bundle_name)
code_dir = "{}/Code".format(content_dir)
libraries_dir = "{}/Libraries".format(content_dir)

# reset the build directory
rmtree(build_dir)
os.makedirs(code_dir)

# scan all files for import code replacements
print "setting up global replacements".format()
global_replacements = []
for dir_name, subdir_names, file_names in os.walk(src_dir):
    global_replacements += extract_replacements_from_filenames(src_dir, dir_name, file_names)

# copy files and fix up the imports
for dir_name, subdir_names, file_names in os.walk(src_dir):
    print "setting up local replacements for directory {}".format(dir_name)
    local_replacements = extract_replacements_from_filenames(src_dir, dir_name, file_names, True)
    for file_name in file_names:
        if not file_name.endswith("_test.py") and (dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            source_path = "{0}/{1}".format(dir_name, file_name)
            build_path = "{0}/{1}_{2}".format(code_dir, dir_name.replace(src_dir, "").replace("/", "_"), file_name).replace("_", "", 1)
            print "compiling {0} to {1}".format(source_path, build_path)
            with open(source_path) as source_file:
                code = source_file.read()
                code = re.sub(r'(\s*from environment.*?\n)', "\n", code)
                code = re.sub(r'(\s*if environments.*?\n)', "\n", code)
                code = re.sub(r'(\s*from plex.*?\n)', "\n", code)
                for replacement in local_replacements: code = replacement.replace(code)
                for replacement in global_replacements: code = replacement.replace(code)
                with open(build_path, 'w') as build_file:
                    build_file.write(code)

print "copying assets"
copyfile('assets/Info.plist', "{}/Info.plist".format(content_dir))
copyfile('assets/DefaultPrefs.json', "{}/DefaultPrefs.plist".format(content_dir))

print "gathering build information"
# print platform.architecture()
# print os.uname()
# print platform.machine()
# print os.name
# print platform.system()
# print platform.release()

platform_system = platform.system().lower()
platform_arch = platform.machine().lower()
platform_lib_dir = ""

print "> system: {}".format(platform_system)
print "> architecture: {}".format(platform_arch)

print "installing libraries"
# if platform_system == "darwin" a
# pip install --target build/JavPlexAgent.bundle/Contents/Libraries/Shared --ignore-installed --requirement requirements.txt
# pip install --target build/JavPlexAgent.bundle/Contents/Libraries/MacOSX/i386 --ignore-installed --requirement requirements_platform.txt
common_flags = "--no-python-version-warning --disable-pip-version-check --quiet"
os.system('pip install {} --target {}/Shared --requirement requirements.txt'.format(common_flags, libraries_dir))
# os.system('pip install {} --target {}/Shared --requirement requirements_platform.txt'.format(common_flags, libraries_dir))
os.system('pip install {} --target {}/MacOSX/i386 --requirement requirements_platform.txt'.format(common_flags, libraries_dir))

print "generating artifacts"
print "> javplexagent-1.2.0-{}-{}".format(platform_system, platform_arch)
# zip: javplexagent-1.2.0-macos-x86_64
# zip: javplexagent-1.2.0-macos-arch64
# zip: javplexagent-1.2.0-ubuntu-arm64
# zip: javplexagent-1.2.0-windows-x86_64
# tar -czvf build/javplexagent-1.2.0-macos-x86_64.tar.gz -C build JavPlexAgent.bundle

# replacing the one in plugins
print "replacing plugin locally"
from_path = "build/JavPlexAgent.bundle"
to_path = expanduser("~/Library/Application Support/Plex Media Server/Plug-ins/JavPlexAgent.bundle")
if os.path.exists(to_path): rmtree(to_path)
copytree(from_path, to_path)

print "done"
