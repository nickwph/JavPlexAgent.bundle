# coding=utf-8
import datetime
from unittest import TestCase

from service.heyzo import api


class Test(TestCase):

    def test_get_by_id_2272(self):
        item = api.get_by_id("2272")
        self.assertEqual(u"2272", item.id)
        self.assertEqual(u'朝比奈菜々子', item.actress_name)
        self.assertEqual(737, item.actress_id)
        self.assertEqual(u'https://www.heyzo.com/listpages/actor_737_1.html?sort=pop', item.actress_url)
        self.assertEqual(u'https://www.heyzo.com/actorprofile/3000/0737/profile.jpg', item.actress_picture_url)
        self.assertEqual(u'https://www.heyzo.com/moviepages/2272/index.html', item.url)
        self.assertEqual(u'https://www.heyzo.com/contents/3000/2272/images/player_thumbnail.jpg', item.cover_url)
        self.assertEqual(u'朝比奈菜々子のパイでズッてあげる！', item.title)
        self.assertEqual(u'', item.description)
        self.assertEqual(datetime.date(2020, 5, 28), item.release_date)
        self.assertEqual(1, len(item.categories))
        self.assertEqual(3, len(item.tags))
        self.assertEqual(2.3, item.rating)

    def test_get_by_id_0467(self):
        item = api.get_by_id("0467")
        self.assertEqual(u"0467", item.id)
        self.assertEqual(u'あいださくら', item.actress_name)
        self.assertEqual(238, item.actress_id)
        self.assertEqual(u'https://www.heyzo.com/listpages/actor_238_1.html?sort=pop', item.actress_url)
        self.assertEqual(u'https://www.heyzo.com/actorprofile/3000/0238/profile.jpg', item.actress_picture_url)
        self.assertEqual(u'https://www.heyzo.com/moviepages/0467/index.html', item.url)
        self.assertEqual(u'https://www.heyzo.com/contents/3000/0467/images/player_thumbnail.jpg', item.cover_url)
        self.assertEqual(u'あいださくらの湯けむり温泉旅情～いっぱいおっぱいがでちゃう～', item.title)
        self.assertEqual(u'前作でインパクトを与えた、元お菓子系アイドル「あいださくら」が再び登場！温泉に浸かっていると、おもちゃ責め'
                         u'され頬を紅潮させながら感じちゃうさくらちゃん。その直後には連続顔射なんと怒涛の６連発！顔中真っ白にされなが'
                         u'ら、余裕のピースまでするエロっ娘。若さ溢れるキレイなカラダにはあるヒミツが！興奮すると100%本物母乳が溢れ出'
                         u'すのです。美しく勃起したプリップリの乳首に吸い付きたくなること間違いなしっ！乳首だけまるで別の生き物のよう。'
                         u'男優にミルクをご奉仕し、そのお返しにと濃厚ザーメンを中だしされ、辺り一面に白いお汁が飛び散って・・・'
                         u'これは必見です！', item.description)
        self.assertEqual(datetime.date(2013, 11, 29), item.release_date)
        self.assertEqual(3, len(item.categories))
        self.assertEqual(10, len(item.tags))
        self.assertEqual(3.8, item.rating)
