from unittest import TestCase

import service_1pondo_api


class Test(TestCase):
    
    def test_get_by_id(self):
        service_1pondo_api.get_by_id("a")
