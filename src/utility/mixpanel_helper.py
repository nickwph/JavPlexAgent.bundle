import datetime
import socket

from mixpanel import Mixpanel

from plex.container import ObjectContainer
from plex.log import Log

track = None  # type: Track


def initialize(token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version):
    global track
    if track is None:
        track = Track(token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version)
    return track


class Track:

    def __init__(self, token, user_id, version, git_hash, build_number, build_datetime, plex_version, environment, os_name, os_version, hostname, full_version):
        Log.Debug(token)
        self.mixpanel = MixpanelExtended(token)  # type: Mixpanel
        self.user_id = user_id  # type: str
        self.main = Track.Main(self)
        self.agent = Track.Agent(self)
        self.version_info = {
            'Agent Version': version,
            'Agent Git Hash': git_hash,
            'Agent Build Number': build_number,
            'Agent Build Date Time': build_datetime,
            'Agent Full Version': full_version,
            'Environment': environment,
            'Plex Version': plex_version,
            'OS Name': os_name,
            'OS Version': os_version,
            'System Hostname': hostname,
        }

    class Main:

        def __init__(self, track):
            self.mixpanel = track.mixpanel  # type: Mixpanel
            self.user_id = track.user_id  # type: str
            self.track = track  # type: Track

        def installed(self):
            self.mixpanel.track(self.user_id, 'Main | Installed', self.track.version_info)
            self.mixpanel.people_set(self.user_id, self.track.version_info)
            self.mixpanel.people_set(self.user_id, {'First Seen At': datetime.datetime.now()})

        def initialized(self, time_spent_in_seconds):
            properties = self.track.version_info.copy()
            properties['Time Spent In Seconds'] = time_spent_in_seconds
            self.mixpanel.track(self.user_id, 'Main | Initialized', properties)
            self.mixpanel.people_set(self.user_id, self.track.version_info)
            self.mixpanel.people_set(self.user_id, {'Last Seen At': datetime.datetime.now()})

    class Agent:

        def __init__(self, track):
            self.mixpanel = track.mixpanel  # type: Mixpanel
            self.user_id = track.user_id  # type: str
            self.search = Track.Agent.Search(track)

        def searched(self, media, lang, manual, primary, filename, directory, product_id, part_number, results, time_spent_in_seconds):
            """
            :type media: Media
            :type lang: str
            :type manual: bool
            :type filename: str
            :type directory: str
            :type product_id: str
            :type part_number: int
            :type results: ObjectContainer
            :return:
            """
            self.mixpanel.track(self.user_id, 'Agent | Searched', {
                "Media ID": media.id,
                "Media Name": media.name,
                "Media Year": media.year,
                "Media Filename": media.filename,
                "Parsed Filename": filename,
                "Parsed Directory": directory,
                "Parsed Product ID": product_id,
                "Parsed Part Number": part_number,
                "Results Count": len(results),
                "Language": lang,
                "Manual": manual,
                "Primary": primary,
                "Time Spent In Seconds": time_spent_in_seconds})

        def updated(self, metadata, lang, force, child_guid, child_id, periodic, prefs, time_spent_in_seconds):
            """
            :type metadata: Movie
            """
            self.mixpanel.track(self.user_id, 'Agent | Updated', {
                "Metadata ID": metadata.id,
                "Metadata Title": metadata.title,
                "Metadata Year": metadata.year,
                "Language": lang,
                "Force": force,
                "Child GUID": child_guid,
                "Child ID": child_id,
                "Periodic": periodic,
                "Prefs": prefs,
                "Time Spent In Seconds": time_spent_in_seconds})

        class Search:

            def __init__(self, track):
                self.mixpanel = track.mixpanel  # type: Mixpanel
                self.user_id = track.user_id  # type: str

            def result_returned(self, source, result, time_spent_in_seconds):
                """
                :type result: MetadataSearchResult
                """
                self.mixpanel.track(self.user_id, 'Agent | Search | Result Returned', {
                    "Source": source,
                    "Result ID": result.id,
                    "Result Name": result.name,
                    "Result Year": result.year,
                    "Result Language": result.lang,
                    "Result Thumbnail": result.thumb,
                    "Result Score": result.score,
                    "Time Spent In Seconds": time_spent_in_seconds})


class MixpanelExtended(Mixpanel):

    def track(self, distinct_id, event_name, properties=None, meta=None):
        Log.Info("Sending analytics event: {}".format(event_name))
        Log.Debug("properties: {}".format(properties))
        Log.Debug("meta: {}".format(meta))
        super(MixpanelExtended, self).track(distinct_id, event_name, properties, meta)
