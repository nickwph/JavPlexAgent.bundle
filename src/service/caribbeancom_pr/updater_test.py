# coding=utf-8
from unittest import TestCase

from libs.plex.plex_metadata import Movie
from service.caribbeancom import updater


class Test(TestCase):

    def test_update___not_run_if_not_carib(self):
        metadata = Movie()
        metadata.id = "somethingelse-070116-197"
        updater.update(metadata)
        self.assertEqual(u"somethingelse-070116-197", metadata.id)
        self.assertEqual(u"Stub", metadata.title)

    def test_update___actual_run(self):
        metadata = Movie()
        metadata.id = "carib-070116-197"
        updater.update(metadata)
        self.assertEqual(u"carib-070116-197", metadata.id)
        self.assertEqual(u"CARIB-070116-197", metadata.title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.original_title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.tagline)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜\n\n「本日は身も心もチンポも癒されてくださいね'
                         u'ぇ」と頭を深々と下げてお辞儀をするAV界を引退してしまった上原亜衣ちゃんが、お客様に極上のおもてなしを披露する'
                         u'為カムバック！お客様の目を見つめて気持ちい部分を確認しながら優しくチク舐め手コキ。口蓋垂で亀頭を刺激させ口内'
                         u'を細めてチンコ全体を締め付けると、お客様は熱い精子を亜衣ちゃんの口いっぱいにブチまいちゃいます！',
                         metadata.summary)
        self.assertEqual(u"https://smovie.caribbeancom.com/moviepages/070116-197/images/jacket.jpg@padded",
                         metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(5, len(metadata.art))
        self.assertEqual(9, len(metadata.genres))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://www.caribbeancom.com/moviepages/070116-197/images/l/00{}.jpg".format(i + 1),
                sorted(metadata.art.keys())[i])

    def test_update___actual_run_2(self):
        metadata_2 = Movie()
        metadata_2.id = "carib-041114-579"
        updater.update(metadata_2)
        self.assertEqual(u"carib-041114-579", metadata_2.id)
        self.assertEqual(u"CARIB-041114-579", metadata_2.title)
        self.assertEqual(u'絶潮スプラッシュ 〜初無修正でハメ潮観察〜', metadata_2.original_title)
        self.assertEqual(u'絶潮スプラッシュ 〜初無修正でハメ潮観察〜', metadata_2.tagline)
        self.assertEqual(u"https://smovie.caribbeancom.com/moviepages/041114-579/images/jacket.jpg@padded",
                         metadata_2.posters.keys()[0])
        self.assertEqual(u"Adult", metadata_2.content_rating)
        self.assertEqual(18, metadata_2.content_rating_age)
        self.assertEqual(5, len(metadata_2.art))
        self.assertEqual(10, len(metadata_2.genres))
        for i in range(0, len(metadata_2.art)):
            self.assertEqual(
                u"https://www.caribbeancom.com/moviepages/041114-579/images/l/00{}.jpg".format(i + 1),
                metadata_2.art.keys()[i])

    def test_update___actual_run_with_part(self):
        metadata = Movie()
        metadata.id = "carib-070116-197@1"
        updater.update(metadata)
        self.assertEqual(u"carib-070116-197@1", metadata.id)
        self.assertEqual(u"CARIB-070116-197 (Part 1)", metadata.title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.original_title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.tagline)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜\n\n「本日は身も心もチンポも癒されてくださいね'
                         u'ぇ」と頭を深々と下げてお辞儀をするAV界を引退してしまった上原亜衣ちゃんが、お客様に極上のおもてなしを披露する'
                         u'為カムバック！お客様の目を見つめて気持ちい部分を確認しながら優しくチク舐め手コキ。口蓋垂で亀頭を刺激させ口内'
                         u'を細めてチンコ全体を締め付けると、お客様は熱い精子を亜衣ちゃんの口いっぱいにブチまいちゃいます！',
                         metadata.summary)
        self.assertEqual(u"https://smovie.caribbeancom.com/moviepages/070116-197/images/jacket.jpg@padded",
                         metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(5, len(metadata.art))
        self.assertEqual(9, len(metadata.genres))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://www.caribbeancom.com/moviepages/070116-197/images/l/00{}.jpg".format(i + 1),
                metadata.art.keys()[i])
