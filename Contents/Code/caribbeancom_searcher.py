import caribbeancom_api
import environments

if environments.is_local_debugging:
    from framework.plex_agent import MetadataSearchResult, ObjectContainer
    from framework.plex_locale import Locale
    from framework.plex_log import Log


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: int
    :type keyword: str
    """
    product_id = caribbeancom_api.extract_id(keyword)
    if product_id is None: return

    Log.Info("Search item with keyword: {}".format(product_id))
    item = caribbeancom_api.get_item(product_id)
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
