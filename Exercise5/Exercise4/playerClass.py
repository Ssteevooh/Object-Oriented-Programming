# File name: playerClass.py
# Author: Steve Hommy
# Description: Create a Player Class


class Player:
    def __init__(self, first_name, last_name, id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = int(id)

    def __str__(self):
        return f"""
        First name: {self.__first_name}
        Last name: {self.__last_name}
        ID: {self.__id}
        """

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_id(self, id):
        self.__id = id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_id(self):
        return self.__id
