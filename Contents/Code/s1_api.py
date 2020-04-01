import requests

base_url = "https://www.s1s1s1.com"
maker_id = 3152


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
