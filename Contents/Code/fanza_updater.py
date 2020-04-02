import datetime

import environments
import fanza_api
import image_helper
import s1_api

if environments.is_local_debugging:
    from framework.plex_proxy import Proxy
    from framework.plex_http import HTTP
    from framework.plex_log import Log
    from framework.plex_proxy import Proxy


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
    body = fanza_api.get_item(id)
    Log.Debug("body.result.status: {}".format(body.result.status))
    Log.Debug("body.result.total_count: {}".format(body.result.status))
    Log.Debug("body.result['items'][0].content_id: {}".format(body.result['items'][0].content_id))
    Log.Info("Found number of items: {}".format(body.result.total_count))

    # feed in information
    item = body.result['items'][0]  # type: fanza_api.Item
    summary = fanza_api.get_product_description(item.URL)
    date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
    metadata.title = fanza_api.denormalize(item.content_id).upper()
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
    part = image_helper.extract_part_number_from_filename(filename)
    if part:
        Log.Debug("part: {}".format(part))
        metadata.id = "{}-{}".format(item.content_id, part)
        metadata.title = "{} (Part {})".format(item.content_id.upper(), part)
        Log.Debug("new metadata.id: {}".format(metadata.id))
        Log.Debug("new metadata.title: {}".format(metadata.title))

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    if item.iteminfo.maker[0].id == s1_api.maker_id:
        poster_url = s1_api.get_product_image(item.product_id)
        Log.Debug("poster_url: {}".format(poster_url))
        metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))
    if len(metadata.posters) == 0:
        for image_url in item.sampleImageURL.sample_s.image:
            image_url = image_url.replace("-", "jp-")
            Log.Debug("Checking image: {}".format(image_url))
            content_type, width, height = image_helper.get_image_info_from_url(image_url)
            Log.Debug("> width: {}, height: {}".format(width, height))
            if image_helper.are_similar(image_url, item.imageURL.small):
                Log.Debug("Found a better poster!")
                Log.Debug("poster_url: {}".format(image_url))
                metadata.posters[image_url] = Proxy.Media(HTTP.Request(image_url))
                break
    if len(metadata.posters) == 0:
        poster_url = item.imageURL.small
        Log.Debug("poster_url: {}".format(poster_url))
        metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    for actress in item.iteminfo.actress:  # type: fanza_api.Item.ItemInfo.Info
        role = metadata.roles.new()
        role.name = actress.name
        # role.photo

    # setting up artworks
    # for key in metadata.art.keys(): del metadata.art[key]
    # for key in item.sampleImageUrl.sample_s:
    #     del metadata.art[key]
    # # poster_url = item.imageURL.small
    # # Log.Debug("poster_url: {}".format(poster_url))
    # metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))
