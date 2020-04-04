# coding=utf-8
import json
from unittest import TestCase

from munch import munchify

from .. import fanza_api
from ..framework.plex_log import Log


class Test(TestCase):

    def test_parse_as_dvd_product_id(self):
        self.assertEqual("ssni558", fanza_api.parse_as_dvd_product_id("SSNI-558"))
        self.assertEqual("ssni558", fanza_api.parse_as_dvd_product_id("SSNI558"))
        self.assertEqual("ssni558", fanza_api.parse_as_dvd_product_id("ssni558"))
        self.assertEqual("ssni558", fanza_api.parse_as_dvd_product_id("   SSNI-558 "))

    def test_parse_as_digital_product_id(self):
        self.assertEqual("ssni00558", fanza_api.parse_as_digital_product_id("SSNI-558"))
        self.assertEqual("ssni00558", fanza_api.parse_as_digital_product_id("  SSNI-558 "))
        self.assertEqual("ssni558", fanza_api.parse_as_digital_product_id("SSNI558"))

    def test_search_dvd_product___one_result(self):
        body = fanza_api.search_dvd_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_dvd_product___no_result_for_vr_product(self):
        body = fanza_api.search_dvd_product("SIVR-002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_digital_product___one_result(self):
        body = fanza_api.search_digital_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_digital_product___two_result(self):
        body = fanza_api.search_digital_product("SIVR-002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(2, body.result.total_count)
        self.assertEqual("h_1382tnsivr00002", body.result['items'][0].content_id)  # items is a reserved variable
        self.assertEqual("sivr00002", body.result['items'][1].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product(self):
        body = fanza_api.get_dvd_product("ssni558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___auto_convert_for_normal_product_id(self):
        body = fanza_api.get_dvd_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___no_result_for_digital_product_id(self):
        body = fanza_api.get_dvd_product("ssni00558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___no_result_for_vr_product_id(self):
        body = fanza_api.get_dvd_product("sivr00002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product(self):
        body = fanza_api.get_digital_product("ssni00558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___auto_convert_for_normal_product_id(self):
        body = fanza_api.get_digital_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result['items'][0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___no_result_for_dvd_product_id(self):
        body = fanza_api.get_digital_product("ssni558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___no_result_for_vr_product_id(self):
        body = fanza_api.get_digital_product("sivr002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_product_description___for_digital_product(self):
        url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00558/"
        description = fanza_api.get_product_description(url)
        self.assertEqual(u"「お姉ちゃんもヤりなよ。すごい気持ちいいよ、セックス」ボクには父親が再婚してできた義理の妹たちがいる。名前は"
                         u"みはるとしおん。ある週末、父と母が外出して家を空けると、僕と妹たちの関係が大きく変わった。姉のみはるの前で妹"
                         u"のしおんと肉体関係を持つとそのままみはるともSEX。そして僕たちは両親がいない3日間、ただただSEXを楽しんだんだ"
                         u"。\n※ 配信方法によって収録内容が異なる場合があります。", description)

    def test_get_product_description___for_dvd_product(self):
        url = "https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ssni555/"
        description = fanza_api.get_product_description(url)
        self.assertEqual(u"初めて行った彼女の家に居たのは超美人でエッチな雰囲気の彼女の姉（長女）でした。そんなお姉さんが脚を開いてパン"
                         u"ツを見せてくる。これは…明らかに僕を誘惑している様子。そして彼女が近くにいるのにも関わらずバレないように僕の興"
                         u"奮したチ●ポを弄り始め射精まで！！美脚で経験豊富な痴女お姉さんは僕の事を気に入ったのかそれからも痴女ってきてと"
                         u"うとう彼女のそばで一線まで超えることに。だってこんなの我慢できないよ！\n\n★アダルトブック「天使もえ写真集」"
                         u"の商品ご購入はこちらから★\n「コンビニ受取」対象商品です。詳しくはこちらをご覧ください。", description)

    def test_get_product_description___none_for_bad_url(self):
        url = "https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ssni1362/"
        description = fanza_api.get_product_description(url)
        self.assertEqual(None, description)
