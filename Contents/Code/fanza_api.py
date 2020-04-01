from munch import munchify
from requests import get, Response
from pyquery import PyQuery as pq
from typing import List

api_id = "Ngdp9rsHvCZ9EWrv1LNU"
affiliate_id = "chokomomo-990"


def normalize(keyword):
    """
    :type keyword: str
    :rtype: str
    """
    keyword = keyword.lower()
    keyword = keyword.strip()
    keyword = keyword.replace("-", "00")
    keyword = keyword.replace("dsvr", "13dsvr")
    keyword = keyword.replace("313dsvr", "13dsvr")
    keyword = keyword.replace("avopvr", "h_1158avopvr")
    keyword = keyword.replace("kmvr", "84kmvr")
    keyword = keyword.replace("bi84kmvr", "h_1285bikmvr")
    keyword = keyword.replace("bzvr", "84bzvr")
    keyword = keyword.replace("crvr", "h_1155crvr")
    keyword = keyword.replace("exvr", "84exvr")
    keyword = keyword.replace("vvvr", "84vvvr")
    keyword = keyword.replace("dtvr", "24dtvr")
    keyword = keyword.replace("scvr", "h_565scvr")
    keyword = keyword.replace("wpvr", "2wpvr")
    keyword = keyword.replace("mxvr", "h_1282mxvr")
    keyword = keyword.replace("tmavr", "55tmavr")
    keyword = keyword.replace("vovs", "h_1127vovs")
    keyword = keyword.replace("cafr", "h_1116cafr")
    keyword = keyword.replace("tpvr", "h_1256tpvr")
    return keyword


def denormalize(keyword):
    keyword = keyword.lower()
    keyword = keyword.strip()
    keyword = keyword.replace("dsvr00", "13dsvr")
    keyword = keyword.replace("313dsvr00", "13dsvr")
    keyword = keyword.replace("h_1158avopvr00", "avopvr")
    keyword = keyword.replace("84kmvr00", "kmvr")
    keyword = keyword.replace("h_1285bikmvr00", "bi84kmvr")
    keyword = keyword.replace("84bzvr00", "bzvr")
    keyword = keyword.replace("h_1155crvr00", "crvr")
    keyword = keyword.replace("84exvr00", "exvr")
    keyword = keyword.replace("84vvvr00", "vvvr")
    keyword = keyword.replace("24dtvr00", "dtvr")
    keyword = keyword.replace("h_565scvr00", "scvr")
    keyword = keyword.replace("2wpvr00", "wpvr")
    keyword = keyword.replace("h_1282mxvr00", "mxvr")
    keyword = keyword.replace("55tmavr00", "tmavr")
    keyword = keyword.replace("h_1127vovs00", "vovs")
    keyword = keyword.replace("h_1116cafr00", "cafr")
    keyword = keyword.replace("h_1256tpvr00", "tpvr")
    return keyword


def search_item(keyword):
    """
    :type keyword: str
    :rtype: GetItemListBody
    """
    return munchify(get("https://api.dmm.com/affiliate/v3/ItemList", params={
        "api_id": api_id,
        "affiliate_id": affiliate_id,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "hits": "10",
        "sort": "date",
        "keyword": normalize(keyword),
        "output": "json"
    }).json())


def get_item(content_id):
    """
    :type content_id: str
    :rtype: GetItemListBody
    """
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
    return pq(url)(".mg-b20.lh4").text().rstrip()


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

    request = Request()
    result = Result()
#
