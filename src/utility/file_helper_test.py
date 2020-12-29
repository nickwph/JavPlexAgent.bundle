from unittest import TestCase

from utility import file_helper


class Test(TestCase):

    def test_extract_part_number_from_filename(self):
        self.assertEqual(1, file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(32, file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(32, file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part32"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("/aaaaa/aaaa-Part534"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("/aaaaa/Part534"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("/aaaaa/-Part534"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("/aaaaa/part534"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("/aaaaa/-part534"))
        self.assertEqual(534, file_helper.extract_part_number_from_filename("asd-part534"))
        self.assertEqual(None, file_helper.extract_part_number_from_filename("/aaaaa/aaaa"))

    def test_extract_filename_without_ext_and_part_number(self):
        self.assertEqual("", file_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534"))
        self.assertEqual("assdf", file_helper.extract_filename_without_ext_and_part_number("/aaa/assdf-part534"))
        self.assertEqual("adffpart534", file_helper.extract_filename_without_ext_and_part_number("/aaaa/adffpart534"))
        self.assertEqual("", file_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual("asdsdf", file_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdsdf-part54.mp4"))
        self.assertEqual("dafpart534", file_helper.extract_filename_without_ext_and_part_number("/aaa/dafpart534.mp4"))
        self.assertEqual("aaa", file_helper.extract_filename_without_ext_and_part_number("/aaa-part534.mp4"))
        self.assertEqual("aaaa", file_helper.extract_filename_without_ext_and_part_number("/aaaa-part534"))
        self.assertEqual("aaaaapart534", file_helper.extract_filename_without_ext_and_part_number("/aaaaapart534"))

    def test_extract_product_id_and_part_number(self):
        self.assertEqual(("aaaa", 1), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(("aaaa", 32), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(("s-cute", 1), file_helper.extract_product_id_and_part_number("/aaaaa/s-cute-Part1.mp4"))
        self.assertEqual(("s-cute-123_ewr_02", None), file_helper.extract_product_id_and_part_number("/aaaaa/s-cute-123_ewr_02.mp4"))
        self.assertEqual(("s-cute-123_ewr_02", 1), file_helper.extract_product_id_and_part_number("/aaaaa/s-cute-123_ewr_02-A.mp4"))
        self.assertEqual(("KV-096", 32), file_helper.extract_product_id_and_part_number("/aaaaa/KV-096-Part32.mp4"))
        self.assertEqual(("KV-096", None), file_helper.extract_product_id_and_part_number("/aaaaa/KV-096.mp4"))
        self.assertEqual(("aaaa", 32), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32"))
        self.assertEqual(("aaaa", 534), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part534"))
        self.assertEqual(("Part534", None), file_helper.extract_product_id_and_part_number("/aaaaa/Part534"))
        self.assertEqual(("", 534), file_helper.extract_product_id_and_part_number("/aaaaa/-Part534"))
        self.assertEqual(("part534", None), file_helper.extract_product_id_and_part_number("/aaaaa/part534"))
        self.assertEqual(("", 534), file_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(("asd", 534), file_helper.extract_product_id_and_part_number("asd-part534"))
        self.assertEqual(("aaaa", None), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa"))
        self.assertEqual(('', 534), file_helper.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(('asdfasdf', 534), file_helper.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual(('aspart534', None), file_helper.extract_product_id_and_part_number("/aaa/aspart534"))
        self.assertEqual(('', 534), file_helper.extract_product_id_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual(('asdfdf', 534), file_helper.extract_product_id_and_part_number("/aaaaa/asdfdf-part534.mp4"))
        self.assertEqual(('abfrt534', 1), file_helper.extract_product_id_and_part_number("/a/abfrt534-A.mp4"))
        self.assertEqual(('aaa', 2), file_helper.extract_product_id_and_part_number("/aaa-B.mp4"))
        self.assertEqual(('aaaa', 4), file_helper.extract_product_id_and_part_number("/aaaa-D"))
        self.assertEqual(('aaaa', 4), file_helper.extract_product_id_and_part_number("/aaaa-d"))
        self.assertEqual(('aaaaapart534', 7), file_helper.extract_product_id_and_part_number("/aaaaapart534-G"))
