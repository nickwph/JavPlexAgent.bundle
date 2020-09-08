from unittest import TestCase

import fanza_helper


class Test(TestCase):

    def test_convert_product_id_to_bongo(self):
        self.assertEqual('KMVR579', fanza_helper.convert_product_id_to_bongo("84KMVR00579"))
        self.assertEqual('VRVR088', fanza_helper.convert_product_id_to_bongo("H_910VRVR00088"))
        self.assertEqual('TPVR144', fanza_helper.convert_product_id_to_bongo("H_1256TPVR00144"))
        self.assertEqual('EXBVR021', fanza_helper.convert_product_id_to_bongo("H_1290EXBVR00021"))
        self.assertEqual('HNVR026', fanza_helper.convert_product_id_to_bongo("HNVR00026"))
        self.assertEqual('SIVR067', fanza_helper.convert_product_id_to_bongo("SIVR00067"))
        self.assertEqual('STARS256', fanza_helper.convert_product_id_to_bongo("1STARS256"))
        self.assertEqual('XRW882', fanza_helper.convert_product_id_to_bongo("84XRW882"))
        self.assertEqual('SSNI796', fanza_helper.convert_product_id_to_bongo("SSNI796"))
        self.assertEqual('REAL729', fanza_helper.convert_product_id_to_bongo("84REAL729"))
        self.assertEqual('SHIC179', fanza_helper.convert_product_id_to_bongo("H_839SHIC179"))
        self.assertEqual('ZEX387', fanza_helper.convert_product_id_to_bongo("H_720ZEX387"))
        self.assertEqual('SQTE200', fanza_helper.convert_product_id_to_bongo("SQTE00200"))

