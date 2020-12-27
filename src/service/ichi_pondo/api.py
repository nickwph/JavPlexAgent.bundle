import re

import humps
import requests
from munch import munchify
from typing import List, Dict

from plex.log import Log

base_url = "https://www.1pondo.tv"


# noinspection SpellCheckingInspection
def extract_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    match = re.match("1Pon(do)?-(\d{6}_\d+)", filename, re.IGNORECASE)  # noqa: W605
    if match:
        return match.group(2)
    return None


def get_by_id(id):
    """
    :type id: str
    :rtype: OnePondoItem
    """
    url = "{}/dyn/phpauto/movie_details/movie_id/{}.json".format(base_url, id)
    request = requests.get(url)
    json = request.json()
    humped = humps.depascalize(json)

    humped['uc'] = humped['UC']
    del humped['UC']
    humped['uc_name'] = humped['UCNAME']
    del humped['UCNAME']
    humped['uc_name_en'] = humped['ucname_en']
    del humped['ucname_en']
    for file in humped["member_files"]:
        file['url'] = file['URL']
        del file['URL']
    for file in humped["sample_files"]:
        file['url'] = file['URL']
        del file['URL']
    humped['avg_rating'] = float(humped['avg_rating'])

    muchified = munchify(humped)
    Log.Debug("url: {}".format(url))
    print muchified
    return muchified


def get_actress_by_id(id):
    """
    :type id: int
    :rtype: OnePondoActress
    """
    url = "{}/dyn/phpauto/actresses.json".format(base_url)
    request = requests.get(url)
    json = request.json()
    for column_key in json:
        for row_key in json[column_key]:
            for actress in json[column_key][row_key]:
                if actress['id'] == id:
                    actress['image_url'] = base_url + actress['image_url']
                    return munchify(actress)  # type: OnePondoActress
    return None


class OnePondoActress(object):
    def __init__(self):
        self.id = 0  # Stub
        self.image_url = "Stub"
        self.kana = "Stub"
        self.name = "Stub"
        self.site_id = 0  # Stub


class OnePondoItem(object):
    def __init__(self):
        self.actor = "Stub"
        self.actor_id = []  # type: List[int]
        self.actresses_ja = []  # type: List[str]
        self.actresses_en = []  # type: List[str]
        self.actresses_list = {}  # type: Dict[str, OnePondoItem.Actress] # actor_id as string
        self.actor_thumb = "Stub"
        self.avg_rating = 0.0  # Stub
        self.can_stream = False  # Stub
        self.conditions = None  # Stub
        self.desc = "Stub"
        self.desc_en = "Stub"
        self.duration = 0  # Stub
        self.expire = None  # Stub
        self.has_flash = False  # Stub
        self.no_list_display = False  # Stub
        self.sample_exclude_flag = False  # Stub
        self.gallery = False  # Stub
        self.aff_zip = False  # Stub
        self.has_gallery = False  # Stub
        self.has_member_gallery_zip = False  # Stub
        self.has_sample_gallery_zip = False  # Stub
        self.meta_movie_id = 0  # Stub
        self.movie_id = "Stub"
        self.movie_seq = 0  # Stub
        self.movie_thumb = "Stub"
        self.real_meta_movie_id = 0  # Stub
        self.release = "Stub"
        self.series = None  # Stub
        self.series_en = None  # Stub
        self.series_id = None  # Stub
        self.site_id = 0  # Stub
        self.status = False  # Stub
        self.thumb_high = "Stub"
        self.thumb_low = "Stub"
        self.thumb_med = "Stub"
        self.thumb_ultra = "Stub"
        self.title = "Stub"
        self.title_en = "Stub"
        self.type = 0  # Stub
        self.year = "Stub"
        self.uc = []  # type: List[int]
        self.uc_name = []  # type: List[str]
        self.uc_name_en = []  # type: List[str]
        self.uc_name_list = {}  # type: Dict[str, OnePondoItem.UcName] # uc_id as string
        self.is_ticket_only = False  # Stub
        self.member_files = []  # type: List[OnePondoItem.File]
        self.sample_files = []  # type: List[OnePondoItem.File]
        self.ppv_price = OnePondoItem.PpvPrice()

    class Actress(object):
        def __init__(self):
            self.name_ja = "Stub"
            self.name_en = "Stub"
            self.sizes = "Stub"
            self.age = None  # Stub

    class UcName(object):
        def __init__(self):
            self.name_en = "Stub"
            self.name_ja = "Stub"

    class File(object):
        def __init__(self):
            self.file_name = "Stub"
            self.file_size = 0  # Stub
            self.meta_movie_id = 0  # Stub
            self.site_id = "Stub"
            self.url = "Stub"

    class PpvPrice(object):
        def __init__(self):
            self.regular = 0  # Stub
            self.discount = 0  # Stub
            self.campaign = 0  # Stub
