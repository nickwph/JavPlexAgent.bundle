from unittest import TestCase

from api_fanza import FanzaApi


class TestFanzaApi(TestCase):

    def test_normalize(self):
        self.assertEqual(FanzaApi.normalize("SSNI-558"), "ssni00558")

    def test_get_item_list(self):
        body = FanzaApi.get_item_list("SSNI-558")
        self.assertEqual(body.result.status, 200)
        self.assertEqual(body.result.total_count, 1)
        self.assertEqual(body.result['items'][0].content_id, "ssni00558")  # items is a reserved variable

    def test_get_product_description(self):
        description = FanzaApi.get_product_description("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00558/")
        self.assertEqual(len(description), 193)  # too hard to check the whole string
