from unittest import TestCase

import s1_api


class Test(TestCase):

    def test_convert_product_id_from_digital_to_dvd_1(self):
        self.assertEqual('sivr001', s1_api.convert_product_id_from_digital_to_dvd('sivr00001'))
        self.assertEqual('sivr067', s1_api.convert_product_id_from_digital_to_dvd('sivr00067'))

    def test_is_valid_actress_1(self):
        result = s1_api.is_valid_actress(1030262)
        self.assertEqual(True, result)

    def test_is_valid_actress_2(self):
        result = s1_api.is_valid_actress(1030222)
        self.assertEqual(False, result)

    def test_get_actress_image_1(self):
        result = s1_api.get_actress_image(1030262)
        self.assertEqual("https://www.s1s1s1.com/contents/actress/1030262/1030262.jpg", result)

    def test_get_actress_image_2(self):
        result = s1_api.get_actress_image(1030222)
        self.assertEqual(None, result)

    def test_is_valid_product_1(self):
        result = s1_api.is_valid_product("sivr002")
        self.assertEqual(True, result)

    def test_is_valid_product_2(self):
        result = s1_api.is_valid_product("sivr2002")
        self.assertEqual(False, result)

    def test_get_product_image_1(self):
        result = s1_api.get_product_image("sivr002")
        self.assertEqual("https://www.s1s1s1.com/contents/works/sivr002/sivr002-ps.jpg", result)

    def test_get_product_image_2(self):
        result = s1_api.get_product_image("sivr2002")
        self.assertEqual(None, result)
