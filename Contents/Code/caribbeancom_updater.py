import caribbeancom_api
import environments

if environments.is_local_debugging:
    from framework.plex_proxy import Proxy
    from framework.plex_http import HTTP
    from framework.plex_log import Log
    from framework.plex_metadata import Movie  # noqa: F401


def update(metadata):
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('carib-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[6:].split("@")
    product_id = split[0]
    part_number = split[1] if len(split) > 1 else None

    # query fanza api
    item = caribbeancom_api.get_item(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "Carib-{}{}".format(item.id, part_text)
    metadata.original_title = item.title
    metadata.year = item.upload_date.year
    metadata.rating = float(item.rating)
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = item.upload_date
    metadata.summary = u"{}\n\n{}".format(item.title, item.description)
    metadata.studio = "Caribbeancom"
    metadata.tagline = item.title

    # TODO: More details needed
    # metadata.countries = {"Japan"}
    # metadata.writers = {}
    # metadata.directors = {}
    # metadata.producers = {}

    # setting up tags
    metadata.tags.clear()
    for tag in item.tags:
        metadata.tags.add(tag)

    # setting up genres
    metadata.genres.clear()
    for genre in item.genres:
        metadata.genres.add(genre)

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    poster_url = item.poster_url
    Log.Debug("poster_url: {}".format(poster_url))
    metadata.posters[poster_url] = Proxy.Media(HTTP.Request(poster_url))

    # setting up artworks
    for key in metadata.art.keys():
        del metadata.art[key]
    for index, image_url in enumerate(item.sample_image_urls):
        Log.Debug("artwork_urls[{}]: {}".format(index, image_url))
        metadata.art[image_url] = Proxy.Media(HTTP.Request(image_url))
