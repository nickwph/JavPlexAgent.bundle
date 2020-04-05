# coding=utf-8
from unittest import TestCase

import environments
from framework.plex_metadata import Movie


class Test(TestCase):

    def setUp(self):
        environments.is_local_debugging = True  # this is needed

    def test_update___not_run_if_not_fanza(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "somethingelse-dvd-070116197"
        fanza_updater.update(metadata)
        self.assertEqual(u"somethingelse-dvd-070116197", metadata.id)
        self.assertEqual(u"Stub", metadata.title)

    def test_update___when_no_review_exist(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-dvd-1stars220"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-1stars220", metadata.id)
        self.assertEqual(u"1STARS220", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_dvd(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-dvd-ssni558"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ssni558", metadata.id)
        self.assertEqual(u"SSNI558", metadata.title)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間', metadata.original_title)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間', metadata.tagline)
        self.assertEqual(u'エスワン ナンバーワンスタイル', metadata.studio)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間\n\n「お姉ちゃんもヤりなよ。すごい気持ちいいよ'
                         u'、セックス」ボクには父親が再婚してできた義理の妹たちがいる。名前はみはるとしおん。ある週末、父と母が外出し'
                         u'て家を空けると、僕と妹たちの関係が大きく変わった。姉のみはるの前で妹のしおんと肉体関係を持つとそのままみは'
                         u'るともSEX。そして僕たちは両親がいない3日間、ただただSEXを楽しんだんだ。\n「コンビニ受取」対象商品です。詳'
                         u'しくはこちらをご覧ください。', metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_dvd_with_part(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-dvd-ssni558@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ssni558@1", metadata.id)
        self.assertEqual(u"SSNI558 (Part 1)", metadata.title)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間', metadata.original_title)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間', metadata.tagline)
        self.assertEqual(u'エスワン ナンバーワンスタイル', metadata.studio)
        self.assertEqual(u'巨乳姉妹2人とただひたすらセックスに明け暮れた両親不在の3日間\n\n「お姉ちゃんもヤりなよ。すごい気持ちいいよ'
                         u'、セックス」ボクには父親が再婚してできた義理の妹たちがいる。名前はみはるとしおん。ある週末、父と母が外出し'
                         u'て家を空けると、僕と妹たちの関係が大きく変わった。姉のみはるの前で妹のしおんと肉体関係を持つとそのままみは'
                         u'るともSEX。そして僕たちは両親がいない3日間、ただただSEXを楽しんだんだ。\n「コンビニ受取」対象商品です。詳'
                         u'しくはこちらをご覧ください。', metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_dvd_use_ideapocket_poster(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-dvd-ipx453@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ipx453@1", metadata.id)
        self.assertEqual(u"IPX453 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.ideapocket.com/contents/works/ipx453/ipx453-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital_use_ideapocket_poster(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-ipx00453@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-ipx00453@1", metadata.id)
        self.assertEqual(u"IPX00453 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.ideapocket.com/contents/works/ipx453/ipx453-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital_use_s1_poster(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-ssni00558@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-ssni00558@1", metadata.id)
        self.assertEqual(u"SSNI00558 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.s1s1s1.com/contents/works/ssni558/ssni558-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital_use_sample_image_as_poster(self):
        import image_helper
        image_helper.can_analyze_images = True
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-sivr00067@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-sivr00067@1", metadata.id)
        self.assertEqual(u"SIVR00067 (Part 1)", metadata.title)
        self.assertEqual(u"https://pics.dmm.co.jp/digital/video/sivr00067/sivr00067jp-1.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital_use_s1_poster_if_pillow_not_available(self):
        import image_helper
        image_helper.can_analyze_images = False
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-sivr00067@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-sivr00067@1", metadata.id)
        self.assertEqual(u"SIVR00067 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.s1s1s1.com/contents/works/sivr067/sivr067-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital_with_part(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-55tmavr00077@1"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-55tmavr00077@1", metadata.id)
        self.assertEqual(u"55TMAVR00077 (Part 1)", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_digital(self):
        import fanza_updater
        metadata = Movie()
        metadata.id = "fanza-digital-h_1127vovs00341"
        fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-h_1127vovs00341", metadata.id)
        self.assertEqual(u"H_1127VOVS00341", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
