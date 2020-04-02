from unittest import TestCase

import file_helper


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
        self.assertEqual("asdfasdf", file_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual("adasfadfpart534",
                         file_helper.extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual("", file_helper.extract_filename_without_ext_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual("asdfasdf",
                         file_helper.extract_filename_without_ext_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual("adasfadfpart534",
                         file_helper.extract_filename_without_ext_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual("aaa", file_helper.extract_filename_without_ext_and_part_number("/aaa-part534.mp4"))
        self.assertEqual("aaaa", file_helper.extract_filename_without_ext_and_part_number("/aaaa-part534"))
        self.assertEqual("aaaaapart534", file_helper.extract_filename_without_ext_and_part_number("/aaaaapart534"))

    def test_extract_product_id_and_part_number(self):
        self.assertEqual(("aaaa", 1), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(("aaaa", 32), file_helper.extract_product_id_and_part_number("/aaaaa/aaaa-Part32.mp4"))
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
        self.assertEqual(('adasfadfpart534', None),
                         file_helper.extract_product_id_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual(('', 534), file_helper.extract_product_id_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual(('asdfasdf', 534), file_helper.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual(('adasfadfpart534', None),
                         file_helper.extract_product_id_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual(('aaa', 534), file_helper.extract_product_id_and_part_number("/aaa-part534.mp4"))
        self.assertEqual(('aaaa', 534), file_helper.extract_product_id_and_part_number("/aaaa-part534"))
        self.assertEqual(('aaaaapart534', None), file_helper.extract_product_id_and_part_number("/aaaaapart534"))
