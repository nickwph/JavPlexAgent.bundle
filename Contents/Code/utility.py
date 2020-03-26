import io
import os
import re
import struct
from skimage import io as io2
from skimage.transform import resize

import numpy
import requests


def extract_part_number_from_filename(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    match = re.match(".*?Part(\d+)", filename_without_ext, re.IGNORECASE)
    if match: return int(match.group(1))
    return None


def extract_filename_without_ext_and_part_number(filename):
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    return re.sub(r"-Part\d+$", "", filename_without_ext, 0, re.IGNORECASE)


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
        hash_1 = calculate_average_hash(url_1)
        hash_2 = calculate_average_hash(url_2)
        return hash_1.diff(hash_2) < 5
    return False


def calculate_average_hash(image_url, hash_size=8):
    """
    Re-implemented average hash from imagehash using pure python.

    https://github.com/JohannesBuchner/imagehash/blob/master/imagehash/__init__.py#L126

    :param str image_url:
    :param int hash_size:
    :return:
    """
    image = io2.imread(image_url, as_gray=True)
    resized = resize(image, (hash_size, hash_size), anti_aliasing=True)
    pixels = numpy.asarray(resized)
    avg = pixels.mean()
    diff = pixels > avg
    return ImageHash(diff)


def binary_array_to_hex(arr):
    """
    internal function to make a hex string out of a binary array.
    """
    bit_string = ''.join(str(b) for b in 1 * arr.flatten())
    width = int(numpy.ceil(len(bit_string) / 4))
    return '{:0>{width}x}'.format(int(bit_string, 2), width=width)


class ImageHash(object):
    """
    Hash encapsulation. Can be used for dictionary keys and comparisons.
    """

    def __init__(self, binary_array):
        self.hash = binary_array

    def diff(self, other):
        if other is None:
            raise TypeError('Other hash must not be None.')
        if self.hash.size != other.hash.size:
            raise TypeError('ImageHashes must be of the same shape.', self.hash.shape, other.hash.shape)
        return numpy.count_nonzero(self.hash.flatten() != other.hash.flatten())

    def __str__(self):
        return binary_array_to_hex(self.hash.flatten())

    def __repr__(self):
        return repr(self.hash)

    def __eq__(self, other):
        if other is None:
            return False
        return numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    def __ne__(self, other):
        if other is None:
            return False
        return not numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    # def __hash__(self):
    #     # this returns a 8 bit integer, intentionally shortening the information
    #     return sum([2 ** (i % 8) for i, v in enumerate(self.hash.flatten()) if v])
