# coding=utf-8

from unittest import TestCase

import service_1pondo_api


class Test(TestCase):

    def test_get_by_id(self):
        item = service_1pondo_api.get_by_id("100616_399")
        self.assertEqual(u"上原亜衣", item.actor)
        self.assertEqual([1937], item.actor_id)
        self.assertEqual([u"上原亜衣"], item.actresses_ja)
        self.assertEqual([u"Ai Uehara"], item.actresses_en)
        self.assertEqual(1, len(item.actresses_list))
        self.assertEqual(u"上原亜衣", item.actresses_list["1937"].name_ja)
        self.assertEqual(u"Ai Uehara", item.actresses_list["1937"].name_en)
        self.assertEqual(u"83-57-82", item.actresses_list["1937"].sizes)
        self.assertEqual(None, item.actresses_list["1937"].age)
        self.assertEqual(4.5714285714286, item.avg_rating)
        self.assertEqual(False, item.can_stream)
        self.assertEqual(None, item.conditions)
        self.assertEqual(u"あいちんこと上原亜衣ちゃんの本気（マジ）モード120パーセントが130分収録された一本道オリジナルスペシャル版"
                         u"です！\r\nファンのお宅へお邪魔してのガチセックス、余計な設定一切なしの濃厚セックス、ブチ切れ状態でのフェ"
                         u"ラ抜き。\r\nあの可愛い顔した亜衣ちゃんが顔を歪ませ額にしわをよせ感じまくる様は必見！\r\n抱き心地最高のカ"
                         u"ラダをくねらせ男に抱かれる亜衣ちゃんは見逃せません！\r\nこんな本気になった亜衣ちゃんは滅多に見ることがで"
                         u"きませんよ！", item.desc)
        self.assertEqual(u"130 minutes special version for the real sex by Ai Uehara. Without any redundant setting, "
                         u"she comes straight to the point, visits his home and sucks him immediately. She screws her "
                         u"cute face into an excited expression. Her body is good for hugging, and hot in the "
                         u"infrequent real sex.\r\n", item.desc_en)
        self.assertEqual(7936, item.duration)
        self.assertEqual(None, item.expire)
        self.assertEqual(True, item.has_flash)
        self.assertEqual(False, item.no_list_display)
        self.assertEqual(False, item.sample_exclude_flag)
        self.assertEqual(False, item.gallery)
        self.assertEqual(False, item.aff_zip)
        self.assertEqual(True, item.has_gallery)
        self.assertEqual(True, item.has_member_gallery_zip)
        self.assertEqual(True, item.has_sample_gallery_zip)
        self.assertEqual(7947, item.meta_movie_id)
        self.assertEqual(u"100616_399", item.movie_id)
        self.assertEqual(23848, item.movie_seq)
        self.assertEqual(u"https://www.1pondo.tv/moviepages/100616_399/images/thum_b.jpg", item.movie_thumb)
        self.assertEqual(104923, item.real_meta_movie_id)
        self.assertEqual(u"2016-10-06", item.release)
        self.assertEqual(None, item.series)
        self.assertEqual(None, item.series_en)
        self.assertEqual(None, item.series_id)
        self.assertEqual(2470, item.site_id)
        self.assertEqual(True, item.status)
        self.assertEqual(u"https://www.1pondo.tv/moviepages/100616_399/images/str.jpg", item.thumb_high)
        self.assertEqual(u"https://www.1pondo.tv/moviepages/100616_399/images/str.jpg", item.thumb_low)
        self.assertEqual(u"https://www.1pondo.tv/moviepages/100616_399/images/str.jpg", item.thumb_med)
        self.assertEqual(u"https://www.1pondo.tv/moviepages/100616_399/images/str.jpg", item.thumb_ultra)
        self.assertEqual(u"上原亜衣〜本気スペシャル〜", item.title)
        self.assertEqual(u"Ai Uehara: Real Sex", item.title_en)
        self.assertEqual(1, item.type)
        self.assertEqual(u"2016", item.year)
        self.assertEqual([1, 17, 38, 44, 46, 50, 54, 61, 66, 67, 70, 50000, 60000, 60001], item.uc)
        self.assertEqual([u"AV女優", u"美脚", u"痴女", u"ロリ", u"美尻", u"巨乳", u"手コキ", u"69", u"中出し",
                          u"生ハメ・生姦", u"フェラ", u"VIP", u"1080p", u"60fps"], item.uc_name)
        self.assertEqual([u"AV Idol", u"Sexy Legs", u"Slut", u"Loli", u"Sweet Ass", u"Big Tits", u"Handjob", u"69",
                          u"Creampie", u"Bareback", u"Blowjob", u"VIP", u"1080p", u"60fps"], item.uc_name_en)
        self.assertEqual(14, len(item.uc_name_list))
        self.assertEqual(u"AV Idol", item.uc_name_list["1"].name_en)
        self.assertEqual(u"AV女優", item.uc_name_list["1"].name_ja)
        self.assertEqual(False, item.is_ticket_only)
        self.assertEqual(5, len(item.member_files))
        self.assertEqual(u"240p.mp4", item.member_files[0].file_name)
        self.assertEqual(373355081, item.member_files[0].file_size)
        self.assertEqual(7947, item.member_files[0].meta_movie_id)
        self.assertEqual(u"2470", item.member_files[0].site_id)
        self.assertEqual(u"https://dl11.1pondo.tv/member/movies/100616_399/240p.mp4", item.member_files[0].url)
        self.assertEqual(5, len(item.sample_files))
        self.assertEqual(u"240p.mp4", item.sample_files[0].file_name)
        self.assertEqual(4645149, item.sample_files[0].file_size)
        self.assertEqual(7947, item.sample_files[0].meta_movie_id)
        self.assertEqual(u"2470", item.sample_files[0].site_id)
        self.assertEqual(u"https://smovie.1pondo.tv/sample/movies/100616_399/240p.mp4", item.sample_files[0].url)
        self.assertEqual(0, item.ppv_price.regular)
        self.assertEqual(0, item.ppv_price.discount)
        self.assertEqual(0, item.ppv_price.campaign)

    def test_get_actress_by_id(self):
        item = service_1pondo_api.get_actress_by_id(1937)
        self.assertEqual(1937, item.id)
        self.assertEqual(u"https://www.1pondo.tv/assets/thumbs/50x50/actor_6706.jpg", item.image_url)
        self.assertEqual(u"うえはらあい", item.kana)
        self.assertEqual(u"上原亜衣", item.name)
        self.assertEqual(2470, item.site_id)
