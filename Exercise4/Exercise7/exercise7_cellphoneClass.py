# File name: exercise7_cellphoneClass.py
# Author: Steve Hommy
# Description: Create a CellPhone Class


# Defining class Cellphone
class Cellphone:
    # Defining method init method with private attributes
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 0
        self.__id = 0

    # Defining method str method that represents the class objects as a string
    # Defining Accessor Method
    def __str__(self):
        # Using formatted string literals
        return f"""
        Manufacturer: {self.__manufact}
        Model number: {self.__model}
        Retail price: {self.__retail_price}
        ID number: {self.__id}
        """

    # Defining Mutator Method
    def set_manufact(self):
        self.__manufact = str(input("Enter manufacturer: "))

    def set_model(self):
        self.__model = str(input("Enter model: "))

    def set_retail_price(self):
        self.__retail_price = int(input("Enter retail price: "))

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
