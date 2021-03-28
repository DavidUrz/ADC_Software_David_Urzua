import unittest
from convert2X import convert2bin
from convert2X import convert2hex


class TestConvert2XMethod(unittest.TestCase):

    def test_convert2bin_positve(self):
        self.assertEqual(convert2bin(89), "1011001")

    def test_convert2hex_positive(self):
        self.assertEqual(convert2hex(46168), "B458")

    def test_convert2bin_string(self):
        self.assertEqual(convert2bin("82"), "1010010")

    def test_convert2hex_string(self):
        self.assertEqual(convert2hex("53"), "35")

    def test_convert2bin_0(self):
        self.assertEqual(convert2bin(0), "0")

    def test_convert2hex_0(self):
        self.assertEqual(convert2hex(0), "0")

    def test_raise_exception_2bin(self):
        with self.assertRaises(SystemExit):
            convert2bin("so")

    def test_raise_exception_2hex(self):
        with self.assertRaises(SystemExit):
            convert2hex("so")

    def test_raise_exception_2bin_negative_number(self):
        with self.assertRaises(SystemExit):
            convert2bin(-9)

    def test_raise_exception_2hex_negative_number(self):
        with self.assertRaises(SystemExit):
            convert2hex(-9)

    def test_raise_exception_2bin_float_number(self):
        with self.assertRaises(SystemExit):
            convert2bin("5.5")

    def test_raise_exception_2hex_float_number(self):
        with self.assertRaises(SystemExit):
            convert2hex("5.5")


if __name__ == '__main__':
    unittest.main()
