import math
import unittest

class TestCeilMethod(unittest.TestCase):
    #default 7 places
    def test_lower_limit_float_tend_inf(self):
        self.assertAlmostEqual(math.ceil(-1.7976931348623157e+308), -1.7976931348623157e+308)

    def test_lower_limit_float_tend_0(self):
        self.assertAlmostEqual(math.ceil(-4.9406564584124654e-324), -4.9406564584124654e-324)

    def test_lower_limit_int_tend_inf(self):
        self.assertAlmostEqual(math.ceil(-1e+308), -1e+308)

    def test_lower_limit_int_tend_0(self):
        self.assertAlmostEqual(math.ceil(-4e-324), -4e-324)

    def test_0(self):
        self.assertAlmostEqual(math.ceil(0), 0)

    def test_upper_limit_int_tend_0(self):
        self.assertAlmostEqual(math.ceil(4e-324), 1)

    def test_upper_limit_int_tend_inf(self):
        self.assertAlmostEqual(math.ceil(1e+308), 1e+308)

    def test_upper_limit_float_tend_0(self):
        self.assertAlmostEqual(math.ceil(4.9406564584124654e-324), 1)

    def test_upper_limit_float_tend_inf(self):
        self.assertAlmostEqual(math.ceil(1.7976931348623157e+308), 1.7976931348623157e+308)

    def test_raise_exceptions(self):
        with self.assertRaises(TypeError):
            math.ceil('z')



if __name__ == '__main__':
    unittest.main()
