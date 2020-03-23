# coding=utf-8
from abc import abstractmethod


class Language(object):
    English = 'Stub'  # type = "Stub"


# noinspection PyPep8Naming
class Locale(object):
    Language = Language

    def Match(self):
        return


# noinspection PyShadowingBuiltins
class MetadataSearchResult:
    id = "Stub"
    name = "Stub"
    year = 0  # Stub
    lang = "Stub"
    score = 0  # Stub

    def __init__(self, id, name, year, lang, score):
        """
        :type id: str
        :type name: str
        :type year: int
        :type lang: str
        :type score: int
        """
        self.id = id
        self.name = name
        self.year = year
        self.lang = lang
        self.score = score


# noinspection PyPep8Naming,PyUnresolvedReferences
class ObjectContainer(object):
    view_group = "Stub"
    art = "Stub"
    title1 = "Stub"
    title2 = "Stub"
    noHistory = False  # Stub
    replaceParent = False  # Stub

    def Append(self, result):
        """
        :param result: MetadataSearchResult
        """
        pass


class MediaContainer(ObjectContainer):  # class name I got from debug loggings
    pass


# noinspection PyUnresolvedReferences
class Agent(object):
    Movies = Agent  # Stub
    TV_Shows = Agent  # Stub
    Artist = Agent  # Stub
    Album = Agent  # Stub
    name = "Stub"
    languages = []  # Stub
    primary_provider = False  # Stub
    fallback_agent = "Stub"
    accepts_from = []  # Stub
    contributes_to = []  # Stub

    @abstractmethod
    def search(self, results, media, lang, manual):
        """
        When the media server needs an agent to perform a search, it calls the agent’s search method:
        :param ObjectContainer results: An empty container that the developer should populate with potential matches.
        :param Media media: An object containing hints to be used when performing the search.
        :param str lang: A string identifying the user’s currently selected language. This will be one of the constants
               added to the agent’s languages attribute.
        :param bool manual: A boolean value identifying whether the search was issued automatically during scanning, or
               manually by the user (in order to fix an incorrect match)
        """
        pass

    @abstractmethod
    def update(self, metadata, media, lang, force):
        """
        Once an item has been successfully matched, it is added to the update queue. As the framework processes queued
        items, it calls the update method of the relevant agents.
        :param MetadataSearchResult metadata: A pre-initialized metadata object if this is the first time the item is
               being updated, or the existing metadata object if the item is being refreshed.
        :param Media media: An object containing information about the media hierarchy in the database.
        :param str lang: A string identifying which language should be used for the metadata. This will be one of the
               constants defined in the agent’s languages attribute.
        :param bool force: A boolean value identifying whether the user forced a full refresh of the metadata. If this
               argument is True, all metadata should be refreshed, regardless of whether it has been populated
               previously.
        """
        pass
