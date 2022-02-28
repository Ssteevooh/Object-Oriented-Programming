# File: card.py
# Author: Steve Hommy
# Description: Create a Card Class


class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f"Card is {self.value} of {self.suit}"

    def show_card(self):
        print("{} of {}".format(self.value, self.suit))
