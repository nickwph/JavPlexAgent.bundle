from abc import abstractmethod, ABCMeta
from enum import Enum


class Language(Enum):
    English = 'English'


# noinspection PyPep8Naming
class Locale(Enum):
    Language = Language

    def Match(self):
        return


class ObjectContainer:
    view_group: str
    art: str
    title1: str


class MetadataSearchResult:
    id: str
    name: str
    year: int
    score: int
    lang: str


class MediaPart:
    file: str
    openSubtitlesHash: str


class Media:
    name: str
    filename: str
    primary_agent = None
    primary_metadata = None
    openSubtitlesHash = None
    year: int = None
    duration: int = None
    show: str
    season: str
    episode: int
    artist: str
    album: str
    track: str
    index: int
    items: ['Media']
    seasons: ['Media']
    episodes: ['Media']


class AgentBase(ABCMeta):
    name: str
    languages: []
    primary_provider: bool
    fallback_agent: str = None
    accepts_from: [str] = None
    contributes_to: [str] = None

    @abstractmethod
    def search(self, results: ObjectContainer, media: Media, lang: str, manual: bool):
        """
        When the media server needs an agent to perform a search, it calls the agent’s search method:
        :param results: An empty container that the developer should populate with potential matches.
        :param media: An object containing hints to be used when performing the search.
        :param lang: A string identifying the user’s currently selected language. This will be one of the constants
                     added to the agent’s languages attribute.
        :param manual: A boolean value identifying whether the search was issued automatically during scanning, or
                       manually by the user (in order to fix an incorrect match)
        """
        pass

    @abstractmethod
    def update(self, metadata, media: Media, lang: str, force: bool):
        """
        Once an item has been successfully matched, it is added to the update queue. As the framework processes queued
        items, it calls the update method of the relevant agents.
        :param metadata: A pre-initialized metadata object if this is the first time the item is being updated, or the
                         existing metadata object if the item is being refreshed.
        :param media: An object containing information about the media hierarchy in the database.
        :param lang: A string identifying which language should be used for the metadata. This will be one of the
                     constants defined in the agent’s languages attribute.
        :param force: A boolean value identifying whether the user forced a full refresh of the metadata. If this
                      argument is True, all metadata should be refreshed, regardless of whether it has been populated
                      previously.
        """
        pass


class Agent:
    Movies: AgentBase
    TV_Shows: AgentBase
    Artist: AgentBase
    Album: AgentBase
