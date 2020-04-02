import datetime
from difflib import SequenceMatcher

from typing import List, Optional

import environments
import fanza_api

if environments.is_local_debugging:
    from framework.plex_agent import MetadataSearchResult, ObjectContainer
    from framework.plex_locale import Locale
    from framework.plex_log import Log


def search(results, part_number, product_id):
    """
    :type results: ObjectContainer
    :type product_id: str
    :type part_number: Optional[int]
    """
    add_body_to_results(results, part_number, fanza_api.search_dvd_product(product_id))
    add_body_to_results(results, part_number, fanza_api.search_digital_product(product_id))


def add_body_to_results(results, part_number, body):
    """
    :type results: ObjectContainer
    :type part_number: Optional[int]
    :type body: fanza_api.GetItemListBody
    """
    # Log.Info("Search item with keyword: {}".format(keyword))
    # body = fanza_api.search_digital_product(keyword)
    Log.Info("Found number of items: {}".format(body.result.total_count))

    # some more debugging
    Log.Debug("body.result.status: {}".format(body.result.status))
    Log.Debug("body.result.total_count: {}".format(body.result.status))

    # items that we found and add them to the matchable list
    items = body.result['items']  # type: List[fanza_api.Item]
    for i, item in enumerate(items):
        Log.Debug("body.result['items'][{}].product_id: {}".format(i, item.product_id))
        metadata_id = "fanza-" + item.product_id + ("@{}".format(part_number) if part_number is not None else "")
        date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')
        score = int(SequenceMatcher(None, body.request.parameters.keyword, item.product_id).ratio() * 100)
        result = MetadataSearchResult(
            id=metadata_id,
            name=u"[{}] {}".format(item.product_id.upper(), item.title),
            year=date.year,
            lang=Locale.Language.Japanese,
            thumb=item.imageURL.small,
            score=score)
        results.Append(result)
        Log.Info(u"Added search result: {}".format(result))
