# File name: car.py
# Author: Steve Hommy
# Description: Create a Car Class


class Car:
    def __init__(self, brand, model, boot_size):
        self.__brand = brand
        self.__model = model
        self.__boot_size = boot_size
        self.__owner = None

    def set_brand(self):
        self.__brand = input("What brand is the car? ")

    def get_brand(self):
        return self.__brand

    def set_model(self):
        self.__model = input("What model is the car? ")

    def get_model(self):
        return self.__model

    def set_boot_size(self):
        self.__boot_size = int(input("What is the boot size? "))

    def get_boot_size(self):
        return self.__boot_size

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def __str__(self):
        return f"""
        Brand: {self.__brand}
        Model: {self.__model}
        Boot size: {self.__boot_size}
        Owner: {self.__owner}
        """
