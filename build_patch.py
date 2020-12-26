import os
import platform
import shutil

import colorama
from PIL import ImageFile
from termcolor import cprint

# allow command line coloring
colorama.init()

# variables
etc_dir = 'etc'
platform_system = platform.system().lower()


def patch_image_file(code_path):
    cprint("> patching image file")
    cprint("code_path: {}".format(code_path), 'yellow')
    if code_path.endswith('pyc'):
        code_path = code_path[:-1]
        cprint("code_path (corrected): {}".format(code_path), 'yellow')
    code = open(code_path).read()
    code = code.replace("import traceback, string, os", "import traceback, string, os, io")
    code = code.replace("except AttributeError", "except (AttributeError, io.UnsupportedOperation)")
    open(code_path, 'w').write(code)


def patch_windows_pillow(lib_dir):
    # show be done in windows only
    cprint("> patching pillow modules")
    if platform_system != 'windows':
        cprint("this should only happen in windows, patch failed", 'red')
        exit(1)
    egg_dir = os.path.join(etc_dir, 'Pillow-1.7.8-py2.7-win32')
    egg_info_dir = os.path.join(egg_dir, 'EGG-INFO')
    cprint("lib_dir: {}".format(lib_dir), 'yellow')
    cprint("egg_dir: {}".format(egg_dir), 'yellow')
    cprint("egg_info_dir: {}".format(egg_info_dir), 'yellow')
    for dir_name, subdir_names, file_names in os.walk(egg_dir):
        if not dir_name.startswith(egg_info_dir):
            for file_name in file_names:
                source_path = os.path.join(dir_name, file_name)
                destination_path = os.path.join(lib_dir, file_name)
                action = "replacing:" if os.path.exists(destination_path) else 'copying:  '
                cprint("{} {}".format(action, destination_path), 'yellow')
                try:
                    shutil.copyfile(source_path, destination_path)
                except IOError as error:
                    cprint('replacing failed and skipped. {}'.format(error.__str__().replace('\\\\', "\\")), 'red')


if __name__ == '__main__':
    if platform_system == 'windows': patch_windows_pillow(os.path.dirname(ImageFile.__file__))
    patch_image_file(ImageFile.__file__)
