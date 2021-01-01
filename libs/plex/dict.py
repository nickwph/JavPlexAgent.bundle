# coding=utf-8
from collections import MutableMapping

from termcolor import colored


# noinspection PyPep8Naming,PyClassHasNoInit
class Dict(dict):
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

    def __getitem__(self, key):
        return self.store[self._keytransform(key)]

    def __setitem__(self, key, value):
        self.store[self._keytransform(key)] = value

    def __delitem__(self, key):
        del self.store[self._keytransform(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def _keytransform(self, key):
        return key
