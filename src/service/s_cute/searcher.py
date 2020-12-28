import re

import api
from plex.agent import MetadataSearchResult
from plex.locale import Locale
from plex.log import Log


def extract_id(filename):
    """
    :type filename: str
    :rtype: str
    """
    match = re.findall("scute-(.*?)$", filename, re.IGNORECASE)
    if len(match) > 0: return match[0]
    return None


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    product_id = extract_id(keyword)
    if product_id is None: return

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
