import os
import re
from shutil import copyfile, rmtree

# variables
src_dir = 'src/main'
build_dir = 'build'
bundle_name = "JavPlexAgent.bundle"
code_path = "{0}/{1}/Contents/Code".format(build_dir, bundle_name)

# reset the build directory
rmtree(build_dir)
os.makedirs(code_path)

# scan all files for import code replacements
replacements = []
for dir, subdirs, files in os.walk(src_dir):
    for file in files:
        if not file.startswith("test") and not file.startswith("__"):
            # print dir, subdirs, files
            py_package = dir.replace(src_dir, "").replace("/", "", 1).replace("/", ".")
            py_module = file.replace(".py", "")
            style_1_from = "from {0} import {1}".format(py_package, py_module)
            style_1_to = "import {0}_{1}".format(py_package.replace(".", "_"), py_module)
            style_2_from = "from {0}.{1} import".format(py_package, py_module)
            style_2_to = "from {0}_{1} import".format(py_package.replace(".", "_"), py_module)
            style_3_from = "import {0}".format(py_module)
            style_3_to = "import {0}_{1}".format(py_package.replace(".", "_"), py_module)
            style_4_from = "{0}.".format(py_module)
            style_4_to = "{0}_{1}.".format(py_package.replace(".", "_"), py_module)
            print "{0} => {1}".format(style_1_from, style_1_to)
            print "{0} => {1}".format(style_2_from, style_2_to)
            print "{0} => {1}".format(style_3_from, style_3_to)
            print "{0} => {1}".format(style_4_from, style_4_to)
            replacements.append((style_1_from, style_1_to))
            replacements.append((style_2_from, style_2_to))
            replacements.append((style_3_from, style_3_to))
            replacements.append((style_4_from, style_4_to))

# copy root init file and fix up the imports
copyfile("{0}/__init__.py".format(src_dir), "{0}/__init__.py".format(code_path))

# copy files and fix up the imports
for dir, subdirs, files in os.walk(src_dir):
    for file in files:
        if not file.startswith("test") and not file.startswith("__") and file.endswith(".py"):
            source_path = "{0}/{1}".format(dir, file)
            build_path = "{0}/{1}_{2}".format(code_path,
                                              dir.replace(src_dir, "").replace("/", "_"),
                                              file).replace("_", "", 1)
            print "compiling {0} to {1}".format(source_path, build_path)
            with open(source_path) as source_file:
                code = source_file.read()
                # temp
                code = re.sub(r'(\s*from environment.*?\n)', "\n", code)
                code = re.sub(r'(\s*if environments.*?\n)', "\n", code)
                code = re.sub(r'(\s*from plex.*?\n)', "\n", code)
                # temp
                for replacement in replacements:
                    code = code.replace(replacement[0], replacement[1])
                with open(build_path, 'w') as build_file:
                    build_file.write(code)

# print built_files

# remove any environment codes
