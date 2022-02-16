# File name: exercise9_carClass.py
# Author: Steve Hommy
# Description: Create a Car Class# File name: exercise8_carClass.py


# Defining class Car
class Car:
    def __init__(self):
        # Defining method init method with private attributes
        self.__make = ""
        self.__model = ""
        self.__mileage = 0
        self.__price = 0
        self.__color = ""
        self.__maximum_load_limit = 0
        self.__size_of_trunk = 0

    # Defining method str method that represents the class objects as a string
    def __str__(self):
        return f"""
        Make: {self.__make}
        Model: {self.__model}
        Mileage: {self.__mileage}
        Price: {self.__price}
        Color: {self.__color}
        Maximum load limit: {self.__maximum_load_limit}
        Size of trunk: {self.__size_of_trunk}
        """

    # Defining Mutator Methods
    def set_make(self):
        self.__make = input("\nEnter car maker: ")

    def set_model(self):
        self.__model = input("Enter car model: ")

    def set_milage(self):
        self.__mileage = int(input("Enter mileage of the car: "))

    def set_price(self):
        self.__price = int(input("Enter price of the car: "))

    def set_color(self):
        self.__color = input("Enter car color: ")

    def set_maximum_load_limit(self):
        self.__maximum_load_limit = input("Enter maximum load limit for the car: ")

    def set_size_of_trunk(self):
        self.__size_of_trunk = input("Enter size of the trunk for the car: ")

    # All of the get methods.
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_milage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_maximum_load_limit(self):
        return self.__maximum_load_limit

    def get_size_of_trunk(self):
        return self.__size_of_trunk
