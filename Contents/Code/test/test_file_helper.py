from unittest import TestCase

import image_helper


class Test(TestCase):

    def test_extract_part_number_from_filename(self):
        self.assertEqual(1, image_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(32, image_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(32, image_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part534"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("/aaaaa/Part534"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("/aaaaa/-Part534"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("/aaaaa/part534"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("/aaaaa/-part534"))
        self.assertEqual(534, image_helper.extract_part_number_from_filename("asd-part534"))
        self.assertEqual(None, image_helper.extract_part_number_from_filename("/aaaaa/aaaa"))

    def test_extract_filename_without_ext_and_part_number(self):
        self.assertEqual("", image_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534"))
        self.assertEqual("asdfasdf", image_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual("adasfadfpart534",
                         image_helper.extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual("", image_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual("asdfasdf",
                         image_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual("adasfadfpart534",
                         image_helper.extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual("aaa", image_helper.extract_filename_without_ext_and_part_number("/aaa-part534.mp4"))
        self.assertEqual("aaaa", image_helper.extract_filename_without_ext_and_part_number("/aaaa-part534"))
        self.assertEqual("aaaaapart534", image_helper.extract_filename_without_ext_and_part_number("/aaaaapart534"))

    def test_extract_product_id_and_part_number(self):
        self.assertEqual(("aaaa", 1), image_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(("aaaa", 32), image_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(("aaaa", 32), image_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32"))
        self.assertEqual(("aaaa", 534), image_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part534"))
        self.assertEqual(("Part534", None), image_helper.extract_product_id_and_part_number("/aaaaa/Part534"))
        self.assertEqual(("", 534), image_helper.extract_product_id_and_part_number("/aaaaa/-Part534"))
        self.assertEqual(("part534", None), image_helper.extract_product_id_and_part_number("/aaaaa/part534"))
        self.assertEqual(("", 534), image_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(("asd", 534), image_helper.extract_product_id_and_part_number("asd-part534"))
        self.assertEqual(("aaaa", None), image_helper.extract_product_id_and_part_number("/aaaaa/aaaa"))
        self.assertEqual(('', 534), image_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(('asdfasdf', 534), image_helper.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual(('adasfadfpart534', None),
                         image_helper.extract_product_id_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual(('', 534), image_helper.extract_product_id_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual(('asdfasdf', 534), image_helper.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual(('adasfadfpart534', None),
                         image_helper.extract_product_id_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual(('aaa', 534), image_helper.extract_product_id_and_part_number("/aaa-part534.mp4"))
        self.assertEqual(('aaaa', 534), image_helper.extract_product_id_and_part_number("/aaaa-part534"))
        self.assertEqual(('aaaaapart534', None), image_helper.extract_product_id_and_part_number("/aaaaapart534"))
