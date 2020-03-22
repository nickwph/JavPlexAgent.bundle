# -*- coding: utf-8 -*-

import time
import requests
from spotify import Logging

class Tunigo():

    def __init__(self, region = "us"):
        self.region = "us" if region is None else region
        self.locale = self.getLocaleFromRegion(self.region)
        self.root_url = "http://api.tunigo.com/v3/space/"
        Logging.debug("Starting with Tunigo for region: "  + self.region)

    def getLocaleFromRegion(self, region):
        if (region == 'AR'):
            return 'es'
        if (region == 'US'):
            return 'us'

        return region

    def getFeaturedPlaylists(self):
      url = self.buildUrl("featured-playlists")
      response = self.doRequest("getFeaturedPlaylists", url)
      return self.parseResponse(response)

    def getTopPlaylists(self):
      url = self.buildUrl("toplists")
      response = self.doRequest("getTopPlaylists", url)
      return self.parseResponse(response)

    def getNewReleases(self):
      url = self.buildUrl("new-releases")
      response = self.doRequest("getNewReleases", url)
      return self.parseResponse(response)

    def getGenres(self):
      url = self.buildUrl("genres")
      response = self.doRequest("getGenres", url)
      return self.parseResponse(response)

    def getPlaylistsByGenre(self, genre_name):
      url = self.buildUrl(genre_name)
      response = self.doRequest("getPlaylistsByGenre", url)
      return self.parseResponse(response)

    def buildUrl(self, action):
      fixed_params = "page=0&per_page=50&product=premium&version=6.31.1&platform=web"
      date_param   = "dt=" + time.strftime("%Y-%m-%dT%H:%M:%S") #2014-05-29T02%3A01%3A00"
      region_param = "region=" + self.region
      locale_param = "locale=" + self.locale
      full_url = self.root_url + action + '?' + fixed_params + '&' + date_param + '&' + region_param + '&' + locale_param
      return full_url

    def doRequest(self, name, url):
      Logging.debug("Tunigo - " + name + " url: " + url)
      response = requests.get(url)
      #Logging.debug("Tunigo - " + name + " response OK")
      #Logging.debug("Tunigo - " + name + " response: " + str(response.json()))
      return response

    def parseResponse(self, response):
      if response.status_code != 200:
        return { 'items': [] }

      return response.json()
