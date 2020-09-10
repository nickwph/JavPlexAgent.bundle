# coding=utf-8
from unittest import TestCase

from typing import Any

import environments
import service_knightsvisual_searcher
from framework.plex_agent import MetadataSearchResult
from framework.plex_container import ObjectContainer

environments.is_local_debugging = True  # this is needed
reload(service_knightsvisual_searcher)


class Test(TestCase):

    def test_search(self):
        results = ObjectContainer()  # type: ObjectContainer[MetadataSearchResult]
        service_knightsvisual_searcher.search(results, None, "KV-094")
        self.assertEqual(1, len(results))
        self.assertEqual(u"ja", results[0].lang)
        self.assertEqual(u"https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-115x85.jpg",
                         results[0].thumb)
        self.assertEqual(66, results[0].score)
        self.assertEqual(2014, results[0].year)
        self.assertEqual(u"knights-visual-kv-094", results[0].id)
        self.assertEqual(u"kv-094 おしゃぶり予備校32 みづなれい", results[0].name)

    def test_search___no_result(self):
        results = ObjectContainer()  # type: ObjectContainer[MetadataSearchResult]
        service_knightsvisual_searcher.search(results, None, "QQ-094")
        self.assertEqual(0, len(results))
