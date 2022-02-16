# File name: exercise5_cellphoneClass.py
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
    def __str__(self):
        # Here I'm using str.format(). Using { and } to mark where a variable will be substituted and can provide detailed formatting directives
        return """
        Manufacturer: {}
        Model number: {}
        Retail price: {}
        Id number: {}
        """.format(self.__manufact, self.__model, self.__retail_price, self.__id)

        # Or you can do this using formatted string literals,
        # begin a string with f or F before the opening quotation mark or triple quotation mark.
        # Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

        # return f"""
        # Manufacturer: {self.__manufact}
        # Model number: {self.__model}
        # Retail price: {self.__retail_price}
        # Id number: {self.__id}
        # """

    # Defining Mutator Method
    def set_manufact(self):
        self.__manufact = str(input("Enter manufacturer: "))

    def set_model(self):
        self.__model = str(input("Enter model: "))

    def set_retail_price(self):
        self.__retail_price = int(input("Enter retail price: "))

    def set_id(self):
        self.__id = int(input("Enter id number between 1-6: "))
        if self.__id <= 0 or self.__id >= 7:
            print("Id must be between 1-6")
            self.set_id()

    # Defining Accessor Method
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

    def get_id(self):
        return self.__id
