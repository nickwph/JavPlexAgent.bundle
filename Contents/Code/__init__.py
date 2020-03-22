from abc import abstractmethod

if False:
    from .framework.agent import Agent, ObjectContainer, Media, Locale, MetadataSearchResult
    from .framework.log import Log


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

    def search(self, results, media, lang, manual):
        self.search_internal(results, media, lang, manual)

    # noinspection PyMethodMayBeStatic
    def search_internal(self, results: ObjectContainer, media: Media, lang: str, manual: bool):
        Log.Error("Search!!")
        Log.Error("Searching results: {}".format(results))
        Log.Error("Searching media: {}".format(vars(media)))
        Log.Error("Searching lang: {}".format(lang))
        Log.Error("Searching manual: {}".format(manual))
        results.Append(MetadataSearchResult(id=media.id, name=media.name, year=media.year, lang=lang, score=100))
        Log.Error("Result results: {}".format(results))
        pass

    def update(self, metadata, media, lang, force):
        self.update(metadata, media, lang, force)

    # noinspection PyMethodMayBeStatic
    def update_internal(self, metadata, media: Media, lang: str, force: bool):
        Log.Error("Update!!")
        Log.Error("Updating metadata: {}".format(metadata))
        Log.Error("Updating media: {}".format(vars(media)))
        Log.Error("Updating lang: {}".format(lang))
        Log.Error("Updating force: {}".format(force))
        pass
