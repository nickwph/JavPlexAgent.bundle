from unittest import TestCase

from mock import patch

import environments
from framework.plex_agent import ObjectContainer


class Test(TestCase):

    def setUp(self):
        environments.is_local_debugging = True  # this is needed

    def test_search(self):
        import caribbeancom_searcher
        results = ObjectContainer()
        caribbeancom_searcher.search(results, "some_product_id")
        self.assertEqual(0, len(results))

    @patch('caribbeancom_searcher.caribbeancom_api')
    def test_search___when_product_id_does_not_work(self, mock_caribbeancom_api):
        """
        :type mock_caribbeancom_api:  caribbeancom_api
        """
        mock_caribbeancom_api.extract_id.return_value = None
        import caribbeancom_searcher
        results = ObjectContainer()
        caribbeancom_searcher.search(results, "some_product_id")
        self.assertEqual(0, len(results))

    @patch('caribbeancom_searcher.caribbeancom_api')
    def test_search___when_product_id_works_but_no_search_results(self, mock_caribbeancom_api):
        """
        :type mock_caribbeancom_api:  caribbeancom_api
        """
        mock_caribbeancom_api.extract_id.return_value = "is_good_product_id"
        import caribbeancom_searcher
        results = ObjectContainer()
        caribbeancom_searcher.search(results, "some_product_id")
        self.assertEqual(1, len(results))
