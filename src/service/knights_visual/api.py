# coding=utf-8
from datetime import datetime, time
from rfc822 import parsedate

import requests
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
    item.description = query("div.entry-content > p").text().strip()
    item.poster_url = base_url + query("div.entry-content > p > a > img").attr("data-lazy-src")
    item.cover_url = base_url + query("div.entry-content > p > a").attr("href")
    item.sample_video_url = query("div.entry-content > video").attr("src")
    item.sample_image_thumbnail_urls = query(".gallery img") \
        .map(lambda i, e: PyQuery(this).attr("data-lazy-src"))  # noqa: this
    item.sample_image_urls = query(".gallery a").map(lambda i, e: PyQuery(this).attr("href"))  # noqa: this

    poster_url_head = requests.head(item.poster_url)
    last_modified = poster_url_head.headers['Last-Modified']
    item.upload_date = datetime(*parsedate(last_modified)[:7])

    return item


class KnightVisualSearchResultItem(object):
    def __init__(self):
        self.id = "Stub"
        self.url = "Stub"
        self.title = "Stub"
        self.thumbnail_url = "Stub"
        self.upload_year = 0  # Stub


class KnightVisualItem(object):
    def __init__(self):
        self.id = "Stub"
        self.url = "Stub"
        self.title = "Stub"
        self.description = "Stub"
        self.label = "Stub"
        self.poster_url = "Stub"
        self.cover_url = "Stub"
        self.sample_video_url = "Stub"
        self.author_name = "Stub"
        self.actress_name = "Stub"
        self.duration = datetime.now().time()  # Stub
        self.duration_in_minutes = 0  # Stub
        self.upload_date = datetime.now()
        self.sample_image_urls = []  # type: List[str]
        self.sample_image_thumbnail_urls = []  # type: List[str]
