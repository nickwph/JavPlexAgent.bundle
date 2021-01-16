import datetime
import socket

from mixpanel import Mixpanel

from plex.log import Log

track = None  # type: Track


def initialize(token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version):
    global track
    if track is None: track = Track(token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version)  # noqa
    return track


class Track:

    def __init__(self, token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version):
        Log.Debug(token)
        self.mixpanel = MixpanelExtended(token)  # type: Mixpanel
        self.mixpanel.people_set(user_id, {'hostname': socket.gethostname()})
        self.user_id = user_id  # type: str
        self.main = Track.Main(self)
        self.agent = Track.Agent(self)
        self.version_info = {
            'version': version,
            'git_hash': git_hash,
            'build_number': build_number,
            'build_datetime': build_datetime,
            'environment': environment,
            'plex_version': plex_version,
            'os_name': os_name,
            'os_version': os_version,
            'hostname': hostname,
            'full_version': full_version,
        }

    class Main:

        def __init__(self, track):
            self.mixpanel = track.mixpanel  # type: Mixpanel
            self.user_id = track.user_id  # type: str
            self.track = track  # type: Track

        def installed(self):
            self.mixpanel.track(self.user_id, 'main-installed', self.track.version_info)
            self.mixpanel.people_append(self.user_id, self.track.version_info)
            self.mixpanel.people_append(self.user_id, {'first_seen_datetime': datetime.datetime.now()})

        def init(self):
            self.mixpanel.track(self.user_id, 'main-init', self.track.version_info)
            self.mixpanel.people_append(self.user_id, self.track.version_info)
            self.mixpanel.people_append(self.user_id, {'last_seen_datetime': datetime.datetime.now()})

    class Agent:

        def __init__(self, track):
            self.mixpanel = track.mixpanel  # type: Mixpanel
            self.user_id = track.user_id  # type: str

        def search(self, media, lang, manual, primary):
            """
            :type media: Media
            :type lang: str
            :type manual: bool
            :return:
            """
            self.mixpanel.track(self.user_id, 'agent-search', {
                "media_id": media.id,
                "media_name": media.name,
                "media_year": media.year,
                "media_filename": media.filename,
                "lang": lang,
                "manual": manual,
                "primary": primary})

        def update(self, metadata, lang, force, child_guid, child_id, periodic, prefs):
            """
            :type metadata: Movie
            """
            self.mixpanel.track(self.user_id, 'agent-search', {
                "metadata_id": metadata.id,
                "metadata_title": metadata.title,
                "metadata_year": metadata.year,
                "lang": lang,
                "force": force,
                "child_guid": child_guid,
                "child_id": child_id,
                "periodic": periodic,
                "prefs": prefs})

    def test(self):
        Log.Debug(self.user_id)
        self.mixpanel.track(self.user_id, 'test')


class MixpanelExtended(Mixpanel):

    def track(self, distinct_id, event_name, properties=None, meta=None):
        Log.Warn("Sending analytics event: {}".format(event_name))
        super(MixpanelExtended, self).track(distinct_id, event_name, properties, meta)
