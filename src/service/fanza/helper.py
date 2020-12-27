import re


def convert_product_id_to_bongo(product_id):
    """
    :type product_id: str
    """
    # TODO: need to handle this: 3DSVR-0796
    bongo = product_id.upper()
    match = re.match("(H_)?(\d*)([a-zA-Z]+)(00)?(\d+)", bongo, re.IGNORECASE)  # noqa: W605
    if match:
        bongo = match.group(3) + "-" + match.group(5)
    return bongo
