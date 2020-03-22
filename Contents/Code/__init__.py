from abc import abstractmethod

if False:
    from .framework.agent import Agent, ObjectContainer, Media, Locale
    from .framework.log import Log


# noinspection PyPep8Naming
def Start():
    Log.error("Start")
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

    @abstractmethod
    def search(self, results: ObjectContainer, media: Media, lang: str, manual: bool):
        pass

    @abstractmethod
    def update(self, metadata, media: Media, lang: str, force: bool):
        pass
