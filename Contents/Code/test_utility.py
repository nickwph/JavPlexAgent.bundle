from unittest import TestCase

from utility import extract_part_number_from_filename, extract_filename_without_ext_and_part_number


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
