# File name: exercise6_main.py
# Author: Steve Hommy
# Description: Main function for CellPhone Class

# Importing Cellphone class into main file
from exercise6_cellphoneClass import Cellphone


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

    print("Here is the data that you provided:")

    for cellphones in cellphone_list:
        print(cellphones)


main()
