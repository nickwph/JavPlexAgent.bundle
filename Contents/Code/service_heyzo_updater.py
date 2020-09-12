import environments
import utility_image_helper
import service_heyzo_api

if environments.is_local_debugging:
    from framework.plex_proxy import Proxy
    from framework.plex_http import HTTP
    from framework.plex_log import Log
    from framework.plex_metadata import Movie  # noqa: F401


def update(metadata):
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('heyzo-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[6:].split("@")
    product_id = split[0]
    part_number = split[1] if len(split) > 1 else None

    # query fanza api
    item = service_heyzo_api.get_by_id(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "HEYZO-{}{}".format(item.id, part_text)
    metadata.original_title = item.title
    metadata.year = item.release_date.year
    metadata.rating = float(item.rating)
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = item.release_date
    metadata.summary = u"{}\n\n{}".format(item.title, item.description)
    metadata.studio = "Heyzo"
    metadata.tagline = item.title

    # TODO: More details needed
    # metadata.countries = {"Japan"}
    # metadata.writers = {}
    # metadata.directors = {}
    # metadata.producers = {}

    # set up actress image
    metadata.roles.clear()
    Log.Info(u"Processing actress data: {}".format(item.actress_name))
    role = metadata.roles.new()
    role.name = item.actress_name
    # role.photo = item.actress_picture_url

    picture = utility_image_helper.crop_square_from_top_left(item.actress_picture_url)
    picture_data = utility_image_helper.convert_image_to_data(picture)
    picture_key = "{}@padded".format(item.actress_picture_url)
    # metadata.posters[picture_key] = Proxy.Media(picture_data)
    role.photo = Proxy.Media(picture_data)

    # setting up genres
    metadata.genres.clear()
    for tag in item.tags:
        Log.Info(u"Adding tag as genre: {}".format(tag.name))
        metadata.genres.add(tag.name)
    for index, genre in enumerate(metadata.genres):
        Log.Debug(u"genres[{}]: {}".format(index, genre))

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    poster = utility_image_helper.add_padding_to_image_as_poster(item.cover_url)
    poster_data = utility_image_helper.convert_image_to_data(poster)
    poster_key = "{}@padded".format(item.cover_url)
    metadata.posters[poster_key] = Proxy.Media(poster_data)
