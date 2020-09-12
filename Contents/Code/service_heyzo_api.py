# coding=utf-8
from datetime import datetime, time

from pyquery import PyQuery
from typing import List, Any
import requests
from rfc822 import parsedate, parsedate_tz

base_url = "https://www.heyzo.com"


# noinspection SpellCheckingInspection
def extract_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    match = re.match("Heyzo-(\d{4})", filename, re.IGNORECASE)  # noqa: W605
    if match:
        return match.group(2)
    return None


def get_by_id(id):
    """
    :type id: str
    :rtype: HeyzoItem
    """
    url = "{}/moviepages/{}/index.html".format(base_url, id)
    query = PyQuery(url)
    item = HeyzoItem()
    item.id = id
    item.url = url
    item.title = query('#movie h1').text().split('-')[0].strip()
    item.description = query('p.memo').text().strip()
    item.actress_name = query('.table-actor span').text()
    item.actress_url = base_url + query('.table-actor a').attr('href')
    item.actress_id = int(item.actress_url.split('_')[1])
    item.actress_picture_url = "{}/actorprofile/3000/{}/profile.jpg".format(base_url, str(item.actress_id).zfill(4))
    item.release_date = datetime.strptime(query('.table-release-day td')[1].text.strip(), '%Y-%m-%d').date()
    item.rating = float(query("span[itemprop='ratingValue']").text())
    item.cover_url = "{}/contents/3000/{}/images/player_thumbnail.jpg".format(base_url, id)

    for element in query(".table-actor-type a"):
        category = HeyzoItem.Category()
        category.name = element.text
        category.url = base_url + element.attrib['href']
        category.id = int(category.url.split('_')[1])
        item.categories.append(category)

    for element in query(".table-tag-keyword-small .tag-keyword-list a"):
        tag = HeyzoItem.Tag()
        tag.name = element.text
        tag.url = base_url + element.attrib['href']
        item.tags.append(tag)

    return item


class HeyzoItem(object):
    id = "Stub"
    url = "Stub"
    title = "Stub"
    description = "Stub"
    cover_url = "Stub"
    actress_id = "Stub"
    actress_name = "Stub"
    actress_url = "Stub"
    actress_picture_url = "Stub"
    rating = 0.0  # Stub
    release_date = datetime.now()  # Stub
    categories = []  # type: List[Category]
    tags = []  # type: List[Tag]

    class Category(object):
        id = 0  # Stub
        name = "Stub"
        url = "Stub"

    class Tag(object):
        name = "Stub"
        url = "Stub"
