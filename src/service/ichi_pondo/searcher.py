import api

from plex.agent import MetadataSearchResult
from plex.locale import Locale
from plex.log import Log


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    product_id = api.extract_id(keyword)
    if product_id is None:
        return

    Log.Info("Search item with keyword: {}".format(product_id))
    item = api.get_by_id(product_id)
    metadata_id = "1pon-" + item.movie_id + ("@{}".format(part_number) if part_number is not None else "")
    result = MetadataSearchResult(
        id=metadata_id,
        name=u"{} {}".format(item.movie_id, item.title),
        year=item.year,
        lang=Locale.Language.Japanese,
        thumb=item.thumb_high,
        score=100)
    results.Append(result)
    Log.Info(u"Added search result: {}".format(result))