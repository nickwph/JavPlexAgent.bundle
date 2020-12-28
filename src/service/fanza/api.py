from urllib2 import HTTPError

import requests
from munch import munchify
from pyquery import PyQuery
from requests import get
from typing import List

from plex.log import Log

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
    :rtype: ItemResponseBody
    """
    keyword = parse_as_dvd_product_id(product_id)
    result = munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "mono",
        "floor": "dvd",
        "hits": "10",
        "sort": "date",
        "keyword": keyword,
        "output": "json"
    }).json())  # type: ItemResponseBody
    result.result.items = result.result['items']
    return result


def search_digital_product(product_id):
    """
    :type product_id: str
    :rtype: ItemResponseBody
    """
    keyword = parse_as_digital_product_id(product_id)
    result = munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "10",
        "sort": "date",
        "keyword": keyword,
        "output": "json"
    }).json())  # type: ItemResponseBody
    result.result.items = result.result['items']
    return result


def get_dvd_product(product_id):
    """
    :type product_id: str
    :rtype: ItemResponseBody
    """
    content_id = parse_as_dvd_product_id(product_id)
    result = munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "mono",
        "floor": "dvd",
        "hits": "10",
        "sort": "date",
        "cid": content_id,
        "output": "json"
    }).json())  # type: ItemResponseBody
    result.result.items = result.result['items']
    return result


def get_digital_product(product_id):
    """
    :type product_id: str
    :rtype: ItemResponseBody
    """
    content_id = parse_as_digital_product_id(product_id)
    result = munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "10",
        "sort": "date",
        "cid": content_id,
        "output": "json"
    }).json())  # type: ItemResponseBody
    result.result.items = result.result['items']
    return result


def get_product_description(url):
    """
    :type url: str
    :rtype: str
    """
    try:
        cookies = {"age_check.done": "1", "cklg": "ja"}  # cklg=en for english
        request = requests.get(url, cookies=cookies)
        return PyQuery(request.text)(".mg-b20.lh4").text().rstrip()
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
    def __init__(self):
        self.request = ActressResponseBody.Request()
        self.result = ActressResponseBody.Result()

    class Request(object):
        def __init__(self):
            self.parameters = ActressResponseBody.Request.Parameters()

        class Parameters(object):
            def __init__(self):
                self.api_id = "Stub"
                self.affiliate_id = "Stub"
                self.actress_id = "Stub"
                self.output = "Stub"

    class Result(object):
        def __init__(self):
            self.status = 0  # Stub
            self.result_count = 0  # Stub
            self.total_count = 0  # Stub
            self.first_position = 0  # Stub
            self.actress = []  # type: List[Actress]


class Actress(object):
    def __init__(self):
        self.birthday = "Stub"
        self.blood_type = "Stub"
        self.bust = "Stub"
        self.height = "Stub"
        self.hip = "Stub"
        self.hobby = "Stub"
        self.id = "Stub"
        self.imageURL = Actress.ImageUrl()
        self.listURL = Actress.ListUrl()
        self.name = "Stub"
        self.prefectures = "Stub"
        self.ruby = "Stub"
        self.waist = "Stub"

    class ImageUrl(object):
        def __init__(self):
            self.large = "Stub"
            self.small = "Stub"

    class ListUrl(object):
        def __init__(self):
            self.digital = "Stub"
            self.mono = "Stub"
            self.monthly = "Stub"
            self.ppm = "Stub"
            self.rental = "Stub"


class ItemResponseBody(object):
    def __init__(self):
        self.request = ItemResponseBody.Request()
        self.result = ItemResponseBody.Result()

    class Request(object):
        def __init__(self):
            self.parameters = ItemResponseBody.Request.Parameters()

        class Parameters(object):
            def __init__(self):
                self.api_id = "Stub"
                self.affiliate_id = "Stub"
                self.site = "Stub"
                self.service = "Stub"
                self.floor = "Stub"
                self.hits = "Stub"
                self.sort = "Stub"
                self.keyword = "Stub"
                self.output = "Stub"

    class Result(object):
        def __init__(self):
            self.status = 0  # Stub
            self.result_count = 0  # Stub
            self.total_count = 0  # Stub
            self.first_position = 0  # Stub
            self.items = []  # type: list[Item]


class Item(object):
    def __init__(self):
        self.service_code = "Stub"
        self.service_name = "Stub"
        self.floor_code = "Stub"
        self.floor_name = "Stub"
        self.category_name = "Stub"
        self.content_id = "Stub"
        self.product_id = "Stub"
        self.title = "Stub"
        self.volume = "Stub"
        self.review = Item.Review()
        self.URL = "Stub"
        self.URLsp = "Stub"
        self.affiliateUrl = "Stub"
        self.affiliateUrLsp = "Stub"
        self.imageURL = Item.ImageUrl()
        self.sampleImageURL = Item.SampleImageUrl()
        self.sampleMovieURL = Item.SampleMovieURL()
        self.prices = Item.Prices()
        self.date = "Stub"
        self.iteminfo = Item.ItemInfo()

    class Review(object):
        def __init__(self):
            self.count = 0  # Stub
            self.average = "Stub"

    class ImageUrl(object):
        def __init__(self):
            self.list = "Stub"
            self.small = "Stub"
            self.large = "Stub"

    class SampleImageUrl(object):
        def __init__(self):
            self.sample_s = Item.SampleImageUrl.Sample()

        class Sample(object):
            def __init__(self):
                self.image = []  # type: List[str]

    class SampleMovieURL(object):
        def __init__(self):
            self.sp_flag = 0  # Stub
            self.size_560_360 = "Stub"
            self.size_644_414 = "Stub"
            self.size_720_480 = "Stub"
            self.size_476_306 = "Stub"

    class Prices(object):
        def __init__(self):
            self.deliveries = Item.Prices.Deliveries()
            self.price = "Stub"

        class Deliveries(object):
            def __init__(self):
                self.delivery = Item.Prices.Deliveries.Delivery()

            class Delivery(object):
                def __init__(self):
                    self.type = "Stub"
                    self.price = "Stub"

    class ItemInfo(object):
        def __init__(self):
            self.genre = []  # type: List[Item.ItemInfo.Info]
            self.series = []  # type: List[Item.ItemInfo.Info]
            self.maker = []  # type: List[Item.ItemInfo.Info]
            self.actress = []  # type: List[Item.ItemInfo.Info]
            self.director = []  # type: List[Item.ItemInfo.Info]
            self.label = []  # type: List[Item.ItemInfo.Info]

        class Info(object):
            def __init__(self):
                self.id = 0  # Stub
                self.name = "Stub"
