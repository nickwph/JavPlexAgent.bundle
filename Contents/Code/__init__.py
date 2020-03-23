import subprocess

from environments import is_local_debugging

if is_local_debugging:
    from .framework.agent import Agent, Media, Locale, MetadataSearchResult
    from .framework.log import Log
    from .framework.platform import Platform


# noinspection PyPep8Naming
def Start():
    Log.Error("=========== Start ==========")

    process = subprocess.Popen(['node', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    Log.Error('stdout, stderr: {} {}'.format(stdout, stderr))

    process = subprocess.Popen(['pwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    Log.Error('stdout, stderr: {} {}'.format(stdout, stderr))

    process = subprocess.Popen(['whoami'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    Log.Error('stdout, stderr: {} {}'.format(stdout, stderr))


class JavAgent(Agent.TV_Shows):
    name = 'Jav Media'
    ver = '1.0.0'
    primary_provider = True
    languages = [Locale.Language.NoLanguage]
    accepts_from = [
        'com.plexapp.agents.localmedia',
        'com.plexapp.agents.opensubtitles',
        'com.plexapp.agents.podnapisi',
        'com.plexapp.agents.subzero'
    ]

    contributes_to = [
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none'
    ]

    # noinspection PyMethodMayBeStatic
    def search(self, results, media, lang, manual):
        """
        :type results: MediaContainer
        :type media: Media
        :type lang: str
        :type manual: bool
        :return:
        """
        Log.Error("=========== Search ==========")
        Log.Error("{} Version: {}".format(self.name, self.ver))
        Log.Error('Plex Server Version: {}'.format(Platform.ServerVersion))
        Log.Error("Searching results: {}".format(results))
        Log.Error("Searching media: {}".format(media))
        Log.Error("Searching lang: {}".format(lang))
        Log.Error("Searching manual: {}".format(manual))

        process = subprocess.Popen(['echo', 'More output'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        results.Append(MetadataSearchResult(id=media.id, name=media.name, year=media.year, lang=lang, score=100))

        Log.Error('media.filename: {}'.format(media.filename))
        Log.Error('stdout, stderr: {} {}'.format(stdout, stderr))

        # path1 = media.items[0].parts[0].file
        # Log.Error('media file: {name}'.format(name=path1))
        #
        # folder_path = os.path.dirname(path1)
        # Log.Error('folder path: {name}'.format(name=folder_path))

        Log.Error("Result results: {}".format(results))
        pass

    # noinspection PyMethodMayBeStatic
    def update(self, metadata, media, lang, force):
        """
        :type metadata: MetadataSearchResult
        :type media: Media
        :type lang: str
        :type force: bool
        """
        Log.Error("=========== Update ==========")
        Log.Error("Updating metadata: {}".format(metadata))
        Log.Error("Updating media: {}".format(media))
        Log.Error("Updating lang: {}".format(lang))
        Log.Error("Updating force: {}".format(force))
        pass
