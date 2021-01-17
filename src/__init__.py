import sentry_sdk

from agent import JavMovieAgent
from plex.agent import Agent
from plex.locale import Locale


# main agent code
class MainAgent(Agent.Movies):
    name = 'Jav Media'
    primary_provider = True
    languages = [
        Locale.Language.English,
        Locale.Language.Chinese,
        Locale.Language.Japanese]
    accepts_from = [
        'com.plexapp.agents.localmedia']
    contributes_to = [
        'com.nicholasworkshop.javplexagents',
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none']

    def __init__(self):
        super(Agent.Movies, self).__init__()  # noqa
        try:
            self.implementation = JavMovieAgent(self.name)
        except Exception as exception:
            sentry_sdk.capture_exception(exception)
            raise exception

    def search(self, results, media, lang, manual, primary):
        try:
            self.implementation.search(results, media, lang, manual, primary)
        except Exception as exception:
            sentry_sdk.capture_exception(exception)
            raise exception

    def update(self, metadata, media, lang, force, child_guid, child_id, periodic, prefs):
        try:
            self.implementation.update(metadata, media, lang, force, child_guid, child_id, periodic, prefs)
        except Exception as exception:
            sentry_sdk.capture_exception(exception)
            raise exception
