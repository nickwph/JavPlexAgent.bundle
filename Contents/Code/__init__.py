"""
Very sad that I have to the old style comments for type checking.
"""

if False:
    from .framework.agent import Agent, ObjectContainer, Media, Locale, MetadataSearchResult
    from .framework.log import Log
    from .framework.platform import Platform


# noinspection PyPep8Naming
def Start():
    Log.Error("Start!!")
    return


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

    # noinspection PyMethodMayBeStatic
    def search(self, results, media, lang, manual):
        """
        :type results: MediaContainer
        :type media: Media
        :type lang: str
        :type manual: bool
        :return:
        """
        Log.Error("{} Version: {}".format(self.name, self.ver))
        Log.Error('Plex Server Version: {}'.format(Platform.ServerVersion))
        Log.Error("Search!!")
        Log.Error("Searching results: {}".format(results))
        Log.Error("Searching media: {}".format(media))
        Log.Error("Searching lang: {}".format(lang))
        Log.Error("Searching manual: {}".format(manual))
        results.Append(MetadataSearchResult(id=media.id, name=media.name, year=media.year, lang=lang, score=100))
        filename = media.filename
        Log.Error("Result results: {}".format(results))
        pass

    # noinspection PyMethodMayBeStatic
    def update(self, metadata, media, lang, force):
        """
        :type metadata: MetadataSearchResult
        :type media: Media
        :type lang: str
        :type force: bool
        """
        Log.Error("Update!!")
        Log.Error("Updating metadata: {}".format(metadata))
        Log.Error("Updating media: {}".format(media))
        Log.Error("Updating lang: {}".format(lang))
        Log.Error("Updating force: {}".format(force))
        pass
