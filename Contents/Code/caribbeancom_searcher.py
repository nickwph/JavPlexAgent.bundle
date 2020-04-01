import caribbeancom_api
import environments

if environments.is_local_debugging:
    from framework.plex_agent import MetadataSearchResult, ObjectContainer
    from framework.plex_locale import Locale
    from framework.plex_log import Log


def search(results, keyword):
    """
    :type results: ObjectContainer
    :type keyword: str
    """
    id = caribbeancom_api.extract_id(keyword)
    if id is None: return

    Log.Info("Search item with keyword: {}".format(id))
    item = caribbeancom_api.get_item(id)
    result = MetadataSearchResult(
        id="carib-" + item.id,
        name="{} {}".format(id, item.title),
        year=item.upload_date.year,
        lang=Locale.Language.Japanese,
        thumb=item.poster_url,
        score=100)
    results.Append(result)
    Log.Info("Added search result: {}".format(result))
