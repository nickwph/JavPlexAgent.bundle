import platform
import socket
import sys
from uuid import uuid4

import sentry_sdk
from sentry_sdk import utils as sentry_utils

from plex.agent import Agent
from plex.dict import Dict
from plex.locale import Locale
from plex.log import Log
from plex.platform import Platform

# to be injected by build script
version = '0.0.0'
git_hash = '000000'
build_number = 'local'
build_datetime = '00000000000000'
environment = 'debug'

# retrieve or generate unique user_id
if 'user_id' not in Dict or build_number == 'local':
    Dict['user_id'] = str(uuid4().hex)
    Dict.Save()
user_id = Dict['user_id']

# initialize sentry
sentry_sdk.init(
    dsn="https://331eb7edb13b4011a21b86ff4c956c7b@o148305.ingest.sentry.io/5574876",
    environment=environment,
    traces_sample_rate=1.0,
    debug=True,
    release="{}-{}-{}".format(version, build_number, git_hash))
sentry_utils.MAX_STRING_LENGTH = 4096
sentry_sdk.set_user({'id': user_id, "email": socket.gethostname(), 'hostname': socket.gethostname()})
sentry_sdk.set_tag("version", version)
sentry_sdk.set_tag("git_hash", git_hash)
sentry_sdk.set_tag("build_number", build_number)
sentry_sdk.set_tag("build_datetime", build_datetime)
sentry_sdk.set_tag("plex_version", Platform.ServerVersion)
if platform.system().lower() == 'darwin':
    sentry_sdk.set_context('os', {'name': "macOS", 'version': platform.mac_ver()[0]})
elif platform.system().lower() == 'linux':
    linux_distribution = platform.linux_distribution()
    sentry_sdk.set_context('os', {'name': linux_distribution[0], 'version': linux_distribution[1]})
elif platform.system().lower() == 'darwin':
    sentry_sdk.set_context('os', {'name': "Windows", 'version': platform.win32_ver()[0]})


def Start():
    Log.Info("Starting plug-in")
    Log.Debug("user_id: {}".format(user_id))
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
    for i, path in enumerate(sys.path):
        Log.Debug("sys.path[{}]: {}".format(i, path))


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
            from agent import JavMovieAgent
            self.implementation = JavMovieAgent()
            Log.Debug("name: {}".format(self.name))
        except Exception as exception:
            sentry_sdk.capture_exception(exception)

    def search(self, results, media, lang, manual, primary):
        try: self.implementation.search(results, media, lang, manual, primary)
        except Exception as exception: sentry_sdk.capture_exception(exception)

    def update(self, metadata, media, lang, force, child_guid, child_id, periodic, prefs):
        try: self.implementation.update(metadata, media, lang, force, child_guid, child_id, periodic, prefs)
        except Exception as exception: sentry_sdk.capture_exception(exception)
