# coding=utf-8
import datetime
from unittest import TestCase

import service_knightsvisual_api


class Test(TestCase):

    def test_search(self):
        results = service_knightsvisual_api.search("KV-094")
        self.assertEqual(1, len(results))
        self.assertEqual(u"kv-094", results[0].id)
        self.assertEqual(u'https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-115x85.jpg',
                         results[0].thumbnail_url)
        self.assertEqual(u'おしゃぶり予備校32 みづなれい', results[0].title)
        self.assertEqual(u'https://www.knights-visual.com/works/furasupi/oshaburi_yobiko/kv-094/', results[0].url)
        self.assertEqual(2014, results[0].upload_year)

    def test_get_by_id(self):
        item = service_knightsvisual_api.get_by_id("KV-094")
        self.assertEqual(u"KV-094", item.id)
        self.assertEqual(u'みづなれい', item.actress_name)
        self.assertEqual(u'ひつき', item.author_name)
        self.assertEqual(u'https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-00.jpg', item.cover_url)
        self.assertEqual(u'フェラ抜き口内発射ゴックン長時間悶絶お掃除フェラ12発。ベロ射ゴックンお掃除5発。喉奥射精そのままゴックンお'
                         u'掃除6発。コパ先生大量顔噴射1発。敏感なチンコお掃除を見せたいので最初から最後までをノーカットで編集に拘りま'
                         u'した。最後は物凄いザーメン量の超大量顔射で締めくくる！', item.description)
        self.assertEqual(datetime.time(hour=2, minute=6), item.duration)
        self.assertEqual(126, item.duration_in_minutes)
        self.assertEqual(u'ふらすぴ', item.label)
        self.assertEqual('https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094.jpg', item.poster_url)
        self.assertEqual(87, len(item.sample_image_thumbnail_urls))
        self.assertEqual('https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-01-150x84.jpg',
                         item.sample_image_thumbnail_urls[0])
        self.assertEqual(87, len(item.sample_image_urls))
        self.assertEqual('https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-01.jpg',
                         item.sample_image_urls[0])
        self.assertEqual('http://fskvsample.knights-visual.com/samplemov/kv-094-samp-st.mp4',
                         item.sample_video_url)
        self.assertEqual(u'おしゃぶり予備校32 みづなれい', item.title)
        self.assertEqual(2014, item.upload_date.year)
        self.assertEqual(11, item.upload_date.month)
        self.assertEqual(23, item.upload_date.day)
        self.assertEqual(1, item.upload_date.hour)
        self.assertEqual(59, item.upload_date.minute)
        self.assertEqual(20, item.upload_date.second)
        self.assertEqual(0, item.upload_date.microsecond)
        self.assertEqual('https://www.knights-visual.com/works/furasupi/KV-094', item.url)
