# File name: exercise4_cellphoneClass.py
# Author: Steve Hommy
# Description: Create a CellPhone Class


class Cellphone:
    def __init__(self):
        self.manufact = ""
        self.model = ""
        self.retail_price = 0

    def set_manufact(self):
        self.manufact = str(input("Enter manufacturer: "))

    def set_model(self):
        self.model = str(input("Enter model: "))

    def set_retail_price(self):
        self.retail_price = int(input("Enter retail price: "))

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price
