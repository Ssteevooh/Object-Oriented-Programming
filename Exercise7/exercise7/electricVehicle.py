# File name: electricVehicle.py
# Author: Steve Hommy
# Description: Inherit Vehicle Class and creating ElectricVehicle Class


from vehicle import Vehicle


class ElectricVehicle(Vehicle):
    def __init__(self, brand, tyre, body_style, zero_to_hundred, electric_power, battery_size):
        Vehicle.__init__(self, brand, tyre, body_style, zero_to_hundred)
        self.__electric_power = electric_power
        self.__battery_size = battery_size

    def __str__(self):
        return super().__str__() + f"""Electric power: {self.__electric_power}
        Battery size: {self.__battery_size}
        """

    def set_electric_power(self, electric_power):
        self.__electric_power = electric_power

    def set_battery_size(self, battery_size):
        self.__battery_size = battery_size

    def get_electric_power(self):
        return self.__electric_power

    def get_battery_size(self):
        return self.__battery_size
