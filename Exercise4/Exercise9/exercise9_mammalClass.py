# File name: exercise9_mammalClass.py
# Author: Steve Hommy
# Description: Create a Mammal Class


class Mammal:
    def __init__(self):
        self.__id = 0
        self.__species = ""
        self.__name = ""
        self.__size = 0
        self.__weight = 0

    def __str__(self):
        return f"""
        ID: {self.__id}
        Species: {self.__species}
        Name: {self.__name}
        Size: {self.__size}
        Weight: {self.__weight}
        """

    def set_id(self, id):
        self.__id = id

    def set_species(self):
        self.__species = str(input("Enter species: "))

    def set_name(self):
        self.__name = str(input("Enter name: "))

    def set_size(self):
        self.__size = int(input("Enter size: "))

    def set_weight(self):
        self.__weight = int(input("Enter weight: "))

    def get_id(self):
        return self.__id

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight
