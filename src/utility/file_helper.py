import os
import re


def extract_part_number_from_filename(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    match = re.match(".*?Part(\d+)", filename_without_ext, re.IGNORECASE)  # noqa: W605
    if match:
        return int(match.group(1))
    return None


def extract_filename_without_ext_and_part_number(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    return re.sub(r"-Part\d+$", "", filename_without_ext, 0, re.IGNORECASE)


def extract_product_id_and_part_number(filename):
    """
    :type filename: str
    :rtype: (str, int)
    """
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    match = re.match("(.*?)-Part(\d+)$", filename_without_ext, re.IGNORECASE)  # noqa: W605
    if match: return match.group(1), int(match.group(2))  # noqa
    match = re.match("(.*?)-([a-zA-Z])$", filename_without_ext, re.IGNORECASE)  # noqa: W605
    if match: return match.group(1), ord(match.group(2).lower()) - 96  # noqa
    return filename_without_ext, None
