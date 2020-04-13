from unittest import TestCase

import knights_visual_api


class Test(TestCase):

    def test_search(self):
        results = knights_visual_api.search("KV-094")
        self.assertEqual(1, len(results))

    def test_get_by_id(self):
        item = knights_visual_api.get_by_id("KV-094")
        self.assertEqual("KV-094", item.id)
