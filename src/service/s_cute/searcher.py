import re
import time

import api
from plex.agent import MetadataSearchResult
from plex.locale import Locale
from plex.log import Log
from utility import mixpanel_helper


def extract_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    match = re.findall("s-cute-(.*?)$", filename, re.IGNORECASE)
    if len(match) > 0: return match[0]  # noqa
    return None


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    start_time_in_seconds = time.time()
    product_id = extract_id(keyword)
    if product_id is None: return  # noqa
    Log.Info("Search item with keyword: {}".format(product_id))
    item = api.get_by_id(product_id)
    metadata_id = "s-cute-" + item.id + ("@{}".format(part_number) if part_number is not None else "")
    result = MetadataSearchResult(
        id=metadata_id,
        name=u"{} {}".format(item.id.upper(), item.title),
        year=item.release_date.year,
        lang=Locale.Language.Japanese,
        thumb=item.cover_url,
        score=100)
    results.Append(result)
    Log.Info(u"Added search result: {}".format(result))
    time_spent_in_seconds = time.time() - start_time_in_seconds
    mixpanel_helper.track.search.result_returned('caribbeancom', result, time_spent_in_seconds)
