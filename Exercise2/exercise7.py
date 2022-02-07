# File name: exercise7.py
# Author: Steve Hommy
# Description: Coin tosser

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'


    def toss_the_coin(self):
        random_number = random.randint(0,4)
        
        if random_number == 0:
            self.sideup = 'Heads'
        elif random_number == 1:
            self.sideup = 'Tails'
        elif random_number == 2:
            self.sideup = "Coin lands on the table upright"
        elif random_number == 3:
            self.sideup = "coin drops on the ground and disappears on a rabbit hole"
        else:
            print("Coin defies gravity and gets lost on a wormhole in space")
            exit()
            

    def get_sideup(self):
        return self.sideup

# Main function definition

def main():

    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())


# Calling the main function
main()
