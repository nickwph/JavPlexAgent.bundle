from environment import environments
import service_heyzo_api

if environments.is_local_debugging:
    from plex_agent import MetadataSearchResult
    from plex_container import ObjectContainer  # noqa:F401
    from plex_locale import Locale
    from plex_log import Log


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    product_id = service_heyzo_api.extract_id(keyword)
    if product_id is None:
        return

    Log.Info("Search item with keyword: {}".format(product_id))
    item = service_heyzo_api.get_by_id(product_id)
    metadata_id = "heyzo-" + item.id + ("@{}".format(part_number) if part_number is not None else "")
    result = MetadataSearchResult(
        id=metadata_id,
        name=u"{} {}".format(item.id, item.title),
        year=item.release_date.year,
        lang=Locale.Language.Japanese,
        thumb=item.cover_url,
        score=100)
    results.Append(result)
    Log.Info(u"Added search result: {}".format(result))
