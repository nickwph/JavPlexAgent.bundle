# to be injected by build script
import platform
import socket

from plex.platform import Platform

version = ''
git_hash = ''
build_number = ''
build_datetime = ''
environment = ''
sentry_dsn = ''
mixpanel_token = ''

# produce other system information
plex_version = Platform.ServerVersion
full_version = "{}-{}-{}-{}".format(version, build_number, git_hash, build_datetime)
hostname = socket.gethostname()
os_name = 'Unknown'
os_version = ''
if platform.system().lower() == 'darwin':
    os_name = 'macOS'
    os_version = platform.mac_ver()[0]
elif platform.system().lower() == 'linux':
    linux_distribution = platform.linux_distribution()
    os_name = linux_distribution[0]
    os_version = linux_distribution[1]
elif platform.system().lower() == 'windows':
    os_name = 'Windows'
    os_version = platform.win32_ver()[0]
