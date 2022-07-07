import unittest
from src.main import ECB


class TestECB(unittest.TestCase):
    def test_init(self):
        key = b"1fEWUoGzMx1TwpRe1fEWUoGzMXlTwpRe"
        ecb = ECB(key)
        self.assertEqual(ecb.key, key)

    def test_encode_decode(self):
        key = b"1fEWUoGzMXITwpRe1fEWUoGzMXITwpRe"
        src1 = "encode_test"
        src2 = b"encode_test"
        ecb = ECB(key)
        encrypt_str1 = ecb.encrypt(src1)
        encrypt_str2 = ecb.encrypt(src2)
        self.assertEqual(src1, ecb.decrypt(encrypt_str1))
        self.assertEqual(src1, ecb.decrypt(encrypt_str2))
