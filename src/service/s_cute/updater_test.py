# coding=utf-8
from unittest import TestCase

from plex.metadata import Movie
import updater


class Test(TestCase):

    def test_update___actual_run(self):
        metadata = Movie()
        metadata.id = "s-cute-734_reona_01"
        updater.update(metadata)
        self.assertEqual(u"s-cute-734_reona_01", metadata.id)
        self.assertEqual(u"S-CUTE-734_REONA_01", metadata.title)
        self.assertEqual(u'上品な仕草がエッチな美女とSEX／Reona', metadata.original_title)
        self.assertEqual(u'上品な仕草がエッチな美女とSEX／Reona', metadata.tagline)
        self.assertEqual(u'上品な仕草がエッチな美女とSEX／Reona\n\n美人でちょっぴりシャイな一面もある'
                         u'Reonaちゃん。照れては目を逸らすのに、男性の服を脱がすのは早かったりと、照れ'
                         u'屋なのに積極的で目が離せません。はにかみながらも情熱的に絡み合う綺麗な裸体に'
                         u'見蕩れてしまうセックスです。', metadata.summary)
        self.assertEqual(u"Adult", metadata.content_rating)
        self.assertEqual(u"S-Cute", metadata.studio)
        self.assertEqual(u"http://static.s-cute.com/images/734_reona/734_reona_01/734_reona_01.jpg@padded", metadata.posters.keys()[0])
        self.assertEqual(2, len(metadata.art))
        for i in range(0, len(metadata.art)):
            art_url = u"http://photos.s-cute.com/130901/sample/contents/734_reona/734_reona_01/{}.jpg".format(str(i + 1).zfill(3))
            self.assertEqual(art_url, metadata.art.keys()[i])
        self.assertEqual(18, metadata.content_rating_age)
