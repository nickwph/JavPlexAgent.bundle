import re
import os
from termcolor import cprint


def extract_replacements_from_filenames(src_dir, dir_name, file_names, local=False):
    replacements = []
    for file_name in file_names:
        if not file_name.endswith("_test.py") and (dir_name == src_dir or not file_name.startswith("__")) and file_name.endswith(".py"):
            package_name = dir_name.replace(src_dir, "").replace(os.path.sep, "", 1).replace(os.path.sep, ".")
            module_name = file_name.replace(".py", "")
            new_module_name = "{}_{}".format(package_name.replace(".", "_"), module_name)
            replacement = Replacement(None if local else package_name, module_name, new_module_name)
            replacements.append(replacement)
    return replacements


class Replacement:

    def __init__(self, old_package, old_module, new_module):

        self.old_package = old_package
        self.old_module = old_module
        self.new_module = new_module
        if self.old_package == "" or self.old_package is None:
            cprint("replace {} with {}".format(self.old_module, self.new_module), 'yellow')
        else:
            cprint("replace {}.{} with {}".format(self.old_package, self.old_module, self.new_module), 'yellow')

    def replace(self, it_code):

        if self.old_package is None:  # it's in the same directory

            import_pattern = r"^(import {})$".format(self.old_module)
            import_replacement = r"#FIXME \1\nimport {}".format(self.new_module)
            import_description = "replacing import:   'import {}' with 'import {}'".format(self.old_module, self.new_module)
            import_found = re.findall(import_pattern, it_code, flags=re.MULTILINE)
            if import_found:
                cprint(import_description, 'yellow')
                it_code = re.sub(import_pattern, import_replacement, it_code, flags=re.MULTILINE)

            import_as_pattern = r"^(import {} as (.*?))$".format(self.old_module)
            import_as_replacement = r"#FIXME \1\nimport {} as \2".format(self.new_module)
            import_as_description = "replacing import:   'import {} as ()' with 'import {} as ()'".format(self.old_module, self.new_module)
            import_as_found = re.findall(import_as_pattern, it_code, flags=re.MULTILINE)
            if import_as_found:
                cprint(import_as_description, 'yellow')
                it_code = re.sub(import_as_pattern, import_as_replacement, it_code, flags=re.MULTILINE)

        else:

            import_pattern = r"^(from {} import {})$".format(self.old_package, self.old_module)
            import_replacement = r"#FIXME \1\nimport {}".format(self.new_module)
            import_description = "replacing import:   'from {} import {}' with 'import {}'".format(self.old_package, self.old_module, self.new_module)
            import_found = re.findall(import_pattern, it_code, flags=re.MULTILINE)
            if import_found:
                cprint(import_description, 'yellow')
                it_code = re.sub(import_pattern, import_replacement, it_code, flags=re.MULTILINE)

            import_as_pattern = r"^(from {} import {} as (.*?))$".format(self.old_package, self.old_module)
            import_as_replacement = r"#FIXME \1\nimport {} as \2".format(self.new_module)
            import_as_description = "replacing import:   'from {} import {} as ()' with 'import {} as ()'".format(self.old_package, self.old_module, self.new_module)
            import_as_found = re.findall(import_as_pattern, it_code, flags=re.MULTILINE)
            if import_as_found:
                cprint(import_as_description, 'yellow')
                it_code = re.sub(import_as_pattern, import_as_replacement, it_code, flags=re.MULTILINE)

        module_found = re.findall(r"(\s{}\.)".format(self.old_module), it_code, flags=re.MULTILINE)
        module_pattern = r"^([^#](.*?\s){}(\..*?))$".format(self.old_module)
        module_replacement = r"#FIXME \1\n \2{}\3".format(self.new_module)
        module_description = "replacing variable: '{}' with '{}'".format(self.old_module, self.new_module)
        if module_found:
            cprint(module_description, 'yellow')
            for _ in range(len(module_found)):
                it_code = re.sub(module_pattern, module_replacement, it_code, flags=re.MULTILINE)

        return it_code
