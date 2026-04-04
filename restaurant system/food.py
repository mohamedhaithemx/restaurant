class Menu:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name} : {self.price}"

class MainDish(Menu):
    ...

class Extra(Menu):
    ...

class Table:    
    #class variable
    menu={"Main":[MainDish("meet",280),MainDish("chicken",185),MainDish("rise",30),MainDish("pasta",80)],"Extra":[Extra("water",15),Extra("tea",8)]}
    #instance variable
    def __init__(self, number): 
        self.number = number
        self._price = 0
        self.order = []
        self.vip = False

    @property
    def price(self):
        if self.vip:
            return self._price * 0.9
        return self._price
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("price not correct")
        self._price += price
 
    def add(self, name, price):
        self.order.append((name, price))
        self.price = price

    def __str__(self):
        return f"\ntable: {self.number}\norder: {' '.join([f'{name}: {price}' for name, price in self.order])}\ntotal: {self.price}"
    
    def check(self):
        print(self)
        self.order = []
        self._price = 0
        print("checkout successfully")
        print(self)

        
#-------------------------------
class Hall:
    def __init__(self,number):
        self.number=number
        self.tables=[Table(i)for i in range(1,6)]

# hi git