from unittest import TestCase

import environments
from framework.plex_agent import ObjectContainer


class Test(TestCase):

    def setUp(self):
        environments.is_local_debugging = True  # this is needed

    def test_search___actual_run(self):
        import fanza_searcher
        results = ObjectContainer()
        fanza_searcher.search(results, "SSNI-558")
        self.assertEqual(2, len(results))
