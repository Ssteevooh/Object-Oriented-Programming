# File name: vehicleClass.py
# Author: Steve Hommy
# Description: Create a Vehicle Class


class Vehicle:
    def __init__(self, brand, tyre, body_style, zero_to_hundred):
        self.__brand = brand
        self.__tyre = tyre
        self.__body_style = body_style
        self.__zero_to_hundred = float(zero_to_hundred)

    def __str__(self):
        return f"""
        Brand: {self.__brand}
        Tyre: {self.__tyre}
        Body style: {self.__body_style}
        0 to 100 in: {self.__zero_to_hundred} seconds
        """

    def set_brand(self, brand):
        self.__brand = brand

    def set_tyre(self, tyre):
        self.__tyre = tyre

    def set_body_style(self, body_style):
        self.__body_style = body_style

    def set_zero_to_hundred(self, zero_to_hundred):
        self.__zero_to_hundred = zero_to_hundred

    def get_brand(self):
        return self.__brand

    def get_tyre(self):
        return self.__tyre

    def get_body_style(self):
        return self.__body_style

    def get_zero_to_hundred(self):
        return self.__zero_to_hundred
