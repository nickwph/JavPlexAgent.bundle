# from environments import is_local_debugging
# from framework import Log
import os
import sys

Log.Error(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


# noinspection PyPep8Naming
def Start():
    from framework.log import Log
    Log.Error("=========== Start ==========")


# noinspection PyMethodMayBeStatic
