from api.fanza import FanzaApi
from environments import is_local_debugging

if is_local_debugging:
    from .framework.agent import Agent, Media, Locale, MetadataSearchResult, MediaContainer
    from .framework.log import Log
    from .framework.platform import Platform


# noinspection PyPep8Naming
def Start():
    Log.Error("=========== Start ==========")


# noinspection PyMethodMayBeStatic
class JavAgent(Agent.TV_Shows):
    name = 'Jav Media'
    ver = '1.0.0'
    primary_provider = True
    languages = [Locale.Language.NoLanguage]
    accepts_from = [
        'com.plexapp.agents.localmedia',
        'com.plexapp.agents.opensubtitles',
        'com.plexapp.agents.podnapisi',
        'com.plexapp.agents.subzero'
    ]

    contributes_to = [
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none'
    ]

    def search(self, results, media, lang, manual):
        """
        :type results: MediaContainer
        :type media: Media
        :type lang: str
        :type manual: bool
        :return:
        """
        Log.Error("=========== Search ==========")
        Log.Error("{} Version: {}".format(self.name, self.ver))
        Log.Error('Plex Server Version: {}'.format(Platform.ServerVersion))
        Log.Error("Searching results: {}".format(results))
        Log.Error("Searching media: {}".format(media))
        Log.Error("Searching lang: {}".format(lang))
        Log.Error("Searching manual: {}".format(manual))

        # FanzaApi.get_item_list()

        results.Append(MetadataSearchResult(id="AAAAA", name="AAAAA", year=2020, lang=lang, score=100))
        results.Append(MetadataSearchResult(id="BBBBB", name="BBBBB", year=2020, lang=lang, score=100))

        Log.Error('media.filename: {}'.format(media.filename))
        Log.Error("Result results: {}".format(results))

    def update(self, metadata, media, lang, force):
        """
        :type metadata: MetadataSearchResult
        :type media: Media
        :type lang: str
        :type force: bool
        """
        Log.Error("=========== Update ==========")
        Log.Error("Updating metadata: {}".format(metadata))
        Log.Error("Updating media: {}".format(media))
        Log.Error("Updating lang: {}".format(lang))
        Log.Error("Updating force: {}".format(force))
