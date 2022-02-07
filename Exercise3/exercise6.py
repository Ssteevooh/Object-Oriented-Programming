# File name: exercise6.py
# Author: Steve Hommy
# Description: Sum of 2 dice value

import random


# Class definition and initializing attributes.

class Dice:
    def __init__(self):
        self.number = 1

    
    # Defining roll_the_dice for 2 dice where they get random integer between 1 to 6
    # and returning their values

    def roll_the_dice1(self):
        random_number = random.randint(1, 6)
        self.number = random_number    

    
    def get_dice1(self):
        return self.number


    def roll_the_dice2(self):
        random_number = random.randint(1, 6)
        self.number = random_number

    
    def get_dice2(self):
        return self.number


def main():

    # Creating 2 objects, calling the functions and sum of two dice

    dice1 = Dice()
    dice2 = Dice()
    dice1.roll_the_dice1()
    dice2.roll_the_dice2()
    print("Rolling the dice1…\nNumber:", dice1.get_dice1())
    print("Rolling the dice2…\nNumber:", dice2.get_dice2())
    print("The sum is:", int(dice1.get_dice1()) + int(dice2.get_dice2()))

main()
