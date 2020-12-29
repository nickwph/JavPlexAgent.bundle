# coding=utf-8
from unittest import TestCase

from plex.agent import MetadataSearchResult
from plex.container import ObjectContainer
import searcher


class Test(TestCase):

    def test_extract_id(self):
        self.assertEqual("734_reona_01", searcher.extract_id("s-cute-734_reona_01"))
        self.assertEqual("123123-233", searcher.extract_id("S-CUTE-123123-233"))
        self.assertEqual(None, searcher.extract_id("SCUTEb-123123-1-FHD"))
        self.assertEqual(None, searcher.extract_id("SCUTEbeanc-123123-1-FHD"))

    def test_search(self):
        results = ObjectContainer()  # type: ObjectContainer[MetadataSearchResult]
        searcher.search(results, None, "s-cute-734_reona_01")
        self.assertEqual(1, len(results))
        self.assertEqual(u"ja", results[0].lang)
        self.assertEqual(u"http://static.s-cute.com/images/734_reona/734_reona_01/734_reona_01.jpg", results[0].thumb)
        self.assertEqual(100, results[0].score)
        self.assertEqual(2019, results[0].year)
        self.assertEqual(u"s-cute-734_reona_01", results[0].id)
        self.assertEqual(u"734_REONA_01 上品な仕草がエッチな美女とSEX／Reona", results[0].name)

    def test_search___no_result(self):
        results = ObjectContainer()  # type: ObjectContainer[MetadataSearchResult]
        searcher.search(results, None, "QQ-094")
        self.assertEqual(0, len(results))
