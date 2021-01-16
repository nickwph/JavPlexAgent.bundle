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


def init_sentry(dsn, user_id, version, git_hash, build_number, build_datetime, environment, plex_version, os_name, os_version, hostname, full_version):
    Log.Warn('Initializing sentry')
    Log.Debug('dsn: {}'.format(dsn))
    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        traces_sample_rate=1.0,
        debug=True,
        before_send=before_send,
        release=full_version)
    sentry_utils.MAX_STRING_LENGTH = 4096
    sentry_sdk.set_user({'id': user_id, "email": hostname, 'hostname': hostname})
    sentry_sdk.set_tag("version", version)
    sentry_sdk.set_tag("git_hash", git_hash)
    sentry_sdk.set_tag("build_number", build_number)
    sentry_sdk.set_tag("build_datetime", build_datetime)
    sentry_sdk.set_tag("plex_version", plex_version)
    sentry_sdk.set_context('os', {'name': os_name, 'version': os_version})
