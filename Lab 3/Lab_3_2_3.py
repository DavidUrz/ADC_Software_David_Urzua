import re
import csv


class Person:

    file_name = "File_Directory.csv"
    already = None

    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = int(age)
        self.country = country

        if not Person.already:
            with open(Person.file_name, 'a', newline='') as my_file:
                fieldnames = ["name", "email", "age", "country"]
                writer = csv.DictWriter(my_file, fieldnames=fieldnames)
                writer.writeheader()
            Person.already = True

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    @property
    def country(self):
        return self._country

    @name.setter
    def name(self, value):
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        for a in value:
            if a.isnumeric() is True:
                raise TypeError("Name cannot contain a number")
        self._name = value

    @email.setter
    def email(self, value):
        regex = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("Not correct format email address.")
        self._email = value

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @country.setter
    def country(self, value):
        for a in value:
            if a.isnumeric() is True:
                raise TypeError("Country cannot contain a number")
        self._country = value

    def add_new_register(self):
        with open(Person.file_name, 'a', newline='') as my_file:
            fieldnames = ["name", "email", "age", "country"]
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)
            writer.writerow({"name": self.name, "email": self.email, "age": self.age, "country": self.country})

    def delete_record(self):
        lines = list()
        with open(Person.file_name, 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
                for field in row:
                    if field == self.name:
                        lines.remove(row)
        with open(Person.file_name, 'w', newline='') as out:
            writer = csv.writer(out)
            writer.writerows(lines)

    @staticmethod
    def look_for(arg):
        arg = str(arg)
        lines = list()
        with open(Person.file_name, 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
                for field in row:
                    if field == arg:
                        return row

    @staticmethod
    def all_records():
        lines = list()
        with open(Person.file_name, 'r') as inp:
            for row in csv.reader(inp):
                lines.append(row)
        # print(lines)
        return lines
