from unittest import TestCase

from service.fanza import helper


class Test(TestCase):

    def test_convert_product_id_to_bongo(self):
        self.assertEqual('KMVR-579', helper.convert_product_id_to_bongo("84KMVR00579"))
        self.assertEqual('VRVR-088', helper.convert_product_id_to_bongo("H_910VRVR00088"))
        self.assertEqual('TPVR-144', helper.convert_product_id_to_bongo("H_1256TPVR00144"))
        self.assertEqual('EXBVR-021', helper.convert_product_id_to_bongo("H_1290EXBVR00021"))
        self.assertEqual('HNVR-026', helper.convert_product_id_to_bongo("HNVR00026"))
        self.assertEqual('SIVR-067', helper.convert_product_id_to_bongo("SIVR00067"))
        self.assertEqual('STARS-256', helper.convert_product_id_to_bongo("1STARS256"))
        self.assertEqual('XRW-882', helper.convert_product_id_to_bongo("84XRW882"))
        self.assertEqual('SSNI-796', helper.convert_product_id_to_bongo("SSNI796"))
        self.assertEqual('REAL-729', helper.convert_product_id_to_bongo("84REAL729"))
        self.assertEqual('SHIC-179', helper.convert_product_id_to_bongo("H_839SHIC179"))
        self.assertEqual('ZEX-387', helper.convert_product_id_to_bongo("H_720ZEX387"))
        self.assertEqual('SQTE-200', helper.convert_product_id_to_bongo("SQTE00200"))
