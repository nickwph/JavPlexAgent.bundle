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
from termcolor import cprint

from build_patch import patch_image_file, patch_windows_pillow
from build_replacement import extract_replacements_from_filenames

# allow command line coloring
colorama.init()


def tail_log():
    # mac
    if platform.system().lower() == 'darwin':
        cprint("> tailing log")
        log_path = "~/Library/Logs/Plex Media Server/PMS Plugin Logs/com.nicholasworkshop.javplexagent.log".replace(" ", "\ ")
        color_debug = '/DEBUG/ {print "\033[35m" $0; next}'
        color_info = '/INFO/ {print "\033[39m" $0; next}'
        color_warn = '/WARN/ {print "\033[33m" $0; next}'
        color_error = '/ERROR/ {print "\033[31m" $0; next}'
        color_critical = '/CRITICAL/ {print "\033[41m\033[37m" $0; next}'
        color_exception = '/EXCEPTION/ {print "\033[41m\033[31m" $0; next}'
        color_default = '{print $0 "\033[39m\033[49m"}'
        os.system("tail -F -n 200 {} | awk '{} {} {} {} {} {} {}'".format(log_path, color_debug, color_info, color_warn, color_error, color_critical, color_exception, color_default))

    # ubuntu
    elif platform.system().lower() == 'linux':
        cprint("> tailing log")
        log_path = "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.nicholasworkshop.javplexagent.log".replace(" ", "\ ")
        color_debug = '/DEBUG/ {print "\033[35m" $0; next}'
        color_info = '/INFO/ {print "\033[39m" $0; next}'
        color_warn = '/WARN/ {print "\033[33m" $0; next}'
        color_error = '/ERROR/ {print "\033[31m" $0; next}'
        color_critical = '/CRITICAL/ {print "\033[41m\033[37m" $0; next}'
        color_exception = '/EXCEPTION/ {print "\033[41m\033[31m" $0; next}'
        color_default = '{print $0 "\033[39m\033[49m"}'
        os.system("tail -F -n 200 {} | awk '{} {} {} {} {} {} {}'".format(log_path, color_debug, color_info, color_warn, color_error, color_critical, color_exception, color_default))

    # windows
    elif platform.system().lower() == 'windows':
        cprint("> tailing log")
        cprint("sorry it is not available yet, open this file by yourself", 'yellow')
        cprint("%LOCALAPPDATA%\Plex Media Server\Logs\PMS Plugin Logs\com.nicholasworkshop.javplexagent", 'yellow')


if __name__ == '__main__':
    tail_log()
