class Computer:                             # Defineeri klass

    def __init__(self):                     # Loo constructor
        self.__sellingprice = 700

    def sell(self):                          # 3. ja 4. defineeri ja väärtusta väljad
        print(f"Selling Price: {self.__sellingprice}")

    def setSellingPrice(self, price):           # 5. tee midagi kasulikku
        self.__sellingprice = price

c = Computer()
c.sell()

# change the price
c.__sellingprice = 1000
c.sell()

# setting selling price using setter function
c.setSellingPrice(1000)
c.sell()


if __name__ == '__main__':
    """Selling Price: 700
    Selling Price: 700
    Selling Price: 1000"""