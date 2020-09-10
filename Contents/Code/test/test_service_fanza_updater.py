# coding=utf-8
from unittest import TestCase

import environments
import service_fanza_updater
from framework.plex_metadata import Movie

environments.is_local_debugging = True  # this is needed
reload(service_fanza_updater)


class Test(TestCase):

    def test_update___not_run_if_not_fanza(self):
        metadata = Movie()
        metadata.id = "somethingelse-dvd-070116197"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"somethingelse-dvd-070116197", metadata.id)
        self.assertEqual(u"Stub", metadata.title)

    def test_update___when_no_review_exist(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-1stars220"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-1stars220", metadata.id)
        self.assertEqual(u"STARS-220", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)

    def test_update___actual_run_dvd(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-ssni558"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ssni558", metadata.id)
        self.assertEqual(u"SSNI-558", metadata.title)
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
        self.assertEqual(10, len(metadata.art))
        self.assertEqual(8, len(metadata.genres))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/ssni00558/ssni00558jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_dvd_with_part(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-ssni558@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ssni558@1", metadata.id)
        self.assertEqual(u"SSNI-558 (Part 1)", metadata.title)
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
        self.assertEqual(10, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/ssni00558/ssni00558jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_dvd_use_ideapocket_poster(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-ipx453@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-ipx453@1", metadata.id)
        self.assertEqual(u"IPX-453 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.ideapocket.com/contents/works/ipx453/ipx453-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(12, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/ipx00453/ipx00453jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_use_ideapocket_poster(self):
        metadata = Movie()
        metadata.id = "fanza-digital-ipx00453@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-ipx00453@1", metadata.id)
        self.assertEqual(u"IPX-453 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.ideapocket.com/contents/works/ipx453/ipx453-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(12, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/ipx00453/ipx00453jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_use_s1_poster(self):
        metadata = Movie()
        metadata.id = "fanza-digital-ssni00558@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-ssni00558@1", metadata.id)
        self.assertEqual(u"SSNI-558 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.s1s1s1.com/contents/works/ssni558/ssni558-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(10, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/ssni00558/ssni00558jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_use_sample_image_as_poster(self):
        import utility_image_helper
        utility_image_helper.can_analyze_images = True
        metadata = Movie()
        metadata.id = "fanza-digital-sivr00067@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-sivr00067@1", metadata.id)
        self.assertEqual(u"SIVR-067 (Part 1)", metadata.title)
        self.assertEqual(u"https://pics.dmm.co.jp/digital/video/sivr00067/sivr00067jp-1.jpg",
                         metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(12, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/sivr00067/sivr00067jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_use_s1_poster_if_pillow_not_available(self):
        import utility_image_helper
        utility_image_helper.can_analyze_images = False
        metadata = Movie()
        metadata.id = "fanza-digital-sivr00067@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-sivr00067@1", metadata.id)
        self.assertEqual(u"SIVR-067 (Part 1)", metadata.title)
        self.assertEqual(u"https://www.s1s1s1.com/contents/works/sivr067/sivr067-ps.jpg", metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(12, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/sivr00067/sivr00067jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_use_cropped_cover_as_poster(self):
        import utility_image_helper
        utility_image_helper.can_analyze_images = True
        metadata = Movie()
        metadata.id = "fanza-digital-36doks00515"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-36doks00515", metadata.id)
        self.assertEqual(u"DOKS-515", metadata.title)
        self.assertEqual(u"https://pics.dmm.co.jp/digital/video/36doks00515/36doks00515pl.jpg@cropped",
                         metadata.posters.keys()[0])
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(20, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/36doks00515/36doks00515jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital_with_part(self):
        metadata = Movie()
        metadata.id = "fanza-digital-55tmavr00077@1"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-55tmavr00077@1", metadata.id)
        self.assertEqual(u"TMAVR-077 (Part 1)", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(10, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/55tmavr00077/55tmavr00077jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___actual_run_digital(self):
        metadata = Movie()
        metadata.id = "fanza-digital-h_1127vovs00341"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-digital-h_1127vovs00341", metadata.id)
        self.assertEqual(u"VOVS-341", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(11, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/h_1127vovs00341/h_1127vovs00341jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___with_no_actress(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-hunta749"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-hunta749", metadata.id)
        self.assertEqual(u"HUNTA-749", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(12, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/hunta00749/hunta00749jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___with_no_actress_image_url(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-mird200"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-mird200", metadata.id)
        self.assertEqual(u"MIRD-200", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(10, len(metadata.art))
        self.assertEqual(10, len(metadata.roles))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/mird00200/mird00200jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])

    def test_update___weird_product_poster_image(self):
        metadata = Movie()
        metadata.id = "fanza-dvd-118docp212"
        service_fanza_updater.update(metadata)
        self.assertEqual(u"fanza-dvd-118docp212", metadata.id)
        self.assertEqual(u"DOCP-212", metadata.title)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(18, metadata.content_rating_age)
        self.assertEqual(20, len(metadata.art))
        self.assertEqual(2, len(metadata.roles))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://pics.dmm.co.jp/digital/video/118docp00212/118docp00212jp-{}.jpg".format(i + 1),
                metadata.art.keys()[i])
