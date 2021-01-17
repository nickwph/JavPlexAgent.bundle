import sentry_sdk
from sentry_sdk import utils as sentry_utils

import build_config
from plex.log import Log


def before_send(event, hint):
    if 'exception' in event:
        Log.Warn('Sending debug event to sentry')
        Log.Debug('event: {}'.format(event))
        Log.Debug('hint: {}'.format(hint))
        return event


def init_sentry(user_id):
    Log.Warn('Initializing sentry')
    Log.Debug('dsn: {}'.format(build_config.sentry_dsn))
    sentry_sdk.init(
        dsn=build_config.sentry_dsn,
        environment=build_config.environment,
        traces_sample_rate=1.0,
        debug=True,
        before_send=before_send,
        release=build_config.full_version)
    sentry_utils.MAX_STRING_LENGTH = 4096
    sentry_sdk.set_user({'id': user_id, "email": build_config.hostname, 'hostname': build_config.hostname})
    sentry_sdk.set_tag("version", build_config.version)
    sentry_sdk.set_tag("git_hash", build_config.git_hash)
    sentry_sdk.set_tag("build_number", build_config.build_number)
    sentry_sdk.set_tag("build_datetime", build_config.build_datetime)
    sentry_sdk.set_tag("plex_version", build_config.plex_version)
    sentry_sdk.set_context('os', {'name': build_config.os_name, 'version': build_config.os_version})
