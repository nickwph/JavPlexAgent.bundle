import datetime
from difflib import SequenceMatcher

from typing import List

from api_fanza import FanzaApi, Item
from environments import is_local_debugging
from utility import extract_part_number_from_filename, \
    get_image_info_from_url

if is_local_debugging:
    from framework.framework_proxy import Proxy
    from framework.framework_agent import MetadataSearchResult, ObjectContainer
    from framework.framework_http import HTTP
    from framework.framework_locale import Locale
    from framework.framework_log import Log
    from framework.framework_proxy import Proxy


# noinspection PyMethodMayBeStatic,DuplicatedCode
class FanzaController(object):

    @staticmethod
    def search(results, keyword):
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
            score = int(SequenceMatcher(None, FanzaApi.normalize(keyword), item.content_id).ratio() * 100)
            result = MetadataSearchResult(
                id="fanza-" + item.content_id,
                name="[{}] {}".format(item.content_id.upper(), item.title),
                year=date.year,
                lang=Locale.Language.Japanese,
                thumb=item.imageURL.small,
                score=score)
            results.Append(result)
            Log.Info("Added search result: {}".format(result))

    @staticmethod
    def update(metadata, media):
        if not metadata.id.startswith('fanza-'): return
        id = metadata.id[6:]

        # some debugging
        Log.Debug("id: {}".format(id))
        Log.Debug("metadata.id: {}".format(metadata.id))
        Log.Debug("metadata.title: {}".format(metadata.title))
        Log.Debug("metadata.year: {}".format(metadata.year))
        Log.Debug("media.id: {}".format(media.id))
        Log.Debug('media.items[0].parts[0].file: {}'.format(media.items[0].parts[0].file))

        # query fanza api
        body = FanzaApi.get_item(id)
        Log.Debug("body.result.status: {}".format(body.result.status))
        Log.Debug("body.result.total_count: {}".format(body.result.status))
        Log.Debug("body.result['items'][0].content_id: {}".format(body.result['items'][0].content_id))
        Log.Info("Found number of items: {}".format(body.result.total_count))

        # feed in information
        item = body.result['items'][0]  # type: Item
        summary = FanzaApi.get_product_description(item.URL)
        date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
        metadata.title = item.content_id.upper()
        metadata.original_title = item.title
        metadata.year = date.year
        metadata.rating = float(item.review.average)
        metadata.content_rating_age = 18
        metadata.content_rating = "Adult"
        metadata.originally_available_at = date
        metadata.summary = "{}\n\n{}".format(item.title, summary)
        # metadata.countries = {"Japan"}
        # metadata.writers = {}
        # metadata.directors = {}
        # metadata.producers = {}
        metadata.studio = "??"
        # metadata.tags = {}
        metadata.tagline = "??"

        # adding part number
        filename = media.items[0].parts[0].file
        part = extract_part_number_from_filename(filename)
        if part:
            Log.Debug("part: {}".format(part))
        metadata.id = "{}-{}".format(item.content_id, part)
        metadata.title = "{} (Part {})".format(item.content_id, part)
        Log.Debug("new metadata.id: {}".format(metadata.id))
        Log.Debug("new metadata.title: {}".format(metadata.title))

        # setting up posters
        for key in metadata.posters.keys(): del metadata.posters[key]
        for image_url in item.sampleImageURL.sample_s.image:
            Log.Debug("checking image: {}".format(image_url))
            content_type, width, height = get_image_info_from_url(image_url)
            Log.Debug("> width: {}, height: {}".format(width, height))
            if height > width:
                Log.Debug("found a better poster!")
                Log.Debug("poster_url: {}".format(image_url))
                metadata.posters[image_url] = Proxy.Media(HTTP.Request(image_url))
                break
        if len(metadata.posters) == 0:
            poster_url = item.imageURL.small
            Log.Debug("poster_url: {}".format(poster_url))
            metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

        # setting up artworks
        # for key in metadata.art.keys(): del metadata.art[key]
        # for key in item.sampleImageUrl.sample_s:
        #     del metadata.art[key]
        # # poster_url = item.imageURL.small
        # # Log.Debug("poster_url: {}".format(poster_url))
        # metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))
