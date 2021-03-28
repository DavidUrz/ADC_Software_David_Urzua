# Python failing David Urzúa A00354893

def str_to_int(string=None):   # number format string "90"-> 90
    try:
        if string is None:     # if function argument is empty raise error
            raise TypeError("Number is empty")
        else:
            if string.find("-") == 0:  # Check if string is negative
                flagNegative = 1
                string = string.replace("-", "")
            else:
                flagNegative = 0
            if string.isnumeric():  # Check if the string is 0-9
                n = 0
                for i in string:
                    n = n * 10 + (ord(i) - 48)
                if flagNegative == 1:
                    return n * -1
                else:
                    return n
            else:
                print("Not a integer")
    except TypeError:
        print("Number is empty")
    except AttributeError:
        print("Not a string ")


def int_to_str(number=None):   # number 57 -> "57"
    try:
        if number is None:    # if function argument is empty raise error
            raise TypeError("Number is empty")
        else:
            if number < 0:     # Manage negative numbers
                number = number * -1
                flagNegative = 1
            else:
                flagNegative = 0
            string = ""
            while True:
                number, remainder = divmod(number, 10)
                string = chr(ord("0") + remainder) + string
                if number == 0:
                    break
            if flagNegative == 1:
                string = "-" + string
                return string
            else:
                return string
    except (TypeError, NameError):
        print("Not an integer to convert")


print("\nTests str_to_int\n")
print("Positive tests ")
print(str_to_int("78697047"))
print(str_to_int("000"))
print(str_to_int("-1"))
print("Negative tests")
print(str_to_int("b"))
print(str_to_int("2.56"))
print(str_to_int("-3.8"))
print(str_to_int(9))
print(str_to_int(2.7))
print(str_to_int())
print(str_to_int(-2.4))

print("\nTests int_to_str\n")
print("Positive tests ")
print(int_to_str(8))
print(int_to_str(00))
print(int_to_str(9908098))
print(int_to_str(-1))
print("Negative tests")
print(int_to_str(9.0))
print(int_to_str(-8.7))
print(int_to_str("24"))
print(int_to_str("-2"))
print(int_to_str(-0.1))
print(int_to_str("bo"))
print(int_to_str())
