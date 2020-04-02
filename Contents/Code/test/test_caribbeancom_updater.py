from unittest import TestCase

import environments
from framework.plex_metadata import Movie


class Test(TestCase):

    def setUp(self):
        environments.is_local_debugging = True  # this is needed

    def test_update___actual_run(self):
        import caribbeancom_updater
        metadata = Movie()
        metadata.id = "carib-070116-197@1"
        caribbeancom_updater.update(metadata)

    def test_update___actual_run_without_part(self):
        import caribbeancom_updater
        metadata = Movie()
        metadata.id = "carib-070116-197"
        caribbeancom_updater.update(metadata)
