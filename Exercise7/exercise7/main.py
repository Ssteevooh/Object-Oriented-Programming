# File: main.py
# Author: Steve Hommy
# Description: Main function


from petrolVehicle import PetrolVehicle
from electricVehicle import ElectricVehicle


def main():
    honda = PetrolVehicle("Honda", "Continental", "Hatchback", 8.5, "1.6l", "100l")
    tesla = ElectricVehicle("Tesla", "Nokia", "Sedan", 4.5, "250W", "1000 000A")

    print("Our first car is:", honda)
    print("Our second car is:", tesla)

    how_fast_dict = {
        honda.get_brand(): honda.get_zero_to_hundred(),
        tesla.get_brand(): tesla.get_zero_to_hundred()
    }

    for key in how_fast_dict:
        print(key, "will reach 0 to 100 in", how_fast_dict[key], "seconds")


main()
