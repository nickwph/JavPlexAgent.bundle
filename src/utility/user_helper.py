# log when it happens
from uuid import uuid4

from plex.dict import Dict

is_new_user_id = False

def get_user_id():
    if 'user_id' not in Dict:
        Dict['user_id'] = str(uuid4().hex)
        Dict.Save()
        global is_new_user_id
        is_new_user_id = True
    return Dict['user_id']
