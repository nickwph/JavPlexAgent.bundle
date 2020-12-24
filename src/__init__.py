import sys

import sentry_sdk

from agent import JavMovieAgent
from plex.log import Log

sentry_sdk.init("https://0305a63d16a24e2eadfc2447182db26b@o148305.ingest.sentry.io/5205047")
sentry_sdk.utils.MAX_STRING_LENGTH = 4096


def Start():
    Log.Info("=========== Start ==========")
    Log.Info("System information")
    Log.Info("sys.version: {}".format(sys.version))
    Log.Info("sys.version_info: {}".format(sys.version_info))
    Log.Info("sys.platform: {}".format(sys.platform))
    Log.Info("sys.executable: {}".format(sys.executable))
    for i, path in enumerate(sys.path):
        Log.Info("sys.path[{}]: {}".format(i, path))


JavMovieAgent = JavMovieAgent
