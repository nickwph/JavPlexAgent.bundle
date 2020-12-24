# coding=utf-8


# noinspection PyPep8Naming,PyClassHasNoInit
class Data:
    """
    The Data API provides methods for storing and retrieving arbitrary data. Plug-ins are generally not allowed to
    access the user’s file system directly, but can use these methods to load and save files in a single directory
    assigned by the framework.

    The data storage locations are unique for each plug-in, preventing one plug-in from modifying data stored by
    another.

    Note: The actual location of data files stored by these methods may vary between platforms.
    """

    @staticmethod
    def Load(item):
        """
        Loads a previously stored binary data item.
        :param str item: The name of the data item to load.
        :return: The contents of the data item stored on disk.
        :rtype: str
        """
        pass

    @staticmethod
    def Save(item, data):
        """
        Stores binary data as a data item with the given name.
        :param str item: The name of the data item to store.
        :param str data: The binary data to store.
        """
        pass

    @staticmethod
    def LoadObject(item):
        """
        Loads a Python object previously stored as a data item.
        :param str item: The name of the data item to load.
        :return: The contents of the data item stored on disk.
        :rtype: object
        """
        pass

    @staticmethod
    def SaveObject(item, obj):
        """
        Stores a Python object as a data item with the given name.
        :param str item: The name of the data item to store.
        :param object obj: The Python object to store.
        """
        pass

    @staticmethod
    def Exists(item):
        """
        Checks for the presence of a data item with the given name.
        :param str item: The name of the data item to check for.
        :return: The existence of the item.
        :rtype: bool
        """
        pass

    @staticmethod
    def Remove(item):
        """
        Removes a previously stored data item with the given name.
        :param str item: The name of the data item to remove.
        """
        pass
