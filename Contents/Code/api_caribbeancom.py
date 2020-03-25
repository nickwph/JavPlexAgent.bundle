# coding=utf-8
from datetime import date, datetime, timedelta

from pyquery import PyQuery as pq
from typing import List


class CaribbeancomApi(object):

    @staticmethod
    def get_item(id):
        """
        :type id: str
        :rtype: CaribbeancomItem
        """
        query = pq("https://www.caribbeancom.com/moviepages/{}/index.html".format(id))
        item = CaribbeancomItem()
        item.id = id
        item.title = query("h1[itemprop='name']").text()
        item.description = query("p[itemprop='description']").text()
        item.actor_name = query("div.movie-info span[itemprop='name']").text()
        item.actor_id = int(query("a[itemprop='actor']").attr("href")
                            .replace("/search_act/", "").replace("/1.html", ""))
        item.actor_url = "https://www.caribbeancom.com" + query("a[itemprop='actor']").attr("href")
        item.sample_video_url = "https://smovie.caribbeancom.com/sample/movies/{}/480p.mp4".format(id)
        item.poster_url = "https://smovie.caribbeancom.com/moviepages/{}/images/l_l.jpg".format(id)
        item.upload_date = datetime.strptime(query("span[itemprop='uploadDate']").text(), '%Y/%m/%d').date()
        item.duration = datetime.strptime(query("span[itemprop='duration']").text(), '%H:%M:%S').time()
        item.duration_in_seconds = int(timedelta(hours=item.duration.hour, minutes=item.duration.minute,
                                                 seconds=item.duration.second).total_seconds())
        item.series_name = query("a[onclick*='Series Name']").text()
        item.series_url = "https://www.caribbeancom.com" + query("a[onclick*='Series Name']").attr("href")
        item.series_id = int(query("a[onclick*='Series Name']").attr("href")
                             .replace("/series/", "").replace("/index.html", ""))

        item.rating = len(query("span.spec-content.rating.meta-rating").text())

        for element in query("span.spec-content > a[itemprop='url']"):
            tag = CaribbeancomItem.Tag()
            tag.name = element.text
            tag.url = "https://www.caribbeancom.com" + element.attrib['href']
            tag.slug = element.attrib['href'].replace("/listpages/", "").replace("1.htm", "")
            item.tags.append(tag)

        for element in query("a[itemprop='genre']"):
            genre = CaribbeancomItem.Genre()
            genre.name = element.text
            genre.url = "https://www.caribbeancom.com" + element.attrib['href']
            genre.slug = element.attrib['href'].replace("/listpages/", "").replace("1.htm", "")
            item.genres.append(genre)

        for element in query("a.gallery-image-wrap.fancy-gallery"):
            url = element.attrib['href']  # type: str
            if "member" not in url:
                item.sample_image_urls.append("https://www.caribbeancom.com" + element.attrib['href'])

        for element in query("img.gallery-image[itemprop='thumbnail']"):
            item.sample_image_thumbnail_urls.append("https://www.caribbeancom.com" + element.attrib['src'])

        return item


# noinspection SpellCheckingInspection
class CaribbeancomItem(object):
    class Tag(object):
        name = "Stub"
        slug = "Stub"
        url = "Stub"

    class Genre(object):
        name = "Stub"
        slug = "Stub"
        url = "Stub"

    id = "Stub"
    title = "Stub"
    description = "Stub"
    poster_url = "Stub"
    sample_video_url = "Stub"
    actor_name = "Stub"
    actor_id = 0  # Stub
    actor_url = "Stub"
    upload_date = date.today()  # Stub
    duration = datetime.now().time()  # Stub
    duration_in_seconds = 0  # Stub
    series_name = "Stub"
    series_id = 0  # Stub
    series_url = "Stub"
    tags = []  # type: List[Tag]
    genres = []  # type: List[Genre]
    rating = 0  # Stub
    sample_image_urls = []  # type: List[str]
    sample_image_thumbnail_urls = []  # type: List[str]