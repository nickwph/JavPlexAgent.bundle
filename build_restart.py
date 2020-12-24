import os
import platform
import re
from os.path import expanduser
from shutil import rmtree, copyfile, copytree
from colorama import Fore, Back, Style

import psutil
from termcolor import cprint

from build_replacement import extract_replacements_from_filenames

cprint("> restarting server", "green")
for proc in psutil.process_iter():
    if proc.name() == "Plex Media Server":
        proc.kill()
os.system("open  /Applications/Plex\ Media\ Server.app")

cprint("> done", "green")
