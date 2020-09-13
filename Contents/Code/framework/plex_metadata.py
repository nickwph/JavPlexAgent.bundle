from collections import OrderedDict, Set, MutableSet
from datetime import date

from typing import List, Any

from plex_proxy import Proxy


class Role(object):
    name = "Stub"
    photo = "Stub"


class RoleList(list):

    def new(self):
        role = Role()
        list.append(self, role)
        return role

    def clear(self):
        del self[:]


class Movie(object):
    """
    Represents a movie (e.g. a theatrical release, independent film, home movie, etc.)

    <Framework.api.agentkit.MediaTree object> from logging.
    """
    id = "Stub"
    genres = set()  # type: MutableSet[str]
    tags = set()  # type: MutableSet[str]
    collections = []  # Stub
    duration = 0  # Stub
    rating = 0.0  # Stub
    original_title = "Stub"
    title = "Stub"
    year = 0  # Stub
    originally_available_at = date.today()  # type: date # Stub
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
    posters = OrderedDict({"Stub": Proxy()})  # Stub
    art = OrderedDict({"Stub": Proxy()})  # Stub
    themes = OrderedDict({"Stub": Proxy()})  # Stub
