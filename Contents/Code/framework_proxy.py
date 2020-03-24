# coding=utf-8


# noinspection PyPep8Naming,PyClassHasNoInit
class Proxy:
    """
    Proxy objects are used for associating image and audio files with metadata.

    Metadata objects will often have many posters, background images or theme music tracks available, but the user will
    usually only require one of each. This makes downloading the data for each possible choice time-consuming and places
    undue burden on the servers providing the data.

    To remedy this, the framework uses proxy objects to reduce the amount of data that needs to be downloaded during
    the initial metadata update. There are two types of proxy available.

    Using proxies is simple. The proxy should be assigned to a proxy container attribute, using the media’s full URL
    as the key:

        metadata.posters[full_poster_url] = Proxy.Preview(poster_thumbnail_data)

    The sort_order attribute can be set to specify the order in which the possible choices are presented to the user.
    Items with lower sort order values are listed first.
    """

    @staticmethod
    def Preview(data, sort_order=None):
        """
        This proxy should be used when a preview version of the final piece of media is available, e.g. a thumbnail
        image for a high-resolution poster, or a short clip of a theme music file. When the user selects a piece of
        media referred to by a preview proxy, the media server will automatically download the final piece of media
        for use by clients.

        :param object data: ??
        :param int sort_order: ??
        :rtype: Proxy
        """
        pass

    @staticmethod
    def Media(data, sort_order=None):
        """
        This proxy should be used when no preview version of the media is available, i.e. the data is the real media
        file data.

        :param object data: ??
        :param int sort_order: ??
        :rtype: Proxy
        """
        pass
