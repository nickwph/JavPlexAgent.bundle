import api
from plex.http import HTTP
from plex.log import Log
from plex.proxy import Proxy
from plex.metadata import Movie  # noqa
from utility import image_helper


def update(metadata):
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('s-cute-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[7:].split("@")
    product_id = split[0]
    part_number = split[1] if len(split) > 1 else None

    # query s-cute api
    item = api.get_by_id(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "S-CUTE-{}{}".format(item.id.upper(), part_text)
    metadata.original_title = item.title
    metadata.year = item.release_date.year
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = item.release_date
    metadata.summary = u"{}\n\n{}".format(item.title, item.description)
    metadata.studio = "S-Cute"
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

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    poster = image_helper.add_padding_to_image_as_poster(item.cover_url)
    poster_data = image_helper.convert_image_to_data(poster)
    poster_key = "{}@padded".format(item.cover_url)
    metadata.posters[poster_key] = Proxy.Media(poster_data)

    # setting up artworks
    max_artwork_count = 2  # TODO: make this configurable in preference
    Log.Debug("max_artwork_count: {}".format(max_artwork_count))
    for key in metadata.art.keys():
        del metadata.art[key]
    for index, photo in enumerate(item.photos):
        if index < max_artwork_count:
            Log.Debug("artwork_urls[{}]: {}".format(index, photo.image_url))
            metadata.art[photo.image_url] = Proxy.Media(HTTP.Request(photo.image_url))
        else:
            Log.Debug("artwork_urls (skipped): {}".format(photo.image_url))
