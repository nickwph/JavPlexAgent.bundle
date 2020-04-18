import sys

import environments
import sentry_sdk

sentry_sdk.init("https://0305a63d16a24e2eadfc2447182db26b@o148305.ingest.sentry.io/5205047")
sentry_sdk.utils.MAX_STRING_LENGTH = 4096

if "pytest" in sys.modules:
    environments.is_local_debugging = True

if environments.is_local_debugging:
    from framework.plex_log import Log
else:
    from jav_agent import JavMovieAgent


# noinspection PyPep8Naming
def Start():
    Log.Info("=========== Start ==========")
    Log.Info("Python version")
    Log.Info(sys.version)
    Log.Info("Version info")
    Log.Info(sys.version_info)
    Log.Info("sys.executable: {}".format(sys.executable))
    for i, path in enumerate(sys.path):
        Log.Info("sys.path[{}]: {}".format(i, path))


if not environments.is_local_debugging:
    JavMovieAgent = JavMovieAgent
