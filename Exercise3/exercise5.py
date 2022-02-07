# File name: exercise5.py
# Author: Steve Hommy
# Description: Dice roller


import random


# Class definition and initializing attributes.

class Dice:
    def __init__(self):
        self.number = 1
        self.color = "Black"
        self.icon = "⚀"
    

    # Defining roll_the_dice. Getting random integer between 1 to 6.
    # Using if, elif and else statment to choose specific value

    def roll_the_dice(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            self.number = 1
            self.color = "Black"
            self.icon = "⚀"
        elif random_number == 2:
            self.number = 2
            self.color = "White"
            self.icon = "⚁"
        elif random_number == 3:
            self.number = 3
            self.color = "Green"
            self.icon = "⚂"
        elif random_number == 4:
            self.number = 4
            self.color = "Yellow"
            self.icon = "⚃"
        elif random_number == 5:
            self.number = 5
            self.color = "Red"
            self.icon = "⚄"
        else:
            self.number = 6
            self.color = "Blue"
            self.icon = "⚅"


    # Defining functions and returning their values

    def get_number(self):
        return self.number
    

    def get_color(self):
        return self.color

    
    def get_icon(self):
        return self.icon

# Defining main

def main():

    # Creating object and calling the functions

    dice = Dice()
    dice.roll_the_dice()
    print("Rolling the dice…")
    print("Number:", dice.get_number())
    print("Color:", dice.get_color())
    print("Icon:", dice.get_icon())

main()
