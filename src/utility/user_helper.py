from uuid import uuid4

from plex.dict import Dict
from plex.log import Log

is_new_user_id = False


def reset_user_id():
    Log.Warn("Resetting user ID")
    del Dict['user_id']
    Dict.Save()


def get_user_id():
    global is_new_user_id
    if 'user_id' not in Dict:
        Log.Info("Generating new user ID")
        Dict['user_id'] = str(uuid4().hex)
        Dict.Save()
        is_new_user_id = True
    Log.Debug("user_id: {}".format(Dict['user_id']))
    Log.Debug("is_new_user_id: {}".format(is_new_user_id))
    return Dict['user_id']
