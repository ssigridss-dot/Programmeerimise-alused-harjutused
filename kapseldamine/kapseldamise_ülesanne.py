class Computer:  # 1. defineeri klass

    def __init__(self):  # 2. loome konstruktori
        self.__sellingprice = 700  # 3. Defineeri ja 4. väärtusta väljad
        self.public_price = 1000

    def sell(self):  # 5. tee midagi kasulikku
        print("Selling Price: {}".format(self.__sellingprice))
        print("Public Price: {}".format(self.public_price))

    def set_selling_price(self, price):
        if price < 0:
            raise Exception("Sorry can't sell negative price")
        self.__sellingprice = price

if __name__ == '__main__':
    c = Computer()
    c.sell()

    # change the price
    c.__sellingprice = 1000
    c.public_price = 200
    c.sell()

    # setting selling price using setter function
    c.set_selling_price(1000)
    c.sell()