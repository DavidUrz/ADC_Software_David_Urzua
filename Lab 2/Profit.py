# Profit David Urzúa A00354893
class Product:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def profit(self):
        try:
            prof = (self.dictionary.get("sell_price") - self.dictionary.get("cost_price")) * self.dictionary.get("inventory")
            prof_round = round(prof, 0)
            return (prof_round)
        except TypeError:
            print("Error in data value in dictionary")


if __name__ == '__main__':
    products = {"A2C8012810": ({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}),
                "A2C2182809": ({"cost_price": 83.90, "sell_price": 93.13, "inventory": 913}),
                "A2C0192830": ({"cost_price": 71.8, "sell_price": 75.02, "inventory": 820}),
                "A2C1872038": ({"cost_price": 12.82, "sell_price": 23.90, "inventory": 1384}),
                "A2C1029380": ({"cost_price": 27.85, "sell_price": 34.12, "inventory": 831}),
                "A2C1293087": ({"cost_price": 87.61, "sell_price": 98.32, "inventory": 1989}),
                "A2C1084894": ({"cost_price": 28.23, "sell_price": 36.83, "inventory": 842}),
                "A2C4892900": ({"cost_price": 17.45, "sell_price": 20.46, "inventory": 12039}),
                "A2C8834971": ({"cost_price": 17.71, "sell_price": 24.45, "inventory": 313}),
                "A2C9251887": ({"cost_price": 6.12, "sell_price": 10.88, "inventory": 931}),
                "A2C9251865": ({"cost_price": 99.99, "sell_price": 108.6, "inventory": "646"})}

    for product_id, product_info in products.items():
        exec("product_{} = Product({})".format(product_id, product_info))

    print(product_A2C8012810.profit())
    print(product_A2C2182809.profit())
    print(product_A2C0192830.profit())
    print(product_A2C1872038.profit())
    print(product_A2C1029380.profit())
    print(product_A2C1293087.profit())
    print(product_A2C1084894.profit())
    print(product_A2C4892900.profit())
    print(product_A2C8834971.profit())
    print(product_A2C9251887.profit())
    print(product_A2C9251865.profit())
