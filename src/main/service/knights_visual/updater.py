import api
from plex_http import HTTP
from plex_log import Log
from plex_metadata import Movie  # noqa: F401
from plex_proxy import Proxy
from utility import image_helper


def update(metadata):
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('knights-visual-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[15:].split("@")
    product_id = split[0]
    part_number = split[1] if len(split) > 1 else None

    # query fanza api
    item = api.get_by_id(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "{}{}".format(item.id.replace("-", ""), part_text)
    metadata.original_title = item.title
    metadata.year = item.upload_date.year
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = item.upload_date
    metadata.summary = u"{}\n\n{}".format(item.title, item.description)
    metadata.studio = "Knights Visual"
    metadata.tagline = item.title

    # TODO: More details needed
    # metadata.rating = float(item.rating)
    # metadata.countries = {"Japan"}
    # metadata.writers = {}
    # metadata.directors = {}
    # metadata.producers = {}
    # metadata.tags = {}
    # metadata.genres = {}

    # clean up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]

    # try to crop poster out from cover, should have the medium resolution
    if len(metadata.posters) == 0:
        Log.Info("Checking if a poster can be cropped out from cover image")
        cover_url = item.cover_url
        small_poster_url = item.poster_url
        poster_data = image_helper.crop_poster_data_from_cover_if_similar_to_small_poster(cover_url,
                                                                                          small_poster_url)
        if poster_data is not None:
            poster_key = "{}@cropped".format(cover_url)
            Log.Info("Using cropped poster from cover url: {}".format(cover_url))
            Log.Info("New poster key: {}".format(poster_key))
            metadata.posters[poster_key] = Proxy.Media(poster_data)

    # use small poster if no options, even it is low resolution
    if len(metadata.posters) == 0:
        Log.Info("No higher resolution poster can be used, using the lowest one")
        poster_url = item.poster_url
        Log.Debug("Small poster URL: {}".format(poster_url))
        metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    # setting up artworks
    for key in metadata.art.keys():
        del metadata.art[key]
    for index, image_url in enumerate(item.sample_image_urls):
        Log.Debug("artwork_urls[{}]: {}".format(index, image_url))
        metadata.art[image_url] = Proxy.Media(HTTP.Request(image_url))
