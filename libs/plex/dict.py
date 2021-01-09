# coding=utf-8


# noinspection PyPep8Naming,PyClassHasNoInit
class DictClass(dict):
    """
    The Dict API provides access to a global singleton dictionary object,
    which can be used as a key-value store by the developer. The dictionary
    is automatically persisted across plug-in relaunches, and can safely
    be accessed from any thread.
    Note: Only basic Python data types are officially supported by the
    dictionary. Many other types of object will be accepted correctly, but
    certain objects will cause errors (e.g. XML and HTML element objects).
    The developer should convert these objects to a more basic type before
    attempting to store them.
    """

    @staticmethod
    def Save():
        pass

    @staticmethod
    def Reset():
        pass


Dict = DictClass()
