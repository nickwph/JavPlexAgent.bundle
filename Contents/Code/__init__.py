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
        Log.Error("=========== Search ==========")
        Log.Error("{} Version: {}".format(self.name, self.ver))
        Log.Error('Plex Server Version: {}'.format(Platform.ServerVersion))
        Log.Error("Searching results: {}".format(results))
        Log.Error("Searching media: {}".format(media))
        Log.Error("Searching lang: {}".format(lang))
        Log.Error("Searching manual: {}".format(manual))

        # query fanza api
        code = "ssni-558"
        response = FanzaApi.get_item_list(code)
        body = Munch.fromDict(response.json())
        Log.Error("body.result.status: {}".format(body.result.status))
        Log.Error("body.result.total_count: {}".format(body.result.status))
        Log.Error("body.result['items'][0].content_id: {}".format(body.result['items'][0].content_id))

        # items that we found and add them to the matchable list
        items = body.result['items']
        for item in items:
            date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
            score = SequenceMatcher(None, code, item.content_id).ratio() * 100
            result = MetadataSearchResult(id=item.content_id, name=item.title, year=date.year, lang="ja", score=score)
            results.Append(result)

        # all set
        Log.Error("Result results: {}".format(results))

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
