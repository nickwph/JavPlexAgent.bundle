# coding=utf-8
import json
from abc import abstractmethod

from plex_metadata import Movie


class MetadataSearchResult(Movie):
    id = "Stub"
    name = "Stub"
    year = 0  # Stub
    lang = "Stub"
    score = 0  # Stub
    thumb = "Stub"

    def __init__(self, id, name, year, lang, score, thumb):
        """
        :type id: str
        :type name: str | unicode
        :type year: int
        :type lang: str
        :type score: int
        :type thumb: str
        """
        self.id = id
        self.name = name
        self.year = year
        self.lang = lang
        self.score = score
        self.thumb = thumb

    def __str__(self):
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False, encoding='utf-8')


# noinspection PyUnresolvedReferences
class Agent(object):
    Movies = object  # type: Agent
    TV_Shows = object  # type: Agent
    Artist = object  # type: Agent
    Album = object  # type: Agent
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
        :param ObjectContainer[MetadataSearchResult] results: An empty container that the developer should populate with
               potential matches.
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
        :param Movie metadata: A pre-initialized metadata object if this is the first time the item is
               being updated, or the existing metadata object if the item is being refreshed.
        :param Media media: An object containing information about the media hierarchy in the database.
        :param str lang: A string identifying which language should be used for the metadata. This will be one of the
               constants defined in the agent’s languages attribute.
        :param bool force: A boolean value identifying whether the user forced a full refresh of the metadata. If this
               argument is True, all metadata should be refreshed, regardless of whether it has been populated
               previously.
        """
        pass
