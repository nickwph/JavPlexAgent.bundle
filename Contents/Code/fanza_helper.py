import re


def convert_product_id_to_bongo(product_id):
    """
    :type product_id: str
    """
    bongo = product_id.upper()
    # remove h_ prefix
    if bongo.startswith('H_'):
        bongo = bongo[len('H_'):]
    # normalize bongo
    match = re.match("(\d*)([a-zA-Z]+)(00)?(\d+)", bongo, re.IGNORECASE)  # noqa: W605
    if match:
        bongo = match.group(2) + match.group(4)
    return bongo