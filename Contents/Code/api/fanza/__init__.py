import requests
from requests import Response
from pyquery import PyQuery as pq

api_id = "Ngdp9rsHvCZ9EWrv1LNU"
affiliate_id = "chokomomo-990"


class FanzaApi(object):

    @staticmethod
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

    @staticmethod
    def get_item_list(keyword):
        """
        :type keyword: str
        :rtype: Response
        """
        return requests.get("https://api.dmm.com/affiliate/v3/ItemList", params={
            "api_id": api_id,
            "affiliate_id": affiliate_id,
            "site": "FANZA",
            "service": "digital",
            "floor": "videoa",
            "hits": "10",
            "sort": "date",
            "keyword": FanzaApi.normalize(keyword),
            "output": "json"
        })

    @staticmethod
    def get_product_description(url):
        """
        :type url: str
        :rtype: str
        """
        return pq(url)(".mg-b20.lh4").text().rstrip()
