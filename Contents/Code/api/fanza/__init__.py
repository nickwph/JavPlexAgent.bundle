import requests


def normalise(keyword):
    """
    :type keyword: str
    :return str: str
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
    print keyword
    return keyword
