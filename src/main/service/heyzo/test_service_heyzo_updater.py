# coding=utf-8
from unittest import TestCase

from environment import environments
from service.knights_visual import service_knightsvisual_updater
from plex_metadata import Movie

environments.is_local_debugging = True  # this is needed
reload(service_knightsvisual_updater)


class Test(TestCase):

    def test_update___actual_run(self):
        metadata = Movie()
        metadata.id = "knights-visual-kv-094"
        service_knightsvisual_updater.update(metadata)
        self.assertEqual(u"knights-visual-kv-094", metadata.id)
        self.assertEqual(u"KV094", metadata.title)
        self.assertEqual(u'おしゃぶり予備校32 みづなれい', metadata.original_title)
        self.assertEqual(u'おしゃぶり予備校32 みづなれい', metadata.tagline)
        self.assertEqual(u'おしゃぶり予備校32 みづなれい\n\n'
                         u'フェラ抜き口内発射ゴックン長時間悶絶お掃除フェラ12発。ベロ射ゴックンお掃除5発。喉奥射精そのままゴックンお掃'
                         u'除6発。コパ先生大量顔噴射1発。敏感なチンコお掃除を見せたいので最初から最後までをノーカットで編集に拘りまし'
                         u'た。最後は物凄いザーメン量の超大量顔射で締めくくる！',
                         metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(u"Knights Visual", metadata.studio)
        self.assertEqual(u"https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-00.jpg@cropped",
                         metadata.posters.keys()[0])
        self.assertEqual(87, len(metadata.art))
        for i in range(0, len(metadata.art)):
            self.assertEqual(
                u"https://www.knights-visual.com/wp-content/uploads/2014/11/kv-094-{}.jpg".format(str(i + 1).zfill(2)),
                metadata.art.keys()[i])
        self.assertEqual(18, metadata.content_rating_age)
