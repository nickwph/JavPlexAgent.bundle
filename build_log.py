import argparse
import datetime
import os
import platform
import re
import sys
import tarfile
from os.path import expanduser
from shutil import rmtree, copyfile, copytree

import colorama
import psutil
from colorama import Fore, Style
from termcolor import cprint

from build_patch import patch_image_file, patch_windows_pillow
from build_replacement import extract_replacements_from_filenames

# allow command line coloring
colorama.init()


def tail_log():
    colors = ""
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('DEBUG', Fore.CYAN, Fore.RESET)
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('INFO', Fore.RESET, Fore.RESET)
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('WARN', Fore.YELLOW, Fore.RESET)
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('ERROR', Fore.RED, Fore.RESET)
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('CRITICAL', Fore.RED + Style.BRIGHT, Fore.RESET + Style.RESET_ALL)
    colors += '/{}/ {{print "{}" $0 "{}"; next}} '.format('EXCEPTION', Fore.MAGENTA + Style.BRIGHT, Fore.RESET + Style.RESET_ALL)
    colors += '{print $0}'
    if platform.system().lower() == 'darwin': # mac
        cprint("> tailing log")
        log_path = "~/Library/Logs/Plex Media Server/PMS Plugin Logs/com.nicholasworkshop.javplexagent.log".replace(" ", "\ ")
        os.system("tail -F -n 200 {} | awk '{}'".format(log_path, colors))
    elif platform.system().lower() == 'linux': # ubuntu
        cprint("> tailing log")
        log_path = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.nicholasworkshop.javplexagent.log".replace(" ", "\ ")
        os.system("tail -F -n 200 {} | awk '{}'".format(log_path, colors))
    elif platform.system().lower() == 'windows': # windows
        cprint("> tailing log")
        cprint("sorry it is not available yet, open this file by yourself", 'yellow')
        cprint("%LOCALAPPDATA%\Plex Media Server\Logs\PMS Plugin Logs\com.nicholasworkshop.javplexagent", 'yellow')


if __name__ == '__main__':
    tail_log()
