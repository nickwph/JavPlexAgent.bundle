from unittest import TestCase

from api_fanza import FanzaApi


class TestFanzaApi(TestCase):

    def test_normalize(self):
        self.assertEqual("ssni00558", FanzaApi.normalize("SSNI-558"))

    def test_get_item_list(self):
        body = FanzaApi.get_item_list("SSNI-558")
        self.assertEqual(200, body.result.status, 200)
        self.assertEqual(1, body.result.total_count, 1)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable

    def test_get_product_description(self):
        description = FanzaApi.get_product_description("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00558/")
        self.assertEqual(193, len(description))  # too hard to check the whole string
