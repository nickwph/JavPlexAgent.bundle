# log when it happens
from uuid import uuid4

from plex.dict import Dict


def get_user_id():
    if 'user_id' not in Dict:
        Dict['user_id'] = str(uuid4().hex)
        Dict.Save()
    return Dict['user_id']
