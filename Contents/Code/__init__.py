import datetime
import json

from munch import Munch

from api_fanza import FanzaApi
from environments import is_local_debugging
from difflib import SequenceMatcher

if is_local_debugging:
    from framework_agent import Agent, Media, Locale, MetadataSearchResult, MediaContainer
    from framework_log import Log
    from framework_platform import Platform


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
        This is called when you click on "fix match" button in Plex.
        :type results: MediaContainer
        :type media: Media
        :type lang: str
        :type manual: bool
        :return:
        """

        # some basic info
        Log.Info("=========== Search ==========")
        Log.Info("{} Version: {}".format(self.name, self.ver))
        Log.Info('Plex Server Version: {}'.format(Platform.ServerVersion))
        Log.Info("Searching results: {}".format(results))
        Log.Info("Searching media: {}".format(media))
        Log.Info("Searching lang: {}".format(lang))
        Log.Info("Searching manual: {}".format(manual))

        # query fanza api
        code = "ssni-558"
        response = FanzaApi.get_item_list(code)
        body = Munch.fromDict(response.json())
        Log.Debug("body.result.status: {}".format(body.result.status))
        Log.Debug("body.result.total_count: {}".format(body.result.status))
        Log.Debug("body.result['items'][0].content_id: {}".format(body.result['items'][0].content_id))
        Log.Info("Found number of items: {}".format(body.result.total_count))

        # items that we found and add them to the matchable list
        items = body.result['items']
        for item in items:
            date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
            score = int(SequenceMatcher(None, code, item.content_id).ratio() * 100)
            result = MetadataSearchResult(id=item.content_id, name=item.title, year=date.year, lang="ja", score=score)
            results.Append(result)
            Log.Info("Added search result: {}".format(result))

        # all set
        Log.Error("Searching is done")

    def update(self, metadata, media, lang, force):
        """
        :type metadata: MetadataSearchResult
        :type media: Media
        :type lang: str
        :type force: bool
        """

        # some basic info
        Log.Error("=========== Update ==========")
        Log.Error("Updating metadata: {}".format(metadata))
        Log.Error("Updating media: {}".format(media))
        Log.Error("Updating lang: {}".format(lang))
        Log.Error("Updating force: {}".format(force))
