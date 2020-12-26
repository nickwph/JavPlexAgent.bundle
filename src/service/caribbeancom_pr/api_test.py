# coding=utf-8
import datetime
from unittest import TestCase

from service.caribbeancom_pr import api


class Test(TestCase):

    def test_get_item(self):
        item = api.get_item("091616-007")
        self.assertEqual(u"091616-007", item.id)
        self.assertEqual(u"https://www.caribbeancompr.com/moviepages/091616_007/index.html", item.url)
        self.assertEqual(u"月刊　上原亜衣", item.title)
        self.assertEqual(u"天使のような可愛いルックスと、その容姿からは想像も出来ないハードプレイをこなす上原亜衣ちゃんがついに月刊で登場！ "
                         u"「激イカセ」、「Z〜極上女優の絶頂アクメ〜」、「マンコ図鑑」亜衣ちゃんの魅力を満喫できる超ヒット3作品コンボを豪華"
                         u"内容でお届け致します！ AV界の女王・上原亜衣ちゃんがハードプレイに挑戦！余計な設定や演出は一切なし！男女一対一で"
                         u"濃厚に絡み合う本気SEX、 自然恥毛の綺麗なおまんこを惜しげもなくゆっくりくぱぁ〜！それでは亜衣ちゃんの魅力を大ボ"
                         u"リューム120％詰め込んだ月刊 上原亜衣を存分にお楽しみください！", item.description)
        self.assertEqual(u"https://smovie.caribbeancompr.com/moviepages/091616_007/images/main_b.jpg", item.poster_url)
        self.assertEqual(u"https://smovie.caribbeancompr.com/moviepages/091616_007/images/l_l.jpg", item.background_url)
        # self.assertEqual(u"https://www.caribbeancompr.com/search_act/6706/1.html", item.actor_url)
        self.assertEqual(u"上原亜衣", item.actor_name)
        # self.assertEqual(6706, item.actor_id)
        # self.assertEqual(u"https://www.caribbeancom.com/box/search_act/6706/images/top.jpg", item.actor_large_picture_url)
        # self.assertEqual(u"https://www.caribbeancom.com/images/actress/50x50/actor_6706.jpg", item.actor_small_picture_url)
        self.assertEqual(u"https://smovie.caribbeancompr.com/sample/movies/091616_007/480p.mp4", item.sample_video_url)
        self.assertEqual(datetime.date(2016, 9, 16), item.upload_date)
        self.assertEqual(datetime.time(2, 22, 38), item.duration)
        self.assertEqual(8558, item.duration_in_seconds)
        self.assertEqual(u"月刊○○", item.series_name)
        # self.assertEqual(960, item.series_id)
        # self.assertEqual(u"https://www.caribbeancom.com/series/960/index.html", item.series_url)
        self.assertEqual(7, len(item.tags))
        self.assertEqual(u"AV女優", item.tags[0].name)
        self.assertEqual(u"1", item.tags[0].slug)
        self.assertEqual(u"https://www.caribbeancompr.com/listpages/1_1.html", item.tags[0].url)
        # self.assertEqual(7, len(item.genres))
        # self.assertEqual(u"中出し", item.genres[0].name)
        # self.assertEqual(u"creampie", item.genres[0].slug)
        # self.assertEqual(u"https://www.caribbeancom.com/listpages/creampie1.htm", item.genres[0].url)
        self.assertEqual(5, item.rating)

    def test_get_item_2(self):
        item = api.get_item("032715-157")
        self.assertEqual(u"032715-157", item.id)
        self.assertEqual(u"https://www.caribbeancompr.com/moviepages/032715_157/index.html", item.url)
        self.assertEqual(u"月刊　上原亜衣", item.title)
        self.assertEqual(u"天使のような可愛いルックスと、その容姿からは想像も出来ないハードプレイをこなす上原亜衣ちゃんがついに月刊で登場！ "
                         u"「激イカセ」、「Z〜極上女優の絶頂アクメ〜」、「マンコ図鑑」亜衣ちゃんの魅力を満喫できる超ヒット3作品コンボを豪華"
                         u"内容でお届け致します！ AV界の女王・上原亜衣ちゃんがハードプレイに挑戦！余計な設定や演出は一切なし！男女一対一で"
                         u"濃厚に絡み合う本気SEX、 自然恥毛の綺麗なおまんこを惜しげもなくゆっくりくぱぁ〜！それでは亜衣ちゃんの魅力を大ボ"
                         u"リューム120％詰め込んだ月刊 上原亜衣を存分にお楽しみください！", item.description)
        self.assertEqual(u"https://smovie.caribbeancompr.com/moviepages/091616_007/images/main_b.jpg", item.poster_url)
        self.assertEqual(u"https://smovie.caribbeancompr.com/moviepages/091616_007/images/l_l.jpg", item.background_url)
        # self.assertEqual(u"https://www.caribbeancompr.com/search_act/6706/1.html", item.actor_url)
        self.assertEqual(u"上原亜衣", item.actor_name)
        # self.assertEqual(6706, item.actor_id)
        # self.assertEqual(u"https://www.caribbeancom.com/box/search_act/6706/images/top.jpg", item.actor_large_picture_url)
        # self.assertEqual(u"https://www.caribbeancom.com/images/actress/50x50/actor_6706.jpg", item.actor_small_picture_url)
        self.assertEqual(u"https://smovie.caribbeancompr.com/sample/movies/091616_007/480p.mp4", item.sample_video_url)
        self.assertEqual(datetime.date(2016, 9, 16), item.upload_date)
        self.assertEqual(datetime.time(2, 22, 38), item.duration)
        self.assertEqual(8558, item.duration_in_seconds)
        self.assertEqual(u"月刊○○", item.series_name)
        # self.assertEqual(960, item.series_id)
        # self.assertEqual(u"https://www.caribbeancom.com/series/960/index.html", item.series_url)
        self.assertEqual(7, len(item.tags))
        self.assertEqual(u"AV女優", item.tags[0].name)
        self.assertEqual(u"1", item.tags[0].slug)
        self.assertEqual(u"https://www.caribbeancompr.com/listpages/1_1.html", item.tags[0].url)
        # self.assertEqual(7, len(item.genres))
        # self.assertEqual(u"中出し", item.genres[0].name)
        # self.assertEqual(u"creampie", item.genres[0].slug)
        # self.assertEqual(u"https://www.caribbeancom.com/listpages/creampie1.htm", item.genres[0].url)
        self.assertEqual(5, item.rating)

    def test_get_item_without_series(self):
        item = api.get_item("052716-172")
        self.assertEqual(u"052716-172", item.id)
        self.assertEqual(u"https://www.caribbeancom.com/moviepages/052716-172/index.html", item.url)
        self.assertEqual(u"ものすごい三穴蹂躙", item.title)

    def test_extract_id(self):
        self.assertEqual("123123-233", api.extract_id("caribpr-123123-233"))
        self.assertEqual("123123-233", api.extract_id("Caribpr-123123-233"))
        self.assertEqual("123123-233", api.extract_id("Caribpr-123123-233-asd"))
        self.assertEqual("123123-233", api.extract_id("Caribpr-123123-233-FHD"))
        self.assertEqual(None, api.extract_id("Caribpr-12123-233-FHD"))
        self.assertEqual("123123-23123123", api.extract_id("Caribpr-123123-23123123-FHD"))
        self.assertEqual("123123-1", api.extract_id("Caribpr-123123-1-FHD"))
        self.assertEqual("123123-1", api.extract_id("Caribbeanpr-123123-1-FHD"))
        self.assertEqual("123123-1", api.extract_id("Caribbeancompr-123123-1-FHD"))
        self.assertEqual(None, api.extract_id("Caribbpr-123123-1-FHD"))
        self.assertEqual(None, api.extract_id("Caribbeancpr-123123-1-FHD"))

    def test_has_valid_id(self):
        self.assertEqual(True, api.has_valid_id("carib-123123-233"))
        self.assertEqual(True, api.has_valid_id("Carib-123123-233"))
        self.assertEqual(True, api.has_valid_id("Carib-123123-233-asd"))
        self.assertEqual(True, api.has_valid_id("Carib-123123-233-FHD"))
        self.assertEqual(False, api.has_valid_id("Carib-12123-233-FHD"))
        self.assertEqual(True, api.has_valid_id("Carib-123123-23123123-FHD"))
        self.assertEqual(True, api.has_valid_id("Carib-123123-1-FHD"))
        self.assertEqual(True, api.has_valid_id("Caribbean-123123-1-FHD"))
        self.assertEqual(True, api.has_valid_id("Caribbeancom-123123-1-FHD"))
        self.assertEqual(False, api.has_valid_id("Caribb-123123-1-FHD"))
        self.assertEqual(False, api.has_valid_id("Caribbeanc-123123-1-FHD"))
