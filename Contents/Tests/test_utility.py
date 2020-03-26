from unittest import TestCase

from utility import extract_part_number_from_filename, extract_filename_without_ext_and_part_number, \
    get_image_info_from_url


class Test(TestCase):

    def test_extract_part_number_from_filename(self):
        self.assertEqual(1, extract_part_number_from_filename("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(32, extract_part_number_from_filename("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(32, extract_part_number_from_filename("/aaaaa/aaaa-Part32"))
        self.assertEqual(534, extract_part_number_from_filename("/aaaaa/aaaa-Part534"))
        self.assertEqual(534, extract_part_number_from_filename("/aaaaa/Part534"))
        self.assertEqual(534, extract_part_number_from_filename("/aaaaa/-Part534"))
        self.assertEqual(534, extract_part_number_from_filename("/aaaaa/part534"))
        self.assertEqual(534, extract_part_number_from_filename("/aaaaa/-part534"))
        self.assertEqual(534, extract_part_number_from_filename("asd-part534"))
        self.assertEqual(None, extract_part_number_from_filename("/aaaaa/aaaa"))

    def test_extract_filename_without_ext_and_part_number(self):
        self.assertEqual("", extract_filename_without_ext_and_part_number("/aaaaa/-part534"))
        self.assertEqual("asdfasdf", extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual("adasfadfpart534", extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual("", extract_filename_without_ext_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual("asdfasdf", extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual("adasfadfpart534", extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual("aaa", extract_filename_without_ext_and_part_number("/aaa-part534.mp4"))
        self.assertEqual("aaaa", extract_filename_without_ext_and_part_number("/aaaa-part534"))
        self.assertEqual("aaaaapart534", extract_filename_without_ext_and_part_number("/aaaaapart534"))

    def test_get_image_info_from_url(self):
        self.assertEqual(('image/jpeg', 1280, 860), get_image_info_from_url(
            "https://www.manulife.com.hk/content/dam/insurance/hk/images/home/mlf_trio_homepage_banner_1920x1290.jpg"
            "/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg"))
        self.assertEqual(('image/png', 48, 48), get_image_info_from_url(
            "https://storage.googleapis.com/google-code-archive/v2/code.google.com/bfg-pages/logo.png"))
        self.assertEqual(('image/png', 110, 30), get_image_info_from_url(
            "https://www.guru99.com/images/logo/logo_v1.png"))
