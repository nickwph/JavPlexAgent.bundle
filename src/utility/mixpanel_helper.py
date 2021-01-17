import datetime

from mixpanel import Mixpanel
from requests import get

import build_config
from plex.container import ObjectContainer  # noqa
from plex.log import Log

track = None  # type: Track


def initialize(user_id, test_mode=False):
    global track
    if track is None:
        track = Track(user_id, test_mode)
    return track


class Track:

    def __init__(self, user_id, test_mode):
        Log.Info("Initializing Mixpanel")
        ip = self.get_ip()
        Log.Debug("user_id: {}".format(user_id))
        Log.Debug("token: {}".format(build_config.mixpanel_token))
        Log.Debug("ip: {}".format(ip))
        self.mixpanel = MixpanelExtended(build_config.mixpanel_token, test_mode)  # type: Mixpanel
        self.mixpanel.people_set(user_id, {'$first_name': build_config.hostname}, {'$ip': ip})
        self.user_id = user_id  # type: str
        self.search = Track.Search(self)
        self.version_info = {
            'Agent Version': build_config.version,
            'Agent Git Hash': build_config.git_hash,
            'Agent Build Number': build_config.build_number,
            'Agent Build Date Time': build_config.build_datetime,
            'Agent Full Version': build_config.full_version,
            'Environment': build_config.environment,
            'Plex Version': build_config.plex_version,
            'OS Name': build_config.os_name,
            'OS Version': build_config.os_version,
            'System Hostname': build_config.hostname,
            'IP Address': ip
        }

    def get_ip(self):
        ip = get('https://api.ipify.org').text
        return ip

    def installed(self):
        self.mixpanel.track(self.user_id, 'Installed', self.version_info)
        self.mixpanel.people_set(self.user_id, self.version_info)
        self.mixpanel.people_set(self.user_id, {'First Seen At': datetime.datetime.now()})

    def initialized(self, image_rocessing_capability, time_spent_in_seconds):
        properties = self.version_info.copy()
        properties['Time Spent In Seconds'] = time_spent_in_seconds
        properties['Image Processing Capability'] = image_rocessing_capability
        self.mixpanel.track(self.user_id, 'Initialized', properties)
        self.mixpanel.people_set(self.user_id, self.version_info)
        self.mixpanel.people_set(self.user_id, {'Last Seen At': datetime.datetime.now()})

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
        self.mixpanel.track(self.user_id, 'Searched', {
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
        self.mixpanel.track(self.user_id, 'Updated', {
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
            self.mixpanel.track(self.user_id, 'Search Result Returned', {
                "Source": source,
                "Result ID": result.id,
                "Result Name": result.name,
                "Result Year": result.year,
                "Result Language": result.lang,
                "Result Thumbnail": result.thumb,
                "Result Score": result.score,
                "Time Spent In Seconds": time_spent_in_seconds})


class MixpanelExtended(Mixpanel):

    def __init__(self, token, test_mode):
        super(MixpanelExtended, self).__init__(token)
        self.test_mode = test_mode

    def track(self, distinct_id, event_name, properties=None, meta=None):
        Log.Info("Sending track event: {}".format(event_name))
        Log.Debug("properties: {}".format(properties))
        Log.Debug("meta: {}".format(meta))
        if not self.test_mode:
            super(MixpanelExtended, self).track(distinct_id, event_name, properties, meta)

    def people_set(self, distinct_id, properties, meta=None):
        Log.Info("Sending people set event")
        Log.Debug("distinct_id: {}".format(distinct_id))
        Log.Debug("properties: {}".format(properties))
        Log.Debug("meta: {}".format(meta))
        if not self.test_mode:
            super(MixpanelExtended, self).people_set(distinct_id, properties, meta)
