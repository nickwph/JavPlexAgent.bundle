import sys

from agent_movie_jav import JavMovieAgent
from environments import is_local_debugging

if is_local_debugging:
    from framework.framework_log import Log


# noinspection PyPep8Naming
def Start():
    Log.Error("=========== Start ==========")
    Log.Error("sys.executable: {}".format(sys.executable))
    for i, path in enumerate(sys.path):
        Log.Error("sys.path[{}]: {}".format(i, path))


JavMovieAgent = JavMovieAgent
