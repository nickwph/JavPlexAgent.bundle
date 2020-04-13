# coding=utf-8
from datetime import datetime, time

from pyquery import PyQuery
from typing import List

base_url = "https://www.knights-visual.com"


def search(product_id):
    """
    :type product_id: str
    :rtype: List[KnightVisualSearchResultItem]
    """
    url = "{}/?auth=ok&s={}".format(base_url, product_id)  # type: str
    query = PyQuery(url)
    results = []

    posts = query("ul.hfeed > li.post")
    for post in posts:
        post_query = PyQuery(post)
        item_url = post_query("a.entry-thumbnails-link").attr("href")  # type: str
        if item_url.startswith("{}/works/furasupi".format(base_url)):
            item_url_split = item_url.split("/")
            item = KnightVisualSearchResultItem()
            item.id = item_url_split[len(item_url_split) - 2]
            item.url = item_url
            item.title = post_query(".entry-title > a").text()
            item.thumbnail_url = post_query("a.entry-thumbnails-link img").attr("data-lazy-src")
            item.upload_year = int(item.thumbnail_url.split("/")[5])
            results.append(item)

    return results


def get_by_id(product_id):
    return get_by_url("{}/works/furasupi/{}".format(base_url, product_id))


# noinspection PyUnresolvedReferences
def get_by_url(product_url):
    query = PyQuery(product_url)
    item = KnightVisualItem()

    table_data = query("div.kvp_goods_info_table td.data")
    item.url = product_url
    item.id = table_data[0].text
    item.label = table_data[1].text
    item.actress_name = table_data[2].text
    item.author_name = table_data[3].text
    item.duration_in_minutes = int(table_data[4].text[:-1])
    item.duration = time(hour=item.duration_in_minutes / 60, minute=item.duration_in_minutes % 60)
    item.title = query("h1.entry-title > a").text()
    item.description = query("div.entry-content > p").text()
    item.poster_url = base_url + query("div.entry-content > p > a > img").attr("data-lazy-src")
    item.cover_url = base_url + query("div.entry-content > p > a").attr("href")
    item.sample_video_url = base_url + query("div.entry-content > video").attr("src")
    item.sample_image_thumbnail_urls = query(".gallery img").map(lambda i, e: PyQuery(this).attr("data-lazy-src"))
    item.sample_image_urls = query(".gallery a").map(lambda i, e: PyQuery(this).attr("href"))

    poster_url_split = item.poster_url.split("/")
    item.upload_year = int(poster_url_split[5])
    item.upload_month = int(poster_url_split[6])

    return item


class KnightVisualSearchResultItem(object):
    id = "Stub"
    url = "Stub"
    title = "Stub"
    thumbnail_url = "Stub"
    upload_year = 0  # Stub


class KnightVisualItem(object):
    id = "Stub"
    url = "Stub"
    title = "Stub"
    description = "Stub"
    poster_url = "Stub"
    sample_video_url = "Stub"
    author_name = "Stub"
    actress_name = "Stub"
    duration = datetime.now().time()  # Stub
    duration_in_minutes = 0  # Stub
    upload_year = 0  # Stub
    upload_month = 0  # Stub
    sample_image_urls = []  # type: List[str]
    sample_image_thumbnail_urls = []  # type: List[str]
