# File name: petrolVehicle.py
# Author: Steve Hommy
# Description: Inherit Vehicle Class and creating PetrolVehicle Class


from vehicleClass import Vehicle


class PetrolVehicle(Vehicle):
    def __init__(self, brand, tyre, body_style, zero_to_hundred, engine_size, tank_size):
        Vehicle.__init__(self, brand, tyre, body_style, zero_to_hundred)
        self.__engine_size = engine_size
        self.__tank_size = tank_size

    def __str__(self):
        return super().__str__() + f"""Engine size: {self.__engine_size}
        Tank size: {self.__tank_size}
        """

    def set_engine_size(self, engine_size):
        self.__engine_size = engine_size

    def set_tank_size(self, tank_size):
        self.__tank_size = tank_size

    def get_engine_size(self):
        return self.__engine_size

    def get_tank_size(self):
        return self.__tank_size
