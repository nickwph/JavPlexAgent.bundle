from unittest import TestCase

import helpers


class Test(TestCase):

    def test_extract_product_id_and_part_number(self):
        self.assertEqual(("aaaa", 1), helpers.extract_product_id_and_part_number("/aaaaa/aaaa-Part1.mp4"))
        self.assertEqual(("aaaa", 32), helpers.extract_product_id_and_part_number("/aaaaa/aaaa-Part32.mp4"))
        self.assertEqual(("aaaa", 32), helpers.extract_product_id_and_part_number("/aaaaa/aaaa-Part32"))
        self.assertEqual(("aaaa", 534), helpers.extract_product_id_and_part_number("/aaaaa/aaaa-Part534"))
        self.assertEqual(("Part534", None), helpers.extract_product_id_and_part_number("/aaaaa/Part534"))
        self.assertEqual(("", 534), helpers.extract_product_id_and_part_number("/aaaaa/-Part534"))
        self.assertEqual(("part534", None), helpers.extract_product_id_and_part_number("/aaaaa/part534"))
        self.assertEqual(("", 534), helpers.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(("asd", 534), helpers.extract_product_id_and_part_number("asd-part534"))
        self.assertEqual(("aaaa", None), helpers.extract_product_id_and_part_number("/aaaaa/aaaa"))
        self.assertEqual(('', 534), helpers.extract_product_id_and_part_number("/aaaaa/-part534"))
        self.assertEqual(('asdfasdf', 534), helpers.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534"))
        self.assertEqual(('adasfadfpart534', None), helpers.extract_product_id_and_part_number("/aaaaa/adasfadfpart534"))
        self.assertEqual(('', 534), helpers.extract_product_id_and_part_number("/aaaaa/-part534.mp4"))
        self.assertEqual(('asdfasdf', 534), helpers.extract_product_id_and_part_number("/aaaaa/asdfasdf-part534.mp4"))
        self.assertEqual(('adasfadfpart534', None), helpers.extract_product_id_and_part_number("/aaaaa/adasfadfpart534.mp4"))
        self.assertEqual(('aaa', 534), helpers.extract_product_id_and_part_number("/aaa-part534.mp4"))
        self.assertEqual(('aaaa', 534), helpers.extract_product_id_and_part_number("/aaaa-part534"))
        self.assertEqual(('aaaaapart534', None), helpers.extract_product_id_and_part_number("/aaaaapart534"))
