import io
import struct
import urllib2

import numpy
from PIL import Image
from cStringIO import StringIO
import binascii
import requests
from PIL.Image import ANTIALIAS

import environments

if environments.is_local_debugging:
    from framework.plex_log import Log

try:
    import PIL
    import imagehash
except ImportError:
    Log.Error("Numpy and PIL are not available")
    PIL, imagehash = None, None

can_analyze_images = PIL is not None and imagehash is not None


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
    if can_analyze_images:
        type_1, width_1, height_1 = get_image_info_from_url(url_1)
        type_2, width_2, height_2 = get_image_info_from_url(url_2)
        is_horizontal_1 = (width_1 - height_1) > 0
        is_horizontal_2 = (width_2 - height_2) > 0
        if is_horizontal_1 == is_horizontal_2:
            # response = requests.get(url_1, stream=True)
            # response.raw.decode_content = True
            # image = Image.frombytes(response.raw)
            # r = requests.get(url_1, stream=True)
            # img = Image.open(r.raw)
            # data_1 = urllib2.urlopen(url_1).read()
            # raw_1 = binascii.unhexlify(data_1)
            # stream = io.BytesIO(raw_1)
            # img = Image.open(urllib2.urlopen(url_1))
            # image_1 = Image.frombytes('RGB', (width_1, height_1), data_1.encode(), 'raw')
            image_1 = PIL.Image.open(io.BytesIO(requests.get(url_1).content))
            image_2 = PIL.Image.open(io.BytesIO(requests.get(url_2).content))
            resized = image_1.resize((800,800), ANTIALIAS)
            pixels = numpy.asarray(resized)
            avg = pixels.mean()
            diff = pixels > avg
            return imagehash.ImageHash(diff)
            # hash_1 = imagehash.average_hash(image_1)
            # hash_2 = imagehash.average_hash(image_2)
            # return hash_1 - hash_2 < 587
            return False
        else:
            return False
    return False
