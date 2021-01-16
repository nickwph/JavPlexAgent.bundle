# coding=utf-8
import datetime
from unittest import TestCase

import api


class Test(TestCase):

    def test_get_by_id(self):
        item = api.get_by_id("805_urara_02")
        self.assertEqual(u"805_urara_02", item.id)
        self.assertEqual(u"https://www.s-cute.com/contents/805_urara_02", item.url)
        self.assertEqual(u"ツインテールが似合うロリっ子の制服Ｈ／Urara", item.title)
        self.assertEqual(u"制服、ツインテール、白ソックス、剛毛、と、ロリ要素高め、かつ個性的な美少女Uraraちゃん。言"
                         u"われるがまま、ローターでオナニーしたり、はしたない姿もたくさん見せてくれます。一番好きだとい"
                         u"うSEX後のオナニーを愉しむ様子もお見逃しなく！", item.description)
        self.assertEqual(52, item.duration_in_min)
        self.assertEqual(u"http://static.s-cute.com/images/805_urara/805_urara_02/805_urara_02.jpg", item.cover_url)
        self.assertEqual(39, item.photo_count)
        self.assertEqual(datetime.datetime(2020, 12, 24), item.release_date)
        self.assertEqual(805, item.actress.id)
        self.assertEqual(u"Urara", item.actress.name)
        self.assertEqual(u"誰とでもすぐに仲良くなれそうな明るい性格のUraraちゃん。148cmの小柄な体に人当たりの良い笑顔"
                         u"を兼ね備えた美少女です。エッチとオナニーは別物！と明言する彼女は、前戯が大好き。手でもお口で"
                         u"も、何時間でもしてほしい！という欲張りさんです。", item.actress.description)
        self.assertEqual(u"https://www.s-cute.com/girls/805_urara/", item.actress.url)
        self.assertEqual(u"http://static.s-cute.com/images/805_urara/805_urara/805_urara_150.jpg", item.actress.photo_url)
        self.assertEqual(10, len(item.photos))
        self.assertEqual(u"http://photos.s-cute.com/130901/sample/contents/805_urara/805_urara_02/001.jpg", item.photos[0].image_url)
        self.assertEqual(u"http://photos.s-cute.com/130901/sample/thumbnails/805_urara/805_urara_02/001.jpg", item.photos[0].thumbnail_url)
        self.assertEqual(5, len(item.tags))
        self.assertEqual(u"hattori", item.tags[0].name)
        self.assertEqual(u"http://www.s-cute.com/contents/?tag=hattori", item.tags[0].url)
