import sys

import environments
import sentry_sdk

sentry_sdk.init("https://0305a63d16a24e2eadfc2447182db26b@o148305.ingest.sentry.io/5205047")

if "pytest" in sys.modules:
    environments.is_local_debugging = True

if environments.is_local_debugging:
    from framework.plex_log import Log
else:
    from jav_agent import JavMovieAgent


# noinspection PyPep8Naming
def Start():
    Log.Debug("=========== Start ==========")
    Log.Debug("Python version")
    Log.Debug(sys.version)
    Log.Debug("Version info")
    Log.Debug(sys.version_info)
    Log.Debug("sys.executable: {}".format(sys.executable))
    for i, path in enumerate(sys.path):
        Log.Debug("sys.path[{}]: {}".format(i, path))


if not environments.is_local_debugging:
    JavMovieAgent = JavMovieAgent
