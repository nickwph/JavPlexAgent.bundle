# coding=utf-8
import json
from unittest import TestCase

from munch import munchify

from plex.log import Log
from service.fanza import api


class Test(TestCase):

    def test_parse_as_dvd_product_id(self):
        self.assertEqual("ssni558", api.parse_as_dvd_product_id("SSNI-558"))
        self.assertEqual("ssni558", api.parse_as_dvd_product_id("SSNI558"))
        self.assertEqual("ssni558", api.parse_as_dvd_product_id("ssni558"))
        self.assertEqual("ssni558", api.parse_as_dvd_product_id("   SSNI-558 "))

    def test_parse_as_digital_product_id(self):
        self.assertEqual("ssni00558", api.parse_as_digital_product_id("SSNI-558"))
        self.assertEqual("ssni00558", api.parse_as_digital_product_id("  SSNI-558 "))
        self.assertEqual("ssni558", api.parse_as_digital_product_id("SSNI558"))

    def test_search_dvd_product___one_result(self):
        body = api.search_dvd_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result.items[0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_dvd_product___one_result_2(self):
        body = api.search_dvd_product("SOAV062")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("soav062", body.result.items[0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_dvd_product___no_result_for_vr_product(self):
        body = api.search_dvd_product("SIVR-002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_digital_product___one_result(self):
        body = api.search_digital_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result.items[0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_search_digital_product___two_result(self):
        body = api.search_digital_product("SIVR-002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(2, body.result.total_count)
        self.assertEqual("h_1382tnsivr00002", body.result.items[0].content_id)  # items is a reserved variable
        self.assertEqual("sivr00002", body.result.items[1].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product(self):
        body = api.get_dvd_product("ssni558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result.items[0].content_id)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___auto_convert_for_normal_product_id(self):
        body = api.get_dvd_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni558", body.result.items[0].content_id)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___no_result_for_digital_product_id(self):
        body = api.get_dvd_product("ssni00558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_dvd_product___no_result_for_vr_product_id(self):
        body = api.get_dvd_product("sivr00002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product(self):
        body = api.get_digital_product("ssni00558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result.items[0].content_id)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___auto_convert_for_normal_product_id(self):
        body = api.get_digital_product("SSNI-558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("ssni00558", body.result.items[0].content_id)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___no_result_for_dvd_product_id(self):
        body = api.get_digital_product("ssni558")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___no_result_for_vr_unconverted_product_id(self):
        body = api.get_digital_product("sivr002")
        self.assertEqual(200, body.result.status)
        self.assertEqual(0, body.result.total_count)
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_digital_product___one_result_for_vr_product_id(self):
        body = api.get_digital_product("h_1127vovs00341")
        self.assertEqual(200, body.result.status)
        self.assertEqual(1, body.result.total_count)
        self.assertEqual("h_1127vovs00341", body.result.items[0].content_id)  # items is a reserved variable
        Log.Debug(u"Body returned: {}".format(json.dumps(munchify(body), indent=2, ensure_ascii=False)))

    def test_get_product_description___for_digital_product(self):
        url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00558/"
        description = api.get_product_description(url)
        self.assertEqual(u"「お姉ちゃんもヤりなよ。すごい気持ちいいよ、セックス」ボクには父親が再婚してできた義理の妹たちがいる。名前は"
                         u"みはるとしおん。ある週末、父と母が外出して家を空けると、僕と妹たちの関係が大きく変わった。姉のみはるの前で妹"
                         u"のしおんと肉体関係を持つとそのままみはるともSEX。そして僕たちは両親がいない3日間、ただただSEXを楽しんだんだ"
                         u"。\n※ 配信方法によって収録内容が異なる場合があります。", description)

    def test_get_product_description___for_dvd_product(self):
        url = "https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ssni555/"
        description = api.get_product_description(url)
        self.assertEqual(u'初めて行った彼女の家に居たのは超美人でエッチな雰囲気の彼女の姉（長女）でした。'
                         u'そんなお姉さんが脚を開いてパンツを見せてくる。これは…明らかに僕を誘惑している様'
                         u'子。そして彼女が近くにいるのにも関わらずバレないように僕の興奮したチ●ポを弄り始'
                         u'め射精まで！！美脚で経験豊富な痴女お姉さんは僕の事を気に入ったのかそれからも痴女'
                         u'ってきてとうとう彼女のそばで一線まで超えることに。だってこんなの我慢できないよ！'
                         u'\n\n★アダルトブック「天使もえ写真集」の商品ご購入はこちらから★\n「コンビニ受取」'
                         u'対象商品です。詳しくはこちらをご覧ください。', description)

    def test_get_product_description___none_for_bad_url(self):
        url = "https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ssni1362/"
        description = api.get_product_description(url)
        self.assertEqual("", description)

    def test_get_actress(self):
        actress_id = 1031805
        body = api.get_actress(actress_id)
        self.assertEqual(200, int(body.result.status))
        self.assertEqual(1, body.result.result_count)
        self.assertEqual(1, int(body.result.total_count))
        self.assertEqual(1, len(body.result.actress))
        self.assertEqual(1031805, int(body.result.actress[0].id))
        self.assertEqual(u'桃乃木かな', body.result.actress[0].name)
        self.assertEqual(u'http://pics.dmm.co.jp/mono/actjpgs/momonogi_kana.jpg', body.result.actress[0].imageURL.large)
        self.assertEqual(u'http://pics.dmm.co.jp/mono/actjpgs/thumbnail/momonogi_kana.jpg',
                         body.result.actress[0].imageURL.small)
        self.assertEqual(
            u'https://al.dmm.co.jp/?lurl=https%3A%2F%2Fwww.dmm.co.jp%2Fmono%2Fdvd%2F-%2Flist%2F%3D%2Farticle%3Dactress%2Fid%3D1031805%2F&af_id=chokomomo-990&ch=api',
            body.result.actress[0].listURL.mono)
