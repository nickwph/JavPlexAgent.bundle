import requests
from munch import munchify
from typing import List, Dict
import humps

def get_by_id(id):
    request = requests.get("https://www.1pondo.tv/dyn/phpauto/movie_details/movie_id/070711_130.json")
    json = request.json()
    muchified = munchify(json)
    result = humps.decamelize(muchified)
    print result
    return result


class PondoItem(object):
    actor = "Stub"
    actor_id = []  # type: List[int]
    actresses_ja = []  # type: List[str]
    actresses_en = []  # type: List[str]
    actresses_list = {}  # type: Dict[str, Actress] # actor_id as string
    avg_rating = 0.0  # Stub
    can_stream = False  # Stub
    conditions = None  # Stub
    desc = "Stub"
    desc_en = "Stub"
    duration = 0  # Stub
    expire = None  # Stub
    has_flash = False  # Stub
    no_list_display = False  # Stub
    sample_exclude_flag = False  # Stub
    gallery = False  # Stub
    aff_zip = False  # Stub
    has_gallery = False  # Stub
    has_member_gallery_zip = False  # Stub
    has_sample_gallery_zip = False  # Stub
    meta_movie_id = 0  # Stub
    movie_id = "Stub"
    movie_seq = 0  # Stub
    movie_thumb = "Stub"
    real_meta_movie_id = 0  # Stub
    release = "Stub"
    series = None  # Stub
    series_en = None  # Stub
    series_id = None  # Stub
    site_id = 0  # Stub
    status = False  # Stub
    thumb_high = "Stub"
    thumb_low = "Stub"
    thumb_med = "Stub"
    thumb_ultra = "Stub"
    title = "Stub"
    title_en = "Stub"
    type = 0  # Stub
    year = "Stub"
    uc = []  # type: List[int]
    uc_name = []  # type: List[str]
    uc_name_en = []  # type: List[str]
    uc_name_list = {}  # type: Dict[str, UcName] # uc_id as string
    is_ticket_only = False  # Stub
    member_files = []  # type: List[MemberFile]
    ppv_price = object  # type: PpvPrice

    class Actress(object):
        name_ja = "Stub"
        name_en = "Stub"
        sizes = "Stub"
        age = None  # Stub

    class UcName(object):
        name_en = "Stub"
        name_ja = "Stub"

    class MemberFile(object):
        file_name = "Stub"
        file_size = 0  # Stub
        meta_movie_id = 0  # Stub
        site_id = "Stub"
        url = "Stub"

    class PpvPrice(object):
        file_name = "Stub"
        file_size = 0  # Stub
        meta_movie_id = 0  # Stub
        site_id = "Stub"
        url = "Stub"
