# David Urzua A00354893
def convert2bin(number):
    try:
        number = int(number)
        if number >= 0:
            quotient = number
            residue = []
            if quotient != 0:
                while quotient >= 1:
                    x = divmod(quotient, 2)
                    quotient = x[0]
                    residue.append(x[1])
                residue.reverse()
                residueStr = [str(integer) for integer in residue]
                joinedStr = "".join(residueStr)
            else:
                joinedStr = str(0)
            return joinedStr
        else:
            print("Sorry number below 0")
            raise ValueError
    except ValueError:
        print("Sorry number invalid")
        raise SystemExit


def convert2hex(number):
    try:
        # if type(number) == 'float':
        #     print("num float")
        number = int(number)
        if number >= 0:
            dictHex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
            quotient = number
            residue = []
            if quotient != 0:
                while quotient >= 1:
                    x = divmod(quotient, 16)
                    quotient = x[0]
                    if x[1] >= 10:
                        hexStr = dictHex[x[1]]
                    else:
                        hexStr = x[1]
                    residue.append(hexStr)
                residue.reverse()
                residueStr = [str(integer) for integer in residue]
                joinedStr = "".join(residueStr)
            else:
                joinedStr = str(0)
            return joinedStr
        else:
            print("Sorry number below 0")
            raise ValueError
    except ValueError:
        print("Sorry number invalid")
        raise SystemExit


# number = input("Enter int number to convert: ")
# print("Number in hex: ", convert2hex(number))
