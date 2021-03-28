import unittest
import csv
from Lab_3_2_3 import Person


class TestPersonClass(unittest.TestCase):

    def setUp(self):
        file = open("File_Directory.csv", "w")
        self.David = Person("David", "david@hotmail.com", 28, "Mexico")
        self.Mariana = Person("Mariana", "Mariana82@gmail.com", 25, "Mexico")
        file.close()

    def tearDown(self):   # reset to an empty file
        file = open("File_Directory.csv", "w")
        file.close()

    def test_add_new_register_delete_record(self):
        lines = list()
        self.David.add_new_register()
        with open("File_Directory.csv", 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
        self.assertEqual(lines[1], ['David', 'david@hotmail.com', '28', 'Mexico'])

        lines = list()
        self.David.delete_record()
        with open("File_Directory.csv", 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
        # means that line 'David', 'david@hotmail.com', '28', 'Mexico' does not exist on file anymore
        with self.assertRaises(IndexError):
            lines[1]

    def test_look_for(self):
        lines = list()
        self.Mariana.add_new_register()
        with open("File_Directory.csv", 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
        self.assertEqual(Person.look_for(25), lines[0])

    def test_all_records(self):
        lines = list()
        self.David.add_new_register()
        self.Mariana.add_new_register()
        with open("File_Directory.csv", 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
        self.assertEqual(Person.all_records(), [['David', 'david@hotmail.com', '28', 'Mexico'], ['Mariana', 'Mariana82@gmail.com', '25', 'Mexico']])

    def test_raise_exception_ValueError_name(self):
        with self.assertRaises(ValueError):
            self.Mariana = Person("IgnacioGustavoRaulJimenezGomez", "Ignacio56@gmail.com", 82, "Mexico")

    def test_raise_exception_TypeError_name(self):
        with self.assertRaises(TypeError):
            self.Mariana = Person("Mariana85", "Mariana82@gmail.com", 26, "Mexico")

    def test_raise_exception_ValueError_age(self):
        with self.assertRaises(ValueError):
            self.Mariana = Person("Mariana", "Mariana82@gmail.com", -5, "Mexico")

    def test_raise_exception_ValueError_email(self):
        with self.assertRaises(ValueError):
            self.Mariana = Person("Mariana", "Mariana82&gmail.com", 25, "Mexico")

    def test_raise_exception_TypeError_country(self):
        with self.assertRaises(TypeError):
            self.Mariana = Person("Mariana", "Mariana82@gmail.com", 25, "Tierra-616")


if __name__ == '__main__':
    unittest.main()
