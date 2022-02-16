# File name: exercise9_diceClass.py
# Author: Steve Hommy
# Description: Create a Dice Class


import random


# Class definition and initializing attributes.
class Dice:
    def __init__(self):
        self.number = 1

    # Defining roll_the_dice. Getting random integer between 1 to 6.
    # Using if, elif and else statment to choose specific value
    def roll_the_dice(self):
        random_number = random.randint(1, 6)
        self.number = random_number

    # Defining functions and returning their values
    def get_number(self):
        return self.number
