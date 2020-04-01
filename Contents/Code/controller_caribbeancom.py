import caribbeancom_api
from environments import is_local_debugging

if is_local_debugging:
    from framework.framework_proxy import Proxy
    from framework.framework_agent import MetadataSearchResult, ObjectContainer
    from framework.framework_http import HTTP
    from framework.framework_locale import Locale
    from framework.framework_log import Log
    from framework.framework_proxy import Proxy


# noinspection PyMethodMayBeStatic,DuplicatedCode
class CaribbeancomController(object):

    @staticmethod
    def search(results, keyword):
        """
        :type results: ObjectContainer
        :type keyword: str
        """
        id = caribbeancom_api.extract_id(keyword)
        if id is None: return

        Log.Info("Search item with keyword: {}".format(id))
        item = caribbeancom_api.get_item(id)
        result = MetadataSearchResult(
            id="carib-" + item.id,
            name="{} {}".format(id, item.title),
            year=item.upload_date.year,
            lang=Locale.Language.Japanese,
            thumb=item.poster_url,
            score=100)
        results.Append(result)
        Log.Info("Added search result: {}".format(result))

    @staticmethod
    def update(metadata, media):
        if not metadata.id.startswith('carib-'): return
        id = metadata.id[6:]

        # some debugging
        Log.Debug("id: {}".format(id))
        Log.Debug("metadata.id: {}".format(metadata.id))
        Log.Debug("metadata.title: {}".format(metadata.title))
        Log.Debug("metadata.year: {}".format(metadata.year))
        Log.Debug("media.id: {}".format(media.id))
        Log.Debug('media.items[0].parts[0].file: {}'.format(media.items[0].parts[0].file))

        # query fanza api
        item = caribbeancom_api.get_item(id)

        # feed in information
        metadata.title = "Carib-" + item.id
        metadata.original_title = item.title
        metadata.year = item.upload_date.year
        metadata.rating = float(item.rating)
        metadata.content_rating_age = 18
        metadata.content_rating = "Adult"
        metadata.originally_available_at = item.upload_date
        metadata.summary = "{}\n\n{}".format(item.title, item.description)
        # metadata.countries = {"Japan"}
        # metadata.writers = {}
        # metadata.directors = {}
        # metadata.producers = {}
        metadata.studio = "Caribbeancom"
        # metadata.tags = {}
        metadata.tagline = "??"

        # # adding part number
        # filename = media.items[0].parts[0].file
        # part = extract_part_number_from_filename(filename)
        # if part:
        #     Log.Debug("part: {}".format(part))
        # metadata.id = "{}-{}".format(item.content_id, part)
        # metadata.title = "{} (Part {})".format(item.content_id, part)
        # Log.Debug("new metadata.id: {}".format(metadata.id))
        # Log.Debug("new metadata.title: {}".format(metadata.title))

        # setting up posters
        for key in metadata.posters.keys(): del metadata.posters[key]
        poster_url = item.poster_url
        Log.Debug("poster_url: {}".format(poster_url))
        metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))
        # metadata.posters[2] = Proxy.Media(HTTP.Request(item.imageURL.large))
        # metadata.posters[3] = Proxy.Media(HTTP.Request(item.imageURL.small))

        # setting up artworks
        # for key in metadata.art.keys(): del metadata.art[key]
        # for key in item.sampleImageUrl.sample_s:
        #     del metadata.art[key]
        # # poster_url = item.imageURL.small
        # # Log.Debug("poster_url: {}".format(poster_url))
        # metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))
