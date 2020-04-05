# coding=utf-8
from unittest import TestCase

import caribbeancom_updater
import environments
from framework.plex_metadata import Movie

environments.is_local_debugging = True  # this is needed
reload(caribbeancom_updater)


class Test(TestCase):

    def test_update___not_run_if_not_carib(self):
        metadata = Movie()
        metadata.id = "somethingelse-070116-197"
        caribbeancom_updater.update(metadata)
        self.assertEqual(u"somethingelse-070116-197", metadata.id)
        self.assertEqual(u"Stub", metadata.title)

    def test_update___actual_run(self):
        metadata = Movie()
        metadata.id = "carib-070116-197"
        caribbeancom_updater.update(metadata)
        self.assertEqual(u"carib-070116-197", metadata.id)
        self.assertEqual(u"Carib-070116-197", metadata.title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.original_title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.tagline)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜\n\n「本日は身も心もチンポも癒されてくださいね'
                         u'ぇ」と頭を深々と下げてお辞儀をするAV界を引退してしまった上原亜衣ちゃんが、お客様に極上のおもてなしを披露する'
                         u'為カムバック！お客様の目を見つめて気持ちい部分を確認しながら優しくチク舐め手コキ。口蓋垂で亀頭を刺激させ口内'
                         u'を細めてチンコ全体を締め付けると、お客様は熱い精子を亜衣ちゃんの口いっぱいにブチまいちゃいます！',
                         metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_with_part(self):
        metadata = Movie()
        metadata.id = "carib-070116-197@1"
        caribbeancom_updater.update(metadata)
        self.assertEqual(u"carib-070116-197@1", metadata.id)
        self.assertEqual(u"Carib-070116-197 (Part 1)", metadata.title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.original_title)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜', metadata.tagline)
        self.assertEqual(u'洗練された大人のいやし亭 〜身も心もチンポも癒されてください〜\n\n「本日は身も心もチンポも癒されてくださいね'
                         u'ぇ」と頭を深々と下げてお辞儀をするAV界を引退してしまった上原亜衣ちゃんが、お客様に極上のおもてなしを披露する'
                         u'為カムバック！お客様の目を見つめて気持ちい部分を確認しながら優しくチク舐め手コキ。口蓋垂で亀頭を刺激させ口内'
                         u'を細めてチンコ全体を締め付けると、お客様は熱い精子を亜衣ちゃんの口いっぱいにブチまいちゃいます！',
                         metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
