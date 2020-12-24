# coding=utf-8
# Locale = Framework.api.networkkit.HTTPKit
# Locale = Framework.components.networking.HTTPRequest

from typing import Dict


# noinspection PyPep8Naming,PyDefaultArgument
class HTTP(object):

    @property
    def CacheTime(self):
        return "Stub"

    @CacheTime.setter
    def CacheTime(self, value):
        pass

    @property
    def Headers(self):
        return "Stub"

    @staticmethod
    def Request(url, values=None, headers={}, cacheTime=None, encoding=None, errors=None,
                timeout=60, immediate=False, sleep=0, data=None):
        """
        Creates and returns a new HTTPRequest (page 70) object.
        :param str url: The URL to use for the request.
        :param dict values: Keys and values to be URL encoded and provided as the request’s POST body.
        :param dict headers: Any custom HTTP headers that should be added to this request.
        :param int cacheTime: The maximum age (in second) of cached data before it should be considered invalid.
        :param str encoding: ??
        :param str errors: ??
        :param float timeout: The maximum amount of time (in seconds) to wait for the request to return a response
               before timing out.
        :param immediate:  If set to True, the HTTP request will be made immediately when the object is created (by
               default, requests are delayed until the data they return is requested).
        :param float sleep: The amount of time (in seconds) that the current thread should be paused for after issuing
               a HTTP request. This is to ensure undue bur- den is not placed on the server. If the data is retrieved
               from the cache, this value is ignored.
        :param str data: The raw POST data that should be sent with the request. This attribute cannot be used in
               conjunction with values.
        :return: A new HTTPRequest (page 70) object.
        :rtype: HTTPRequest
        """
        pass

    def CookiesForURL(self, url):
        pass

    def GetCookiesForURL(self, url):
        pass

    def SetPassword(self, url, username, password, realm=None):
        pass

    def PreCache(self, url, values=None, headers={}, cacheTime=None, encoding=None, errors=None):
        pass

    @property
    def Cookies(self):
        return "Stub"

    def ClearCookies(self):
        pass

    def ClearCache(self):
        pass

    def RandomizeUserAgent(self, browser=None):
        pass

    class HTTPRequest(object):
        """
        This class cannot be instantiated directly. These objects are returned from HTTP.Request() (page 69). They
        encapsulate information about a pending HTTP request, and issue it when necessary.
        """
        url = "Stub",
        values = "Stub",
        headers = {},  # type: Dict[str, str] # Stub
        cacheTime = "Stub",
        encoding = "Stub",
        errors = "Stub",
        timeout = "Stub",
        immediate = "Stub",
        sleep = "Stub",
        data = "Stub",
        opener = "Stub",
        follow_redirects = "Stub",
        method = "Stub",

        def __init__(self, url, values=None, headers={}, cacheTime=None, encoding=None, errors=None, timeout=GLOBAL_DEFAULT_TIMEOUT, immediate=False, sleep=0, data=None, opener=None,
                     sandbox=None, follow_redirects=True, basic_auth=None, method=None):
            pass

        def load(self):
            """
            Instructs the object to issue the HTTP request, if it hasn’t done so already.
            """
            pass

        @property
        def headers(self):
            pass

        @property
        def content(self):
            pass

