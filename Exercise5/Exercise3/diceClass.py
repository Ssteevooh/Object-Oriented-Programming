# File name: diceClass.py
# Author: Steve Hommy
# Description: Create a Dice Class


import random


class Dice:
    def __init__(self):
        self.number = 1

    def roll_the_dice(self):
        random_number = random.randint(1, 6)
        self.number = random_number

    def get_number(self):
        return self.number
