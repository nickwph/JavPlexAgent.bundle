from unittest import TestCase

from api_fanza import FanzaApi


class TestFanzaApi(TestCase):

    def test_normalize(self):
        self.assertEqual("ssni00558", FanzaApi.normalize("SSNI-558"))

    def test_search_item_1(self):
        body = FanzaApi.search_item("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable

    def test_search_item_2(self):
        body = FanzaApi.search_item("SIVR-002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(2, body.result.total_count)
        self.assertEqual("h_1382tnsivr00002", body.result['items'][0].content_id)  # items is a reserved variable
        self.assertEqual("sivr00002", body.result['items'][1].content_id)  # items is a reserved variable

    def test_get_item_1(self):
        body = FanzaApi.get_item("SSNI-558")
        self.assertEqual(400, body.result.status)

    def test_get_item_2(self):
        body = FanzaApi.get_item("SIVR-002")
        self.assertEqual(400, body.result.status)

    def test_get_item_3(self):
        body = FanzaApi.get_item("ssni00558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable

    def test_get_item_4(self):
        body = FanzaApi.get_item("sivr00002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("sivr00002", body.result['items'][0].content_id)  # items is a reserved variable

    def test_get_product_description(self):
        description = FanzaApi.get_product_description("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00558/")
        self.assertEqual(193, len(description))  # too hard to check the whole string
