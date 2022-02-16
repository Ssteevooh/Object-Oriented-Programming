# File name: exercise9_main.py
# Author: Steve Hommy
# Description: Main function file


from exercise9_carClass import Car
from exercise9_diceClass import Dice
from exercise9_mammalClass import Mammal


mammal_list = []


def new_mammal():

    ID = 0

    for i in range(int(input("How many mammals would you like to create? "))):

        mammal = input("\nEnter new object name: ")

        mammal = Mammal()
        ID += 1
        mammal.set_id(ID)
        mammal.set_species()
        mammal.set_name()
        mammal.set_size()
        mammal.set_weight()

        mammal_list.append(mammal)


# Check if the mammal fits into the car and if it does then proceedes to check weight limit
def mammal_into_trunk(mammals, car):

    if int(mammals.get_size()) <= int(car.get_size_of_trunk()):
        print(f"""Mammal will fit into the trunk, because:
The trunk size is {car.get_size_of_trunk()} and mammal size is {mammals.get_size()}\n""")

        mammal_load_limit(mammals, car)

    else:
        print(f"""Mammal will not fit into the trunk, because:
The trunk size is {car.get_size_of_trunk()} and mammal size is {mammals.get_size()}""")


def mammal_load_limit(mammals, car):

    if int(mammals.get_weight()) <= int(car.get_maximum_load_limit()):
        print(f"""Mammal does not exceed the car's load limit, because:
The car's maximum load limit is {car.get_maximum_load_limit()} and mammal weight is {mammals.get_weight()}""")

    else:
        print(f"""Mammal have exceeded the car's load limit, because:
The car's maximum load limit is {car.get_maximum_load_limit()} and mammal weight is {mammals.get_weight()}""")


def main():

    new_mammal()

    car = Car()
    car.set_make()
    car.set_model()
    car.set_milage()
    car.set_price()
    car.set_color()
    car.set_maximum_load_limit()
    car.set_size_of_trunk()

    print("\nThis is your car:")
    print(car)

    dice = Dice()
    dice.roll_the_dice()
    print("\nDice number is:", dice.get_number())

    for mammals in mammal_list:
        if dice.number == int(mammals.get_id()):
            print("\nHere is mammal based on dice roll: ")
            print(mammals)
            mammal_into_trunk(mammals, car)


main()
