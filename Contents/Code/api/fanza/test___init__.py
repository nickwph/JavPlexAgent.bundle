from unittest import TestCase

from api.fanza import normalise


class Test(TestCase):
    def test_normalise(self):
        normalise("ASDASD")
        # self.fail()
