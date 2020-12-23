import re


def convert_product_id_to_bongo(product_id):
    """
    :type product_id: str
    """
    bongo = product_id.upper()
    match = re.match("(H_)?(\d*)([a-zA-Z]+)(00)?(\d+)", bongo, re.IGNORECASE)  # noqa: W605
    if match:
        bongo = match.group(3) + "-" + match.group(5)
    return bongo
