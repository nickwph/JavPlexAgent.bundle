import sys
import os
from inspect import getfile, currentframe
from os.path import dirname, abspath, join, isdir

import requests

root_dir = dirname(dirname(abspath(getfile(currentframe()))))
sys.path.insert(0, join(root_dir, 'src'))
sys.path.insert(0, join(root_dir, 'libs'))

import service.caribbeancom.api as caribbeancom_api
import service.caribbeancom_pr.api as caribbeancom_pr_api
import service.fanza.api as fanza_api
import service.heyzo.api as heyzo_api
import service.ichi_pondo.api as ichi_pondo_api
import service.idea_pocket.api as idea_pocket_api
import service.knights_visual.api as knights_visual_api
import service.s1.api as s1_api
import service.s_cute.api as s_cute_api


def get_cover_url(product_id):
    function_calls = [
        fanza_dvd_cover_url,
        fanza_digital_cover_url,
        caribbeancom_cover_url,
        caribbeancom_pr_cover_url,
        heyzo_cover_url,
        ichi_pondo_cover_url,
        knights_visual_cover_url,
        s_cute_cover_url,
    ]
    for call in function_calls:
        url = call(product_id)
        if url is not None:
            print 'found cover: ' + url
            return url


def fanza_digital_cover_url(product_id):
    print 'checking: fanza_digital_cover_url'
    result = fanza_api.search_digital_product(product_id)
    if result.result.result_count > 0:
        return result.result.items[0].imageURL.large


def fanza_dvd_cover_url(product_id):
    print 'checking: fanza_dvd_cover_url'
    result = fanza_api.search_dvd_product(product_id)
    if result.result.result_count > 0:
        return result.result.items[0].imageURL.large


def caribbeancom_cover_url(product_id):
    print 'checking: caribbeancom_cover_url'
    result = caribbeancom_api.get_item(product_id)
    if result:
        return result.poster_url


def caribbeancom_pr_cover_url(product_id):
    print 'checking: caribbeancom_pr_cover_url'
    result = caribbeancom_pr_api.get_item(product_id)
    if result:
        return result.poster_url


def heyzo_cover_url(product_id):
    print 'checking: heyzo_cover_url'
    result = heyzo_api.get_by_id(product_id)
    if result:
        return result.cover_url


def ichi_pondo_cover_url(product_id):
    print 'checking: ichi_pondo_cover_url'
    result = ichi_pondo_api.get_by_id(product_id)
    if result:
        return result.thumb_high


def knights_visual_cover_url(product_id):
    print 'checking: knights_visual_cover_url'
    result = knights_visual_api.get_by_id(product_id)
    if result:
        return result.cover_url


def s_cute_cover_url(product_id):
    print 'checking: s_cute_cover_url'
    result = s_cute_api.get_by_id(product_id)
    if result:
        return result.cover_url


directory = join('e2e')
for name in os.listdir(directory):
    if isdir(join(directory, name)):
        print 'checking ' + name + '...',
        cover_path = join(directory, name, name + '.jpg')
        if os.path.exists(cover_path):
            print 'cover exists'
            break
        cover_url = get_cover_url(name)
        if cover_url is None:
            print 'cover not found. skipping'
        else:
            print 'downloading cover'
            r = requests.get(cover_url, allow_redirects=True)
            open(cover_path, 'wb').write(r.content)
