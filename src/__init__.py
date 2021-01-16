import platform
import socket
import sys

import sentry_sdk

from plex.agent import Agent
from plex.locale import Locale
from plex.log import Log
from plex.platform import Platform
from utility import mixpanel_helper
from utility import sentry_helper
from utility import user_helper

# to be injected by build script
version = ''
git_hash = ''
build_number = ''
build_datetime = ''
environment = ''
sentry_dsn = ''
mixpanel_token = ''

# produce other system information
plex_version = Platform.ServerVersion
full_version = "{}-{}-{}-{}".format(version, build_number, git_hash, build_datetime)
hostname = socket.gethostname()
os_name = 'Unknown'
os_version = ''
if platform.system().lower() == 'darwin':
    os_name = 'macOS'
    os_version = platform.mac_ver()[0]
elif platform.system().lower() == 'linux':
    linux_distribution = platform.linux_distribution()
    os_name = linux_distribution[0]
    os_version = linux_distribution[1]
elif platform.system().lower() == 'windows':
    os_name = 'Windows'
    os_version = platform.win32_ver()[0]

# init user id and mixpanel
user_id = user_helper.get_user_id()
mixpanel_helper.initialize(mixpanel_token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version)
mixpanel_helper.track.test()
if user_helper.is_new_user_id:
    mixpanel_helper.track.main.installed()


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
            mixpanel_helper.track.main.init()
            sentry_helper.init_sentry(sentry_dsn, user_id, version, git_hash, build_number, build_datetime, environment, plex_version, os_name, os_version, hostname, full_version)
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
