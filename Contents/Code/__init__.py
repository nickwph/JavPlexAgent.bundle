import datetime
import os
import re
import urllib
from compiler.ast import List
from difflib import SequenceMatcher

from api_fanza import FanzaApi, Item
from environments import is_local_debugging

if is_local_debugging:
    from framework_agent import Agent, MetadataSearchResult, ObjectContainer
    from framework_http import HTTP
    from framework_locale import Locale
    from framework_log import Log
    from framework_media import Media
    from framework_metadata import Movie
    from framework_platform import Platform
    from framework_proxy import Proxy


# noinspection PyPep8Naming
def Start():
    Log.Error("=========== Start ==========")


# noinspection PyMethodMayBeStatic,DuplicatedCode
class JavMovieAgent(Agent.Movies):
    name = 'Jav Media'
    ver = '1.0.0'
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
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none'
    ]

    def __init__(self):
        """
        This is where everything starts.
        """
        super(Agent.Movies, self).__init__()
        Log.Error("=========== Init ==========")
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
        Log.Debug("media.filename: {}".format(urllib.unquote(media.filename)))

        # generating keywords from directory and filename
        filename = urllib.unquote(media.filename)
        directory = os.path.basename(os.path.dirname(filename))
        filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
        filename_without_ext_and_part = re.sub(r"-Part\d+$", "", filename_without_ext, 0, re.MULTILINE | re.IGNORECASE)
        Log.Debug("directory: {}".format(directory))
        Log.Debug("filename_without_ext: {}".format(filename_without_ext))
        Log.Debug("filename_without_ext_and_part: {}".format(filename_without_ext_and_part))

        # query fanza api with keywords
        self.search_with_keyword(results, directory)
        self.search_with_keyword(results, filename_without_ext_and_part)
        Log.Error("Searching is done")

    def search_with_keyword(self, results, keyword):
        """
        :type results: ObjectContainer
        :type keyword: str
        """
        Log.Info("Search item with keyword: {}".format(keyword))
        body = FanzaApi.search_item(keyword)
        Log.Info("Found number of items: {}".format(body.result.total_count))

        # some more debugging
        Log.Debug("body.result.status: {}".format(body.result.status))
        Log.Debug("body.result.total_count: {}".format(body.result.status))

        # items that we found and add them to the matchable list
        items = body.result['items']  # type: List[Item]
        for i, item in enumerate(items):
            Log.Debug("body.result['items'][{}].content_id: {}".format(i, item.content_id))
            Log.Debug("body.result['items'][{}].product_id: {}".format(i, item.product_id))
            date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
            score = int(SequenceMatcher(None, keyword, item.content_id).ratio() * 100)
            result = MetadataSearchResult(
                id=item.content_id,
                name="[{}] {}".format(item.content_id.upper(), item.title),
                year=date.year,
                lang=Locale.Language.Japanese,
                score=score)
            results.Append(result)
            Log.Info("Added search result: {}".format(result))

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

        # some debugging
        Log.Debug("metadata.id: {}".format(metadata.id))
        Log.Debug("metadata.title: {}".format(metadata.title))
        Log.Debug("metadata.year: {}".format(metadata.year))
        Log.Debug("media.id: {}".format(media.id))
        # Log.Debug("media.name: {}".format(media.name))
        # Log.Debug("media.year: {}".format(media.year))

        # query fanza api
        body = FanzaApi.get_item(metadata.id)
        Log.Debug("body.result.status: {}".format(body.result.status))
        Log.Debug("body.result.total_count: {}".format(body.result.status))
        Log.Debug("body.result['items'][0].content_id: {}".format(body.result['items'][0].content_id))
        Log.Info("Found number of items: {}".format(body.result.total_count))

        # feed in information
        item = body.result['items'][0]  # type: Item
        date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
        metadata.title = item.content_id.upper()
        metadata.original_title = item.title
        metadata.year = date.year
        metadata.rating = float(item.review.average)

        path1 = media.items[0].parts[0].file
        Log.Debug('media file: {name}'.format(name=path1))

        folder_path = os.path.dirname(path1)
        Log.Debug('folder path: {name}'.format(name=folder_path))

        Log.Debug('folder path: {name}'.format(name=folder_path))
        metadata.posters[1] = Proxy.Media(HTTP.Request(item.imageURL.list))
        metadata.posters[2] = Proxy.Media(HTTP.Request(item.imageURL.large))
        metadata.posters[3] = Proxy.Media(HTTP.Request(item.imageURL.small))

        metadata.content_rating_age = 18
        metadata.content_rating = "Adult"
        metadata.originally_available_at = date
