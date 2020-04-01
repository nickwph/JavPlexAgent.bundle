from unittest import TestCase

from framework.framework_agent import ObjectContainer

import caribbeancom_searcher


class Test(TestCase):

    def test_search(self):
        results = ObjectContainer()
        caribbeancom_searcher.search(results, "iuh3r2af3")
