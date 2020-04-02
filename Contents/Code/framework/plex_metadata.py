from datetime import date

from framework.plex_proxy import Proxy


class Role(object):
    name = "Stub"


class RoleList(list):

    def new(self):
        role = Role()
        list.append(self, role)
        return role


class Movie(object):
    """
    Represents a movie (e.g. a theatrical release, independent film, home movie, etc.)

    <Framework.api.agentkit.MediaTree object> from logging.
    """
    id = "Stub"
    genres = []  # Stub
    tags = []  # Stub
    collections = []  # Stub
    duration = 0  # Stub
    rating = 0.0  # Stub
    original_title = "Stub"
    title = "Stub"
    year = 0  # Stub
    originally_available_at = date.today()  # Stub
    studio = "Stub"
    tagline = "Stub"
    summary = "Stub"
    trivia = "Stub"
    quotes = "Stub"
    content_rating = "Stub"
    content_rating_age = 0  # Stub
    writers = {"Stub"}
    directors = {"Stub"}
    producers = {"Stub"}
    countries = {"Stub"}
    roles = RoleList()  # Stub
    posters = {"Stub": Proxy()}  # Stub
    art = {"Stub": Proxy()}  # Stub
    themes = {"Stub": Proxy()}  # Stub
