from difflib import SequenceMatcher

from typing import Optional

import environments
import knights_visual_api

if environments.is_local_debugging:
    from framework.plex_agent import MetadataSearchResult
    from framework.plex_container import ObjectContainer  # noqa:F401
    from framework.plex_locale import Locale
    from framework.plex_log import Log


def search(results, part_number, keyword):
    """
    :type results: ObjectContainer[MetadataSearchResult]
    :type part_number: Optional[int]
    :type keyword: str
    """
    if not keyword.startswith("KV") or not keyword.startswith("KV-"):
        return

    product_id = keyword
    if keyword.startswith("KV") and not keyword.startswith("KV-"):
        product_id = product_id.replace("KV", "KV-")

    Log.Info("Search item with keyword: {}".format(product_id))
    items = knights_visual_api.search(product_id)

    for item in items:
        metadata_id = "knightsvisual-" + item.id + ("@{}".format(part_number) if part_number is not None else "")
        score = int(SequenceMatcher(None, keyword, item.id).ratio() * 100)
        result = MetadataSearchResult(
            id=metadata_id,
            name=u"{} {}".format(item.id, item.title),
            year=item.upload_year,
            lang=Locale.Language.Japanese,
            thumb=item.thumbnail_url,
            score=score)
        results.Append(result)
        Log.Info(u"Added search result: {}".format(result))
