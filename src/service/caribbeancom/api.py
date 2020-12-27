# coding=utf-8
import re
from datetime import date, datetime, timedelta

from pyquery import PyQuery
from typing import List

base_url = "https://www.caribbeancom.com"
resource_base_url = "https://smovie.caribbeancom.com"


def has_valid_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    return extract_id(filename) is not None


# noinspection SpellCheckingInspection
def extract_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    match = re.match("Carib(bean|beancom)?-(\d{6}-\d+)", filename, re.IGNORECASE)  # noqa: W605
    if match:
        return match.group(2)
    return None


# noinspection PyShadowingBuiltins
def get_item(id):
    """
    :type id: str
    :rtype: CaribbeancomItem
    """
    url = "{}/moviepages/{}/index.html".format(base_url, id)
    query = PyQuery(url)
    item = CaribbeancomItem()
    item.id = id
    item.url = url
    item.title = query("h1[itemprop='name']").text()
    item.description = query("p[itemprop='description']").text()
    item.actor_name = query("div.movie-info span[itemprop='name']").text()
    item.actor_id = int(query("a[itemprop='actor']").attr("href")
                        .replace("/search_act/", "").replace("/1.html", ""))
    item.actor_url = base_url + query("a[itemprop='actor']").attr("href")
    item.actor_small_picture_url = "{}/images/actress/50x50/actor_{}.jpg".format(base_url, item.actor_id)
    item.actor_large_picture_url = "{}/box/search_act/{}/images/top.jpg".format(base_url, item.actor_id)
    item.sample_video_url = "{}/sample/movies/{}/480p.mp4".format(resource_base_url, id)
    item.poster_url = "{}/moviepages/{}/images/jacket.jpg".format(resource_base_url, id)
    item.background_url = "{}/moviepages/{}/images/l_l.jpg".format(resource_base_url, id)
    item.upload_date = datetime.strptime(query("span[itemprop='uploadDate']").text(), '%Y/%m/%d').date()
    item.duration = datetime.strptime(query("span[itemprop='duration']").text(), '%H:%M:%S').time()
    item.duration_in_seconds = int(timedelta(hours=item.duration.hour, minutes=item.duration.minute,
                                             seconds=item.duration.second).total_seconds())
    item.rating = len(query("span.spec-content.rating.meta-rating").text())

    series = query("a[onclick*='Series Name']")
    if series.length > 0:
        item.series_name = series.text()
        item.series_url = "{}{}".format(base_url, series.attr("href"))
        item.series_id = int(series.attr("href").replace("/series/", "").replace("/index.html", ""))

    for element in query("span.spec-content > a[itemprop='url']"):
        tag = CaribbeancomItem.Tag()
        tag.name = element.text
        tag.url = base_url + element.attrib['href']
        tag.slug = element.attrib['href'].replace("/listpages/", "").replace("1.htm", "")
        item.tags.append(tag)

    for element in query("a[itemprop='genre']"):
        genre = CaribbeancomItem.Genre()
        genre.name = element.text
        genre.url = base_url + element.attrib['href']
        genre.slug = element.attrib['href'].replace("/listpages/", "").replace("1.htm", "")
        item.genres.append(genre)

    for element in query("div.movie-gallery.section a.gallery-image-wrap.fancy-gallery"):
        url = element.attrib['href']  # type: str
        if "member" not in url:
            item.sample_image_urls.append(base_url + element.attrib['href'])

    for element in query("img.gallery-image[itemprop='thumbnail']"):
        item.sample_image_thumbnail_urls.append(base_url + element.attrib['src'])

    return item


# noinspection SpellCheckingInspection
class CaribbeancomItem(object):
    def __init__(self):
        self.id = "Stub"
        self.url = "Stub"
        self.title = "Stub"
        self.description = "Stub"
        self.poster_url = "Stub"
        self.background_url = "Stub"
        self.sample_video_url = "Stub"
        self.actor_name = "Stub"
        self.actor_id = 0  # Stub
        self.actor_url = "Stub"
        self.actor_small_picture_url = "Stub"
        self.actor_large_picture_url = "Stub"
        self.upload_date = date.today()  # Stub
        self.duration = datetime.now().time()  # Stub
        self.duration_in_seconds = 0  # Stub
        self.series_name = "Stub"
        self.series_id = 0  # Stub
        self.series_url = "Stub"
        self.tags = []  # type: List[CaribbeancomItem.Tag]
        self.genres = []  # type: List[CaribbeancomItem.Genre]
        self.rating = 0  # Stub
        self.sample_image_urls = []  # type: List[str]
        self.sample_image_thumbnail_urls = []  # type: List[str]

    class Tag(object):
        def __init__(self):
            self.name = "Stub"
            self.slug = "Stub"
            self.url = "Stub"

    class Genre(object):
        def __init__(self):
            self.name = "Stub"
            self.slug = "Stub"
            self.url = "Stub"
