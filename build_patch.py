from PIL import ImageFile
from termcolor import cprint


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


if __name__ == '__main__':
    patch_image_file(ImageFile.__file__)
