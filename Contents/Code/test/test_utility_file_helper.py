from unittest import TestCase

import utility_file_helper


class Test(TestCase):

    def test_extract_part_number_from_filename(self):
        self.assertEqual(1, utility_file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(32, utility_file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(32, utility_file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part534"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("/aaaaa/Part534"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("/aaaaa/-Part534"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("/aaaaa/part534"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("/aaaaa/-part534"))
        self.assertEqual(534, utility_file_helper.extract_part_number_from_filename("asd-part534"))
        self.assertEqual(None, utility_file_helper.extract_part_number_from_filename("/aaaaa/aaaa"))

    def test_extract_filename_without_ext_and_part_number(self):
        self.assertEqual("", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534"))
        self.assertEqual("assdf", utility_file_helper.extract_filename_without_ext_and_part_number("/aaa/assdf-part534"))
        self.assertEqual("adffpart534", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaa/adffpart534"))
        self.assertEqual("", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual("asdsdf", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdsdf-part54.mp4"))
        self.assertEqual("dafpart534", utility_file_helper.extract_filename_without_ext_and_part_number("/aaa/dafpart534.mp4"))
        self.assertEqual("aaa", utility_file_helper.extract_filename_without_ext_and_part_number("/aaa-part534.mp4"))
        self.assertEqual("aaaa", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaa-part534"))
        self.assertEqual("aaaaapart534", utility_file_helper.extract_filename_without_ext_and_part_number("/aaaaapart534"))

    def test_extract_product_id_and_part_number(self):
        self.assertEqual(("aaaa", 1), utility_file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(("aaaa", 32), utility_file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(("aaaa", 32), utility_file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32"))
        self.assertEqual(("aaaa", 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part534"))
        self.assertEqual(("Part534", None), utility_file_helper.extract_product_id_and_part_number("/aaaaa/Part534"))
        self.assertEqual(("", 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/-Part534"))
        self.assertEqual(("part534", None), utility_file_helper.extract_product_id_and_part_number("/aaaaa/part534"))
        self.assertEqual(("", 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(("asd", 534), utility_file_helper.extract_product_id_and_part_number("asd-part534"))
        self.assertEqual(("aaaa", None), utility_file_helper.extract_product_id_and_part_number("/aaaaa/aaaa"))
        self.assertEqual(('', 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(('asdfasdf', 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual(('aspart534', None), utility_file_helper.extract_product_id_and_part_number("/aaa/aspart534"))
        self.assertEqual(('', 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual(('asdfdf', 534), utility_file_helper.extract_product_id_and_part_number("/aaaaa/asdfdf-part534.mp4"))
        self.assertEqual(('abfrt534', 1), utility_file_helper.extract_product_id_and_part_number("/a/abfrt534-A.mp4"))
        self.assertEqual(('aaa', 2), utility_file_helper.extract_product_id_and_part_number("/aaa-B.mp4"))
        self.assertEqual(('aaaa', 4), utility_file_helper.extract_product_id_and_part_number("/aaaa-D"))
        self.assertEqual(('aaaa', 4), utility_file_helper.extract_product_id_and_part_number("/aaaa-d"))
        self.assertEqual(('aaaaapart534', 7), utility_file_helper.extract_product_id_and_part_number("/aaaaapart534-G"))
