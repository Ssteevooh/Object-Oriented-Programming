# File name: exercise7_main.py
# Author: Steve Hommy
# Description: Main function file

# Importing Cellphone and Dice class into main file
from exercise7_cellphoneClass import Cellphone
from exercise7_diceClass import Dice


cellphone_list = []


def new_cellphone():

    ID = 0

    for i in range(int(input("How many cellphones would you like to create? "))):

        # Creating new objects
        cellphone = input("\nEnter new object name: ")

        cellphone = Cellphone()
        cellphone.set_manufact()
        cellphone.set_model()
        cellphone.set_retail_price()
        ID += 1
        cellphone.set_id(ID)

        cellphone_list.append(cellphone)


def main():

    new_cellphone()
    dice = Dice()
    dice.roll_the_dice()
    print("\nDice number is:", dice.get_number())

    print("\nHere is the data that you provided:")

    for cellphones in cellphone_list:
        print(cellphones)

    print("Here is cellphone based on dice roll: ")

    for cellphones in cellphone_list:
        if dice.number == int(cellphones.get_id()):
            print(cellphones)


main()
