# File name: exercise4_main.py
# Author: Steve Hommy
# Description: Main function for CellPhone Class

# Importing Cellphone class into main file
from exercise4_cellphoneClass import Cellphone


def main():
    cellphone = Cellphone()
    cellphone.set_manufact()
    cellphone.set_model()
    cellphone.set_retail_price()

    print("Here is the data that you provided:")

    print("Manufacturer:", cellphone.get_manufact())
    print("Model number:", cellphone.get_model())
    print("Retail price:", cellphone.get_retail_price())


main()
