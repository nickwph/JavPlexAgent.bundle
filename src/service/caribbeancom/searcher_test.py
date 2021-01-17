# coding=utf-8
from unittest import TestCase

from plex.agent import MetadataSearchResult
from plex.container import ObjectContainer
from service.caribbeancom import searcher
from utility import mixpanel_helper


class Test(TestCase):

    def setUp(self):
        mixpanel_helper.initialize('test', True)

    def test_search___actual_run(self):

        results = ObjectContainer()
        searcher.search(results, 1, "Carib-070116-197")
        self.assertEqual(1, len(results))

        result = results[0]  # type: MetadataSearchResult
        self.assertEqual(u"carib-070116-197@1", result.id)
        self.assertEqual(u"070116-197 洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜", result.name)
        self.assertEqual(u"https://smovie.caribbeancom.com/moviepages/070116-197/images/jacket.jpg", result.thumb)
        self.assertEqual(u"ja", result.lang)
        self.assertEqual(2016, result.year)
        self.assertEqual(100, result.score)

    def test_search___actual_run_with_bad_product_id(self):
        results = ObjectContainer()
        searcher.search(results, 1, "bad_one")
        self.assertEqual(0, len(results))
