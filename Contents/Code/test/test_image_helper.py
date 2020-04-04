from unittest import TestCase

from .. import image_helper


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
