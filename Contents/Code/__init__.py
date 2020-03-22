from abc import abstractmethod

if False:
    from .framework.agent import Agent, ObjectContainer, Media
    from .framework.log import Log


# noinspection PyPep8Naming
def Start():
    Log.error("Start")
    return


class JavAgent(Agent.TV_Shows):

    @abstractmethod
    def search(self, results: ObjectContainer, media: Media, lang: str, manual: bool):
        pass

    @abstractmethod
    def update(self, metadata, media: Media, lang: str, force: bool):
        pass
