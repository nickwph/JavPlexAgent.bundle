import datetime

import environments
import fanza_api
import ideapocket_api
import image_helper
import s1_api

if environments.is_local_debugging:
    from framework.plex_proxy import Proxy
    from framework.plex_http import HTTP
    from framework.plex_log import Log
    from framework.plex_metadata import Movie  # noqa: F401


def update(metadata):  # noqa: C901
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('fanza-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[6:].split("@")
    type, product_id = split[0].split("-")
    part_number = split[1] if len(split) > 1 else None

    # query fanza api
    body = fanza_api.get_dvd_product(product_id) if type == 'dvd' else fanza_api.get_digital_product(product_id)
    Log.Debug("body.result.status: {}".format(body.result.status))
    Log.Debug("body.result.total_count: {}".format(body.result.total_count))
    Log.Info("Found number of items: {}".format(body.result.total_count))

    # feed in information
    item = body.result['items'][0]  # type: fanza_api.Item
    summary = fanza_api.get_product_description(item.URL)
    date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
    part_text = " (Part {})".format(part_number) if part_number is not None else ""
    studio = item.iteminfo.maker[0]  # type: fanza_api.Item.ItemInfo.Info
    Log.Debug("item.product_id: {}".format(item.product_id))
    Log.Debug("studio.id: {}".format(studio.id))
    Log.Debug(u"studio.name: {}".format(studio.name))

    metadata.title = "{}{}".format(item.product_id.upper(), part_text)
    metadata.original_title = item.title
    metadata.year = date.year
    metadata.rating = float(item.review.average) if 'review' in item else 0.0
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = date
    metadata.summary = u"{}\n\n{}".format(item.title, summary)
    # metadata.countries = {"Japan"}
    # metadata.writers = {}
    # metadata.directors = {}
    # metadata.producers = {}
    metadata.studio = studio.name
    # metadata.tags = {}
    metadata.tagline = item.title

    # clean up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]

    # check posters from sample images, should have the highest resolution
    if image_helper.can_analyze_images:
        for image_url in item.sampleImageURL.sample_s.image:
            image_url = image_url.replace("-", "jp-")
            Log.Info("Checking sample image: {}".format(image_url))
            if image_helper.are_similar(image_url, item.imageURL.small):
                Log.Info("Found a better poster from sample images: {}".format(image_url))
                metadata.posters[image_url] = Proxy.Media(HTTP.Request(image_url))
                break

    # check s1 posters, should have the high resolution
    if len(metadata.posters) == 0 and studio.id == s1_api.maker_id:
        Log.Info("Checking if there is a poster from S1 website")
        s1_id = s1_api.convert_product_id_from_digital_to_dvd(product_id) if type == 'digital' else product_id
        poster_url = s1_api.get_product_image(s1_id)
        if poster_url is not None:
            Log.Info("Using poster URL from S1 website: {}".format(poster_url))
            metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    # check pocket idea posters, should have the high resolution
    if len(metadata.posters) == 0 and studio.id == ideapocket_api.maker_id:
        Log.Info("Checking if there is a poster from Idea Pocket website")
        product_id_for_studio = ideapocket_api.convert_product_id_from_digital_to_dvd(product_id) if type == 'digital' \
            else product_id
        poster_url = ideapocket_api.get_product_image(product_id_for_studio)
        if poster_url is not None:
            Log.Info("Using poster URL from Idea Pocket website: {}".format(poster_url))
            metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    # try to crop poster out from cover, should have the medium resolution
    if len(metadata.posters) == 0:
        Log.Info("Checking if a poster can be cropped out from cover image")
        cover_url = item.imageURL.large
        small_poster_url = item.imageURL.small
        poster_data = image_helper.crop_poster_data_from_cover_if_similar_to_small_poster(cover_url, small_poster_url)
        if poster_data is not None:
            poster_key = "{}@cropped".format(cover_url)
            Log.Info("Using cropped poster from cover url: {}".format(cover_url))
            Log.Info("New poster key: {}".format(poster_key))
            metadata.posters[poster_key] = Proxy.Media(poster_data)

    # use small poster if no options, even it is low resolution
    if len(metadata.posters) == 0:
        Log.Info("No higher resolution poster can be used, using the lowest one")
        poster_url = item.imageURL.small
        Log.Debug("Small poster URL: {}".format(poster_url))
        metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    for actress in item.iteminfo.actress:  # type: fanza_api.Item.ItemInfo.Info
        role = metadata.roles.new()
        role.name = actress.name
        # role.photo

    # setting up artworks
    for key in metadata.art.keys():
        del metadata.art[key]
    for index, image_url in enumerate(item.sampleImageURL.sample_s.image):
        image_url = image_url.replace("-", "jp-")
        Log.Debug("artwork_urls[{}]: {}".format(index, image_url))
        metadata.art[image_url] = Proxy.Media(HTTP.Request(image_url))

