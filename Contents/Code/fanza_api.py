from urllib2 import HTTPError

from munch import munchify
from pyquery import PyQuery
from requests import get
from typing import List

import environments

if environments.is_local_debugging:
    from framework.plex_log import Log

api_id = "Ngdp9rsHvCZ9EWrv1LNU"
affiliate_id = "chokomomo-990"


def parse_as_dvd_product_id(product_id):
    """
    :type product_id: str
    :rtype: str
    """
    product_id = product_id.lower()
    product_id = product_id.strip()
    product_id = product_id.replace("-", "")
    return product_id


def parse_as_digital_product_id(product_id):
    """
    :type product_id: str
    :rtype: str
    """
    product_id = product_id.lower()
    product_id = product_id.strip()
    product_id = product_id.replace("-", "00")
    product_id = replace_prefix(product_id, "dsvr", "13dsvr")
    product_id = replace_prefix(product_id, "313dsvr", "13dsvr")
    product_id = replace_prefix(product_id, "avopvr", "h_1158avopvr")
    product_id = replace_prefix(product_id, "kmvr", "84kmvr")
    product_id = replace_prefix(product_id, "bi84kmvr", "h_1285bikmvr")
    product_id = replace_prefix(product_id, "bzvr", "84bzvr")
    product_id = replace_prefix(product_id, "crvr", "h_1155crvr")
    product_id = replace_prefix(product_id, "exvr", "84exvr")
    product_id = replace_prefix(product_id, "vvvr", "84vvvr")
    product_id = replace_prefix(product_id, "dtvr", "24dtvr")
    product_id = replace_prefix(product_id, "scvr", "h_565scvr")
    product_id = replace_prefix(product_id, "wpvr", "2wpvr")
    product_id = replace_prefix(product_id, "mxvr", "h_1282mxvr")
    product_id = replace_prefix(product_id, "tmavr", "55tmavr")
    product_id = replace_prefix(product_id, "vovs", "h_1127vovs")
    product_id = replace_prefix(product_id, "cafr", "h_1116cafr")
    product_id = replace_prefix(product_id, "tpvr", "h_1256tpvr")
    return product_id


def replace_prefix(text, prefix, new_prefix):
    """
    :type text: str
    :type prefix: str
    :type new_prefix: str
    :rtype: str
    """
    if text.startswith(prefix):
        return text.replace(prefix, new_prefix, 1)
    return text


def search_dvd_product(product_id):
    """
    :type product_id: str
    :rtype: GetItemListBody
    """
    keyword = parse_as_dvd_product_id(product_id)
    return munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "mono",
        "floor": "dvd",
        "hits": "10",
        "sort": "date",
        "keyword": keyword,
        "output": "json"
    }).json())


def search_digital_product(product_id):
    """
    :type product_id: str
    :rtype: GetItemListBody
    """
    keyword = parse_as_digital_product_id(product_id)
    return munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "10",
        "sort": "date",
        "keyword": keyword,
        "output": "json"
    }).json())


def get_dvd_product(product_id):
    """
    :type product_id: str
    :rtype: GetItemListBody
    """
    content_id = parse_as_dvd_product_id(product_id)
    return munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "mono",
        "floor": "dvd",
        "hits": "10",
        "sort": "date",
        "cid": content_id,
        "output": "json"
    }).json())


def get_digital_product(product_id):
    """
    :type product_id: str
    :rtype: GetItemListBody
    """
    content_id = parse_as_digital_product_id(product_id)
    return munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "10",
        "sort": "date",
        "cid": content_id,
        "output": "json"
    }).json())


def get_product_description(url):
    """
    :type url: str
    :rtype: str
    """
    try:
        return PyQuery(url)(".mg-b20.lh4").text().rstrip()
    except HTTPError as error:
        Log.Debug(error.msg)
        return None


def get_actress(actress_id):
    """
    :type actress_id: int
    :rtype: ActressResponseBody
    """
    return munchify(get("https://api.dmm.com/affiliate/v3/ActressSearch", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "actress_id": actress_id,
        "output": "json"
    }).json())


class ActressResponseBody(object):
    request = object  # type: ActressResponseBody.Request
    result = object  # type: ActressResponseBody.Result

    class Request(object):
        class Parameters(object):
            api_id = "Stub"
            affiliate_id = "Stub"
            actress_id = "Stub"
            output = "Stub"

        parameters = Parameters()

    class Result(object):
        status = 0  # Stub
        result_count = 0  # Stub
        total_count = 0  # Stub
        first_position = 0  # Stub
        actress = []  # type: List[Actress]


class Actress(object):
    birthday = "Stub"
    blood_type = "Stub"
    bust = "Stub"
    height = "Stub"
    hip = "Stub"
    hobby = "Stub"
    id = "Stub"
    imageURL = object  # type: Actress.ImageUrl
    listURL = object  # type: Actress.ListUrl
    name = "Stub"
    prefectures = "Stub"
    ruby = "Stub"
    waist = "Stub"

    class ImageUrl(object):
        large = "Stub"
        small = "Stub"

    class ListUrl(object):
        digital = "Stub"
        mono = "Stub"
        monthly = "Stub"
        ppm = "Stub"
        rental = "Stub"


# noinspection SpellCheckingInspection
class Item(object):
    class Review(object):
        count = 0  # Stub
        average = "Stub"

    class ImageUrl(object):
        list = "Stub"
        small = "Stub"
        large = "Stub"

    class SampleImageUrl(object):
        class Sample(object):
            image = []  # type: List[str]

        sample_s = Sample()

    class SampleMovieURL(object):
        sp_flag = 0  # Stub
        size_560_360 = "Stub"
        size_644_414 = "Stub"
        size_720_480 = "Stub"
        size_476_306 = "Stub"

    class Prices(object):
        class Deliveries(object):
            class Delivery(object):
                type = "Stub"
                price = "Stub"

            delivery = Delivery()

        deliveries = Deliveries()
        price = "Stub"

    class ItemInfo(object):
        class Info(object):
            id = 0  # Stub
            name = "Stub"

        genre = []  # type: List[Info]
        series = []  # type: List[Info]
        maker = []  # type: List[Info]
        actress = []  # type: List[Info]
        director = []  # type: List[Info]
        label = []  # type: List[Info]

    service_code = "Stub"
    service_name = "Stub"
    floor_code = "Stub"
    floor_name = "Stub"
    category_name = "Stub"
    content_id = "Stub"
    product_id = "Stub"
    title = "Stub"
    volume = "Stub"
    review = Review
    URL = "Stub"
    URLsp = "Stub"
    affiliateUrl = "Stub"
    affiliateUrLsp = "Stub"
    imageURL = ImageUrl
    sampleImageURL = SampleImageUrl()
    sampleMovieURL = SampleMovieURL()
    prices = Prices()
    date = "Stub"
    iteminfo = ItemInfo()


class GetItemListBody(object):
    class Request(object):
        class Parameters(object):
            api_id = "Stub"
            affiliate_id = "Stub"
            site = "Stub"
            service = "Stub"
            floor = "Stub"
            hits = "Stub"
            sort = "Stub"
            keyword = "Stub"
            output = "Stub"

        parameters = Parameters()

    class Result(object):
        status = 0  # Stub
        result_count = 0  # Stub
        total_count = 0  # Stub
        first_position = 0  # Stub
        items = [Item()]

        def __getitem__(self, item):
            """
            :rtype: Item
            """
            pass

    request = Request()
    result = Result()
#
