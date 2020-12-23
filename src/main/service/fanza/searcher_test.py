# coding=utf-8
from unittest import TestCase

from plex_agent import MetadataSearchResult
from plex_container import ObjectContainer
from service.fanza import searcher


class Test(TestCase):

    def test_search___actual_run(self):
        results = ObjectContainer()
        searcher.search(results, None, "SSNI-558")
        self.assertEqual(2, len(results))

        result_0 = results[0]  # type: MetadataSearchResult
        self.assertEqual(u"fanza-dvd-ssni558", result_0.id)
        self.assertEqual(u"SSNI558 巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間", result_0.name)
        self.assertEqual(u"https://pics.dmm.co.jp/mono/movie/adult/ssni558/ssni558ps.jpg", result_0.thumb)
        self.assertEqual(u"ja", result_0.lang)
        self.assertEqual(2019, result_0.year)
        self.assertEqual(100, result_0.score)

        result_1 = results[1]  # type: MetadataSearchResult
        self.assertEqual(u"fanza-digital-ssni00558", result_1.id)
        self.assertEqual(u"SSNI00558 巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間", result_1.name)
        self.assertEqual(u"https://pics.dmm.co.jp/digital/video/ssni00558/ssni00558ps.jpg", result_1.thumb)
        self.assertEqual(u"ja", result_1.lang)
        self.assertEqual(2019, result_1.year)
        self.assertEqual(100, result_1.score)

    def test_search___actual_run_with_part_number(self):
        results = ObjectContainer()
        searcher.search(results, 1, "SSNI-558")
        self.assertEqual(2, len(results))

        result_0 = results[0]  # type: MetadataSearchResult
        self.assertEqual(u"fanza-dvd-ssni558@1", result_0.id)
        self.assertEqual(u"SSNI558 巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間", result_0.name)
        self.assertEqual(u"https://pics.dmm.co.jp/mono/movie/adult/ssni558/ssni558ps.jpg", result_0.thumb)
        self.assertEqual(u"ja", result_0.lang)
        self.assertEqual(2019, result_0.year)
        self.assertEqual(100, result_0.score)

        result_1 = results[1]  # type: MetadataSearchResult
        self.assertEqual(u"fanza-digital-ssni00558@1", result_1.id)
        self.assertEqual(u"SSNI00558 巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間", result_1.name)
        self.assertEqual(u"https://pics.dmm.co.jp/digital/video/ssni00558/ssni00558ps.jpg", result_1.thumb)
        self.assertEqual(u"ja", result_1.lang)
        self.assertEqual(2019, result_1.year)
        self.assertEqual(100, result_1.score)
