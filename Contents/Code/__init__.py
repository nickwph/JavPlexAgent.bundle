import sys
import os
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

source_dir = os.path.dirname(os.path.dirname(__file__))
if sys.platform == "darwin":  # MacOS
    sys.path.insert(0, '{}/Virtualenv/MacOS/lib/python2.7/site-packages'.format(source_dir))
elif sys.platform == "win32":
    Log.Error("Windows is not supported yet")
    pass
elif sys.platform == "linux" or sys.platform == "linux2":  # Ubuntu
    sys.path.insert(0, '{}/Virtualenv/Ubuntu/lib/python2.7/site-packages'.format(source_dir))
else:
    Log.Error("The plarform is not supported yet".format(sys.platform))


# noinspection PyPep8Naming
def Start():
    Log.Info("=========== Start ==========")
    Log.Info("System information")
    Log.Info("sys.version: {}".format(sys.version))
    Log.Info("sys.version_info: {}".format(sys.version_info))
    Log.Info("sys.platform: {}".format(sys.platform))
    Log.Info("sys.executable: {}".format(sys.executable))
    for i, path in enumerate(sys.path):
        Log.Info("sys.path[{}]: {}".format(i, path))


if not environments.is_local_debugging:
    JavMovieAgent = JavMovieAgent
