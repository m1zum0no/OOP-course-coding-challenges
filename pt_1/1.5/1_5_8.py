class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{self.goods[i].name}: {self.goods[i].price}' for i in range(len(self.goods))]

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
        
for i in ( TV("samsung", 1111), TV("LG", 1234), Table("ikea", 2345), Notebook("msi", 5433), 
            Notebook("apple", 542), Cup("keepcup", 43) ):
    cart.add(i)
    