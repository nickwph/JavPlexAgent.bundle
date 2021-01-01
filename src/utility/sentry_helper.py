# log when it happens
import platform
import socket

import sentry_sdk
from sentry_sdk import utils as sentry_utils

from plex.log import Log
from plex.platform import Platform


def before_send(event, hint):
    if 'exception' in event:
        Log.Warn('Sending debug event to sentry')
        Log.Debug('event: {}'.format(event))
        Log.Debug('hint: {}'.format(hint))
        return event


def init_sentry(user_id, version, git_hash, build_number, build_datetime, environment):
    Log.Warn('Initializing sentry')
    sentry_sdk.init(
        dsn="https://81a6a4b2981a4d7487660950d8324bd7@o148305.ingest.sentry.io/5576704",
        environment=environment,
        traces_sample_rate=1.0,
        debug=True,
        before_send=before_send,
        release="{}-{}-{}".format(version, build_number, git_hash))
    sentry_utils.MAX_STRING_LENGTH = 4096
    sentry_sdk.set_user({'id': user_id, "email": socket.gethostname(), 'hostname': socket.gethostname()})
    sentry_sdk.set_tag("version", version)
    sentry_sdk.set_tag("git_hash", git_hash)
    sentry_sdk.set_tag("build_number", build_number)
    sentry_sdk.set_tag("build_datetime", build_datetime)
    sentry_sdk.set_tag("plex_version", Platform.ServerVersion)
    if platform.system().lower() == 'darwin':
        sentry_sdk.set_context('os', {'name': "macOS", 'version': platform.mac_ver()[0]})
    elif platform.system().lower() == 'linux':
        linux_distribution = platform.linux_distribution()
        sentry_sdk.set_context('os', {'name': linux_distribution[0], 'version': linux_distribution[1]})
    elif platform.system().lower() == 'darwin':
        sentry_sdk.set_context('os', {'name': "Windows", 'version': platform.win32_ver()[0]})
