import io
import struct
from io import BytesIO

import requests

import environments

if environments.is_local_debugging:
    from framework.plex_log import Log

try:
    # noinspection PyUnresolvedReferences
    from PIL import Image
    # noinspection PyUnresolvedReferences
    from imagehash import average_hash

    average_hash_check_enabled = True
except ImportError:
    Log.Error("Numpy and PIL are not available")
    average_hash_check_enabled = False


def get_image_info_from_url(image_url):
    """
    Found this solution from https://stackoverflow.com/a/30685578

    :param image_url:
    :return:
    """
    request = requests.get(image_url, headers={"Range": "bytes=0-166"})  # might need to adjust this
    return get_image_info(request.content)


def get_image_info(data):
    """
    Found this solution from https://stackoverflow.com/a/30685578

    :param data:
    :return:
    """
    data = data
    size = len(data)
    # print(size)
    height = -1
    width = -1
    content_type = ''

    # handle GIFs
    if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack(b"<HH", data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n')
          and (data[12:16] == b'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        jpeg = io.BytesIO(data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):
                while (ord(b) != 0xFF): b = jpeg.read(1)
                while (ord(b) == 0xFF): b = jpeg.read(1)
                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(b">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(b">H", jpeg.read(2))[0]) - 2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            pass
        except ValueError:
            pass

    return content_type, width, height


def are_similar(url_1, url_2):
    type_1, width_1, height_1 = get_image_info_from_url(url_1)
    type_2, width_2, height_2 = get_image_info_from_url(url_2)
    is_horizontal_1 = (width_1 - height_1) > 0
    is_horizontal_2 = (width_2 - height_2) > 0
    if is_horizontal_1 == is_horizontal_2:
        if average_hash_check_enabled:
            image_1 = Image.open(BytesIO(requests.get(url_1).content))
            image_2 = Image.open(BytesIO(requests.get(url_2).content))
            hash_1 = average_hash(image_1)
            hash_2 = average_hash(image_2)
            return hash_1 - hash_2 < 5
        else:
            return False
    return False