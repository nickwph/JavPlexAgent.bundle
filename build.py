import os
import re
from shutil import rmtree

from build_replacement import extract_replacements_from_filenames

# variables
src_dir = 'src/main'
build_dir = 'build'
bundle_name = "JavPlexAgent.bundle"
code_dir = "{0}/{1}/Contents/Code".format(build_dir, bundle_name)

# reset the build directory
rmtree(build_dir)
os.makedirs(code_dir)

# scan all files for import code replacements
print "setting up global replacements".format()
global_replacements = []
for dir_name, subdir_names, file_names in os.walk(src_dir):
    global_replacements += extract_replacements_from_filenames(src_dir, dir_name, file_names)
print

# copy files and fix up the imports
for dir_name, subdir_names, file_names in os.walk(src_dir):
    print "setting up local replacements for directory {}".format(dir_name)
    local_replacements = extract_replacements_from_filenames(src_dir, dir_name, file_names, True)
    print
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
            print
