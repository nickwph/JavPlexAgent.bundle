import os

from plex.agent import Agent
from plex.locale import Locale
from plex.log import Log
from plex.platform import Platform
from service._1pondo import searcher as _1pondo_searcher
from service._1pondo import updater as _1pondo_updater
from service.caribbeancom import searcher as  caribbeancom_searcher
from service.caribbeancom import updater  as caribbeancom_updater
from service.caribbeancom_pr import searcher as caribbeancom_pr_searcher
from service.caribbeancom_pr import updater  as caribbeancom_pr_updater
from service.fanza import searcher as  fanza_searcher
from service.fanza import updater  as fanza_updater
from service.heyzo import searcher as  heyzo_searcher
from service.heyzo import updater  as heyzo_updater
from service.knights_visual import searcher as  knights_visual_searcher
from service.knights_visual import updater  as knights_visual_updater
from utility import file_helper


# noinspection PyMethodMayBeStatic,DuplicatedCode
class JavMovieAgent(Agent.Movies):
    name = 'Jav Media'
    ver = '1.1.0'
    primary_provider = True
    languages = [  # must have the language of the system, other update() will not be called
        Locale.Language.English,
        Locale.Language.Chinese,
        Locale.Language.Japanese,
        Locale.Language.Korean,
        Locale.Language.French,
        Locale.Language.NoLanguage]
    accepts_from = [
        'com.plexapp.agents.localmedia',
        'com.plexapp.agents.opensubtitles',
        'com.plexapp.agents.podnapisi',
        'com.plexapp.agents.subzero'
    ]
    contributes_to = [
        'com.nicholasworkshop.javplexagents',
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none'
    ]

    def __init__(self):
        """
        This is where everything starts.
        """
        super(Agent.Movies, self).__init__()
        Log.Info("=========== Init ==========")
        Log.Info("{} Version: {}".format(self.name, self.ver))
        Log.Info('Plex Server Version: {}'.format(Platform.ServerVersion))

    def search(self, results, media, lang, manual):
        """
        This is called when you click on "fix match" button in Plex.

        :type results: ObjectContainer
        :type media: Media
        :type lang: str
        :type manual: bool
        :return:
        """
        Log.Info("=========== Search ==========")
        Log.Info("Searching results: {}".format(results))
        Log.Info("Searching media: {}".format(media))
        Log.Info("Searching lang: {}".format(lang))
        Log.Info("Searching manual: {}".format(manual))

        # some debugging
        Log.Debug("media.id: {}".format(media.id))
        Log.Debug("media.name: {}".format(media.name))
        Log.Debug("media.year: {}".format(media.year))
        Log.Debug("media.filename: {}".format(media.items[0].parts[0].file))

        # generating keywords from directory and filename
        filename = media.items[0].parts[0].file
        directory = os.path.basename(os.path.dirname(filename))
        product_id, part_number = file_helper.extract_product_id_and_part_number(filename)
        Log.Debug("directory: {}".format(directory))
        Log.Debug("product_id: {}".format(product_id))
        Log.Debug("part_number: {}".format(part_number))

        # query fanza api with keywords
        caribbeancom_searcher.search(results, part_number, directory)
        caribbeancom_searcher.search(results, part_number, product_id)
        caribbeancom_pr_searcher.search(results, part_number, directory)
        caribbeancom_pr_searcher.search(results, part_number, product_id)
        fanza_searcher.search(results, part_number, directory)
        fanza_searcher.search(results, part_number, product_id)
        knights_visual_searcher.search(results, part_number, directory)
        knights_visual_searcher.search(results, part_number, product_id)
        heyzo_searcher.search(results, part_number, directory)
        heyzo_searcher.search(results, part_number, product_id)
        _1pondo_searcher.search(results, part_number, directory)
        _1pondo_searcher.search(results, part_number, product_id)
        Log.Info("Searching is done")

    def update(self, metadata, media, lang, force):
        """
        :type metadata: Movie
        :type media: Media
        :type lang: str
        :type force: bool
        """
        Log.Info("=========== Update ==========")
        Log.Info("Updating metadata: {}".format(metadata))
        Log.Info("Updating media: {}".format(media))
        Log.Info("Updating lang: {}".format(lang))
        Log.Info("Updating force: {}".format(force))

        # actual updating
        caribbeancom_updater.update(metadata)
        caribbeancom_pr_updater.update(metadata)
        fanza_updater.update(metadata)
        knights_visual_updater.update(metadata)
        heyzo_updater.update(metadata)
        _1pondo_updater.update(metadata)
