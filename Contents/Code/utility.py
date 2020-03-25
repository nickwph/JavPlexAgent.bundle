import os
import re

import requests
from PIL import Image
from io import BytesIO


def extract_part_number_from_filename(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    match = re.match(".*?Part(\d+)", filename_without_ext, re.IGNORECASE)
    if match: return int(match.group(1))
    return None


def extract_filename_without_ext_and_part_number(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    return re.sub(r"-Part\d+$", "", filename_without_ext, 0, re.IGNORECASE)


def get_image_dimension(image_url):
    request = requests.get(image_url)
    image = Image.open(BytesIO(request.content))
    width, height = image.size
    print(width, height)
    return image.size
