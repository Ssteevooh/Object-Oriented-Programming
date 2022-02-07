# File name: exercise2-4.py
# Author: Steve Hommy
# Description: Coin tosser

import random

# Class definition and initializing attributes. sideup attribute is private

class Coin:
    def __init__(self):
        self.__sideup = "Heads"
        self.currency = "Euro"


    # Defining toss_the_coin
    # Getting random integer between 0 to 4
    # If value is 0 sideup is heads, elif 1 sideup is tails, elif 2 sideup is Coin lands on the table upright,
    # elif 3 sideup is coin drops on the ground and disappears on a rabbit hole
    # else Coin defies gravity and gets lost on a wormhole in space

    def toss_the_coin(self):
        random_number = random.randint(0,4)
        
        if random_number == 0:
            self.__sideup = "Heads"
        elif random_number == 1:
            self.__sideup = "Tails"
        elif random_number == 2:
            self.__sideup = "Coin lands on the table upright"
        elif random_number == 3:
            self.__sideup = "coin drops on the ground and disappears on a rabbit hole"
        else:
            self.__sideup = "Coin defies gravity and gets lost on a wormhole in space"
            
            
    # Defining get_sideup and returning sideup value

    def get_sideup(self):
        return self.__sideup


    # Defining generate_the_currency.
    # List of different currency and return randomly selected element using choice() method

    def generate_the_currency(self):
        random_currency = random.choice(["Euro", "Pound", "Dollar", "Ruble", "Yen"])
        self.currency = random_currency


    # Defining get_currency and returning currency value

    def get_currency(self):
        return self.currency

# Main function definition

def main():

    # Creating object and calling the functions

    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Original currency", my_coin.get_currency())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

    my_coin.generate_the_currency()

    print("Currency is:", my_coin.get_currency())

# Calling the main function

main()
