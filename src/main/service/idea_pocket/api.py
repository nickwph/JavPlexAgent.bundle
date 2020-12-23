import requests

base_url = "https://www.ideapocket.com"
maker_id = 1219


def convert_product_id_from_digital_to_dvd(product_id):
    """
    :type product_id: str
    :rtype: str
    """
    product_id = product_id.lower()
    product_id = product_id.strip()
    product_id = product_id.replace("00", "", 1)
    product_id = product_id.replace("13dsvr", "dsvr", 1)
    product_id = product_id.replace("13dsvr", "313dsvr", 1)
    product_id = product_id.replace("h_1158avopvr", "avopvr", 1)
    product_id = product_id.replace("84kmvr", "kmvr", 1)
    product_id = product_id.replace("h_1285bikmvr", "bi84kmvr", 1)
    product_id = product_id.replace("84bzvr", "bzvr", 1)
    product_id = product_id.replace("h_1155crvr", "crvr", 1)
    product_id = product_id.replace("84exvr", "exvr", 1)
    product_id = product_id.replace("84vvvr", "vvvr", 1)
    product_id = product_id.replace("24dtvr", "dtvr", 1)
    product_id = product_id.replace("h_565scvr", "scvr", 1)
    product_id = product_id.replace("2wpvr", "wpvr", 1)
    product_id = product_id.replace("h_1282mxvr", "mxvr", 1)
    product_id = product_id.replace("55tmavr", "tmavr", 1)
    product_id = product_id.replace("h_1127vovs", "vovs", 1)
    product_id = product_id.replace("h_1116cafr", "cafr", 1)
    product_id = product_id.replace("h_1256tpvr", "tpvr", 1)
    return product_id


def is_valid_actress(actress_id):
    """
    :type actress_id: int
    :rtype: bool
    """
    url = "{}/actress/detail/{}/".format(base_url, actress_id)
    return requests.head(url).status_code == 200


def get_actress_image(actress_id):
    """
    :type actress_id: int
    :rtype: str
    """
    if is_valid_actress(actress_id):
        return "{}/contents/actress/{}/{}.jpg".format(base_url, actress_id, actress_id)
    else:
        return None


def is_valid_product(product_id):
    """
    :type product_id: str
    :rtype: bool
    """
    url = "{}/works/detail/{}/".format(base_url, product_id)
    return requests.head(url).status_code == 200


def get_product_image(product_id):
    """
    :type product_id: str
    :rtype: str
    """
    if is_valid_product(product_id):
        return "{}/contents/works/{}/{}-ps.jpg".format(base_url, product_id, product_id)
    else:
        return None
