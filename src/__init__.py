import platform
import sys

import sentry_sdk

from plex.agent import Agent
from plex.locale import Locale
from plex.log import Log
from plex.platform import Platform
from utility import sentry_helper
from utility import user_helper

# to be injected by build script
version = '0.0.0'
git_hash = '000000'
build_number = 'local'
build_datetime = '00000000000000'
environment = 'debug'
sentry_dsn = ''


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
            Log.Info("Initializing agent")
            user_id = user_helper.get_user_id()
            sentry_helper.init_sentry(sentry_dsn, user_id, version, git_hash, build_number, build_datetime, environment)
            from agent import JavMovieAgent
            self.implementation = JavMovieAgent()
            Log.Debug("name: {}".format(self.name))
            Log.Debug('user_id: {}'.format(user_id))
            Log.Debug('plex_version: {}'.format(Platform.ServerVersion))
            Log.Debug("version: {}".format(version))
            Log.Debug("git_hash: {}".format(git_hash))
            Log.Debug("build_number: {}".format(build_number))
            Log.Debug("build_datetime: {}".format(build_datetime))
            Log.Debug("environment: {}".format(environment))
            Log.Debug("sys.version: {}".format(sys.version.replace("\n", "")))
            Log.Debug("sys.version_info: {}".format(sys.version_info))
            Log.Debug("sys.platform: {}".format(sys.platform))
            Log.Debug("sys.executable: {}".format(sys.executable))
            Log.Debug("platform.system: {}".format(platform.system().lower()))
            Log.Debug("platform.mac_ver: {}".format(platform.mac_ver()))
            Log.Debug("platform.linux_distribution: {}".format(platform.linux_distribution()))
            Log.Debug("platform.win32_ver: {}".format(platform.win32_ver()))
            for i, path in enumerate(sys.path): Log.Debug("sys.path[{}]: {}".format(i, path))  # noqa
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
