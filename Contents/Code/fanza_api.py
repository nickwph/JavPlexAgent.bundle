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
    product_id = product_id.replace("dsvr", "13dsvr")
    product_id = product_id.replace("313dsvr", "13dsvr")
    product_id = product_id.replace("avopvr", "h_1158avopvr")
    product_id = product_id.replace("kmvr", "84kmvr")
    product_id = product_id.replace("bi84kmvr", "h_1285bikmvr")
    product_id = product_id.replace("bzvr", "84bzvr")
    product_id = product_id.replace("crvr", "h_1155crvr")
    product_id = product_id.replace("exvr", "84exvr")
    product_id = product_id.replace("vvvr", "84vvvr")
    product_id = product_id.replace("dtvr", "24dtvr")
    product_id = product_id.replace("scvr", "h_565scvr")
    product_id = product_id.replace("wpvr", "2wpvr")
    product_id = product_id.replace("mxvr", "h_1282mxvr")
    if product_id.startswith("tmavr"):
        product_id = product_id.replace("tmavr", "55tmavr")
    product_id = product_id.replace("vovs", "h_1127vovs")
    product_id = product_id.replace("cafr", "h_1116cafr")
    product_id = product_id.replace("tpvr", "h_1256tpvr")
    return product_id


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
        Log.Error(error.msg)
        return None


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
