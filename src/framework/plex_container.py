# noinspection PyPep8Naming,PyUnresolvedReferences
class ObjectContainer(list):
    """
    <MediaContainer object> from logging
    """
    view_group = "Stub"
    art = "Stub"
    title1 = "Stub"
    title2 = "Stub"
    noHistory = False  # Stub
    replaceParent = False  # Stub

    def Append(self, result):
        """
        :param result: MetadataSearchResult
        """
        list.append(self, result)
