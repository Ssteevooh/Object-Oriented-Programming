# File name: main.py
# Author: Steve Hommy
# Description: Main function file


from playerClass import Player
from diceClass import Dice


def main():

    # Giving values to object
    player1 = Player("Steve", "Hommy", 1)
    player2 = Player("Tom", "Cruise", 2)
    print("Player1 status:", player1)
    print("Player2 status:", player2)

    dice1 = Dice()
    dice2 = Dice()
    dice1.roll_the_dice()
    dice2.roll_the_dice()
    print("Player1 and player2 roll their dices...\n")

    # Creating dictionary where player id is the key and dice number is value
    player_dict = {
        player1.get_id(): dice1.get_number(),
        player2.get_id(): dice2.get_number()
    }

    # looping through dictionary and printing out the key and the value
    for key in player_dict:
        print("player with ID:", key, "\nRolled:", player_dict[key])


main()
