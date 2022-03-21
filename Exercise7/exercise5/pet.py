# File name: pet.py
# Author: Steve Hommy
# Description: Create a Pet Class


class Pet:
    def __init__(self, species, name, pet_size):
        self.__species = species
        self.__name = name
        self.__pet_size = pet_size
        self.__owner = None

    def set_species(self):
        self.__species = input("Give species for pet: ")

    def get_species(self):
        return self.__species

    def set_name(self):
        self.__name = input("Give name for pet: ")

    def get_name(self):
        return self.__name

    def set_pet_size(self):
        self.__pet_size = int(input("Size of the pet"))

    def get_pet_size(self):
        return self.__pet_size

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def __str__(self):
        return f"""
        Species of the pet: {self.__species}
        Name of the pet: {self.__name}
        Size of the pet: {self.__pet_size}
        Owner of the pet: {self.__owner}"""
