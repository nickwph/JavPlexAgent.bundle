from datetime import datetime

import environments
import service_1pondo_api
import utility_image_helper

if environments.is_local_debugging:
    from framework.plex_proxy import Proxy
    from framework.plex_log import Log
    from framework.plex_metadata import Movie  # noqa: F401


def update(metadata):
    """
    :type metadata: Movie
    """
    if not metadata.id.startswith('1pon-'):
        return

    Log.Debug("metadata.id: {}".format(metadata.id))
    Log.Debug("metadata.title: {}".format(metadata.title))
    Log.Debug("metadata.year: {}".format(metadata.year))

    split = metadata.id[6:].split("@")
    product_id = split[0]
    part_number = split[1] if len(split) > 1 else None

    # query fanza api
    item = service_1pondo_api.get_by_id(product_id)
    part_text = " (Part {})".format(part_number) if part_number is not None else ""

    # fill in information
    metadata.title = "1PON-{}{}".format(item.movie_id, part_text)
    metadata.original_title = item.title
    metadata.year = item.year
    metadata.rating = item.avg_rating
    metadata.content_rating_age = 18
    metadata.content_rating = "Adult"
    metadata.originally_available_at = datetime.strptime(item.release, '%Y-%m-%d').date()
    metadata.summary = u"{}\n\n{}".format(item.title, item.desc)
    metadata.studio = "Caribbeancom"
    metadata.tagline = item.title

    # TODO: More details needed
    # metadata.countries = {"Japan"}
    # metadata.writers = {}
    # metadata.directors = {}
    # metadata.producers = {}

    # set up actress image
    metadata.roles.clear()
    for actress_id in item.actresses_list:
        actress = item.actresses_list[actress_id]
        Log.Info(u"Processing actress data: {}".format(actress.name_ja))
        role = metadata.roles.new()
        role.name = actress.name_ja
        role.photo = service_1pondo_api.get_actress_by_id(int(actress_id)).image_url

    # setting up genres
    metadata.genres.clear()
    for tag in item.uc_name:
        Log.Info(u"Adding tag as genre: {}".format(tag))
        metadata.genres.add(tag)
    for index, genre in enumerate(metadata.genres):
        Log.Debug(u"genres[{}]: {}".format(index, genre))

    # TODO
    # # setting up artworks
    # for key in metadata.art.keys():
    #     del metadata.art[key]
    # for index, image_url in enumerate(item.sample_image_urls):
    #     Log.Debug("artwork_urls[{}]: {}".format(index, image_url))
    #     metadata.art[image_url] = Proxy.Media(HTTP.Request(image_url))

    # setting up posters
    for key in metadata.posters.keys():
        del metadata.posters[key]
    poster = utility_image_helper.add_padding_to_image_as_poster(item.thumb_high)
    poster_data = utility_image_helper.convert_image_to_data(poster)
    poster_key = "{}@padded".format(item.thumb_high)
    metadata.posters[poster_key] = Proxy.Media(poster_data)
