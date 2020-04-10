import io
from unittest import TestCase

import requests
from PIL import Image

import image_helper


# import PIL
# import requests

class Test(TestCase):

    def test_get_image_info_from_url(self):
        self.assertEqual(('image/jpeg', 1280, 860), image_helper.get_image_info_from_url(
            "https://www.manulife.com.hk/content/dam/insurance/hk/images/home/mlf_trio_homepage_banner_1920x1290.jpg"
            "/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg"))
        self.assertEqual(('image/png', 48, 48), image_helper.get_image_info_from_url(
            "https://storage.googleapis.com/google-code-archive/v2/code.google.com/bfg-pages/logo.png"))
        self.assertEqual(('image/png', 110, 30), image_helper.get_image_info_from_url(
            "https://www.guru99.com/images/logo/logo_v1.png"))

    def test_are_similar(self):
        self.assertEqual(True, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg"))
        self.assertEqual(True, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007jp-1.jpg"))
        self.assertEqual(False, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007jp-2.jpg"))
        self.assertEqual(False, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007jp-3.jpg"))
        self.assertEqual(False, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007jp-4.jpg"))
        self.assertEqual(False, image_helper.are_similar(
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg",
            "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007jp-5.jpg"))

    def test_crop_poster_from_cover(self):
        small_poster_url = "https://pics.dmm.co.jp/mono/movie/adult/soav062/soav062ps.jpg"
        cover_url = "https://pics.dmm.co.jp/mono/movie/adult/soav062/soav062pl.jpg"
        poster = image_helper.crop_poster_from_cover(cover_url)
        poster_to_check = Image.open(io.BytesIO(requests.get(small_poster_url).content))
        self.assertEqual(True, image_helper.images_are_similar(poster, poster_to_check))

    def test_crop_poster_from_cover_2(self):
        small_poster_url = "https://pics.dmm.co.jp/mono/movie/adult/ssni558/ssni558ps.jpg"
        cover_url = "https://pics.dmm.co.jp/mono/movie/adult/ssni558/ssni558pl.jpg"
        poster = image_helper.crop_poster_from_cover(cover_url)
        poster_to_check = Image.open(io.BytesIO(requests.get(small_poster_url).content))
        self.assertEqual(True, image_helper.images_are_similar(poster, poster_to_check))

    def test_crop_poster_from_cover___cover_does_not_have_poster(self):
        small_poster_url = "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007ps.jpg"
        cover_url = "https://pics.dmm.co.jp/digital/video/hnvr00007/hnvr00007pl.jpg"
        poster = image_helper.crop_poster_from_cover(cover_url)
        poster_to_check = Image.open(io.BytesIO(requests.get(small_poster_url).content))
        self.assertEqual(False, image_helper.images_are_similar(poster, poster_to_check))
