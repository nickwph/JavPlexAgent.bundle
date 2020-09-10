import service_caribbeancom_api
import utility_image_helper
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
    item = service_caribbeancom_api.get_item(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "CARIB-{}{}".format(item.id, part_text)
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

    # set up actress image
    metadata.roles.clear()
    Log.Info(u"Processing actress data: {}".format(item.actor_name))
    role = metadata.roles.new()
    role.name = item.actor_name
    if utility_image_helper.does_image_exist(item.actor_large_picture_url):
        role.photo = item.actor_large_picture_url
    else:
        role.photo = item.actor_small_picture_url

    # setting up genres
    metadata.genres.clear()
    for genre in item.genres:
        Log.Info(u"Adding genre: {}".format(genre.name))
        metadata.genres.add(genre.name)
    for tag in item.tags:
        Log.Info(u"Adding tag as genre: {}".format(tag.name))
        metadata.genres.add(tag.name)
    for index, genre in enumerate(metadata.genres):
        Log.Debug(u"genres[{}]: {}".format(index, genre))

    # setting up artworks
    for key in metadata.art.keys():
        del metadata.art[key]
    for index, image_url in enumerate(item.sample_image_urls):
        Log.Debug("artwork_urls[{}]: {}".format(index, image_url))
        metadata.art[image_url] = Proxy.Media(HTTP.Request(image_url))

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    poster_url = None  # type: str
    if utility_image_helper.does_image_exist(item.poster_url):
        Log.Debug("Got a decent poster: {}".format(item.poster_url))
        poster_url = item.poster_url
    if poster_url is None:
        Log.Debug("No decent poster available, using banner as poster")
        Log.Debug("Poster image: {}".format(item.background_url))
        poster_url = item.background_url
    poster = utility_image_helper.add_padding_to_image_as_poster(poster_url)
    poster_data = utility_image_helper.convert_image_to_data(poster)
    poster_key = "{}@padded".format(poster_url)
    metadata.posters[poster_key] = Proxy.Media(poster_data)
