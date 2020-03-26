import sys
if is_local_debugging:
    from framework.framework_log import Log
Log.Error("=========== Start ==========")
for i, path in enumerate(sys.path):
    Log.Error("sys.path[{}]: {}".format(i, path))

from agent_movie_jav import JavMovieAgent
from environments import is_local_debugging



# noinspection PyPep8Naming
def Start():
    Log.Error("=========== Start ==========")
    for i, path in enumerate(sys.path):
        Log.Error("sys.path[{}]: {}".format(i, path))


JavMovieAgent = JavMovieAgent
