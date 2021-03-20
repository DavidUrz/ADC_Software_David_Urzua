import filecmp
import unittest


class TestCmpMethod(unittest.TestCase):

    def setUp(self):
        self.file_1 = "Limites_DCU.csv"
        self.file_1_copy = "Limites_DCU - copia.csv"
        self.file_2 = "Limites_DCU_5.csv"
        self.file_3_not_exist = "Limites_DCU_X.csv"

    def tearDown(_):
        filecmp.clear_cache()

    def test_positive(self):
        self.assertTrue(filecmp.cmp(self.file_1, self.file_1_copy), True)

    def test_negative(self):
        self.assertFalse(filecmp.cmp(self.file_1, self.file_2), False)

    def test_optional_param_false(self):
        self.assertTrue(filecmp.cmp(self.file_1, self.file_1_copy, False), True)

    def test_raise_exception(self):
        with self.assertRaises(FileNotFoundError):
            filecmp.cmp(self.file_1, self.file_3_not_exist)


if __name__ == '__main__':
    unittest.main()
