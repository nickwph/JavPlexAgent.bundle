import time

import api
from plex.agent import MetadataSearchResult
from plex.locale import Locale
from plex.log import Log
from utility import mixpanel_helper


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    start_time_in_seconds = time.time()
    product_id = api.extract_id(keyword)
    if product_id is None: return  # noqa
    Log.Info("Search item with keyword: {}".format(product_id))
    item = api.get_item(product_id)
    metadata_id = "carib-" + item.id + ("@{}".format(part_number) if part_number is not None else "")
    result = MetadataSearchResult(
        id=metadata_id,
        name=u"{} {}".format(item.id, item.title),
        year=item.upload_date.year,
        lang=Locale.Language.Japanese,
        thumb=item.poster_url,
        score=100)
    results.Append(result)
    Log.Info(u"Added search result: {}".format(result))
    time_spent_in_seconds = time.time() - start_time_in_seconds
    mixpanel_helper.track.search.result_returned('caribbeancom', result, time_spent_in_seconds)
