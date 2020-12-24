import io
import struct

import requests

from plex.log import Log

try:
    from PIL import Image
    from imagehash import average_hash
    Log.Info("Numpy and PIL are working")
except ImportError as error:
    Log.Info("Numpy and PIL are not available")
    Log.Info(error)
    Image, average_hash = None, None

can_analyze_images = Image is not None and average_hash is not None


def add_padding_to_image_as_poster(image_url, background_color=(0, 0, 0)):
    """
    :type image_url: str
    :rtype: Image.Image
    """
    image_data = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_data))  # type: Image.Image
    width, height = image.size
    if float(height) / width == 1.5:
        return image
    elif float(height) / width < 1.5:
        expected_height = int(float(width) * 1.5)
        result = Image.new(image.mode, (width, expected_height), background_color)
        result.paste(image, (0, (expected_height - height) // 2))
        return result
    else:
        expected_width = int(float(height) // 1.5)
        result = Image.new(image.mode, (expected_width, height), background_color)
        result.paste(image, ((expected_width - width) // 2, 0))
        return result


def crop_square_from_top_left(image_url):
    """
    :type image_url: str
    :rtype: Image.Image
    """
    image_data = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_data))  # type: Image.Image
    width, height = image.size
    if height == width:
        return image
    elif height > width:
        result = Image.new(image.mode, (width, width), (0, 0, 0))
        result.paste(image, (0, 0))
        return result
    else:
        expected_width = int(float(height) // 1.5)
        result = Image.new(image.mode, (height, height), (0, 0, 0))
        result.paste(image, 0, 0)
        return result


def does_image_exist(image_url):
    """
    :type image_url: str
    :rtype: bool
    """
    return get_image_info_from_url(image_url) != ('', -1, -1)


def get_image_info_from_url(image_url):
    """
    Found this solution from https://stackoverflow.com/a/30685578
    :type image_url: str
    :rtype: (str, int, int)
    """
    request = requests.get(image_url, headers={"Range": "bytes=0-166"})  # might need to adjust this
    return get_image_info(request.content)


def get_image_info(data):  # noqa: C901
    """
    Found this solution from https://stackoverflow.com/a/30685578
    :type data: str
    :rtype: (str, int, int)
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
            w = -1
            h = -1
            while b and ord(b) != 0xDA:
                while ord(b) != 0xFF:
                    b = jpeg.read(1)
                while ord(b) == 0xFF:
                    b = jpeg.read(1)
                if 0xC0 <= ord(b) <= 0xC3:
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
            image_1 = Image.open(io.BytesIO(requests.get(url_1).content))
            image_2 = Image.open(io.BytesIO(requests.get(url_2).content))
            return images_are_similar(image_1, image_2)
    return False


def crop_poster_data_from_cover_if_similar_to_small_poster(cover_url, small_poster_url):
    if can_analyze_images:
        poster = crop_poster_from_cover(cover_url)
        poster_to_check = Image.open(io.BytesIO(requests.get(small_poster_url).content))
        if images_are_similar(poster, poster_to_check):
            return convert_image_to_data(poster)
    return None


def convert_image_to_data(image):
    bytes_io = io.BytesIO()
    image.save(bytes_io, format='jpeg')
    return bytes_io.getvalue()


def images_are_similar(image_1, image_2):
    hash_1 = average_hash(image_1)
    hash_2 = average_hash(image_2)
    return hash_1 - hash_2 <= 8


def crop_poster_from_cover(cover_url):
    """
    :type cover_url: str
    :rtype: Image.Image
    """
    cover_image_data = requests.get(cover_url).content
    cover_image = Image.open(io.BytesIO(cover_image_data))  # type: Image.Image
    (cover_content_type, cover_width, cover_height) = get_image_info(cover_image_data)
    default_poster_height = 538.0
    default_poster_width = 379.0
    poster_height = cover_height
    poster_width = default_poster_width / default_poster_height * cover_height
    poster_left = int(cover_width - poster_width)
    poster_upper = 0
    poster_right = int(cover_width)
    poster_lower = int(poster_height)
    poster_image = cover_image.crop((poster_left, poster_upper, poster_right, poster_lower))
    return poster_image
