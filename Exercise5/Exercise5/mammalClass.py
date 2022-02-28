# File name: mammalClass.py
# Author: Steve Hommy
# Description: Create a Mammal Class


class Mammal:
    def __init__(self, name, species, size, weight, id):
        self.__name = name
        self.__species = species
        self.__size = int(size)
        self.__weight = int(weight)
        self.__id = int(id)

    def __str__(self):
        return f"""
        Name: {self.__name}
        Species: {self.__species}
        Size: {self.__size}
        Weight: {self.__weight}
        ID: {self.__id}
        """

    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        self.__species = species

    def set_size(self, size):
        self.__size = size

    def set_weight(self, weight):
        self.__weight = weight

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def get_id(self):
        return self.__id
