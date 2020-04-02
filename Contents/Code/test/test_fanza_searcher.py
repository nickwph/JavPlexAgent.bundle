from unittest import TestCase

import environments
from framework.plex_agent import ObjectContainer


class Test(TestCase):

    def setUp(self):
        environments.is_local_debugging = True  # this is needed

    def test_search___actual_run_without_part_number(self):
        import fanza_searcher
        results = ObjectContainer()
        fanza_searcher.search(results, None, "SSNI-558")
        self.assertEqual(2, len(results))

    def test_search___actual_run_with_part_number(self):
        import fanza_searcher
        results = ObjectContainer()
        fanza_searcher.search(results, 1, "SSNI-558")
        self.assertEqual(2, len(results))
