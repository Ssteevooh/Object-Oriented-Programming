# File name: exercise7.py
# Author: Steve Hommy
# Description: Dice rolling game of three players


import random


# Creating class and initializing attributes

class Dice:
    def __init__(self):
        self.number1 = 1
        self.number2 = 1
        self.number3 = 1

    
    # Get random integer between 1 to 6 and setting the value for each player

    def player1_roll(self):
        player1_dice = random.randint(1, 6)
        self.number1 = player1_dice


    def get_player1(self):
        return int(self.number1)

    
    def player2_roll(self):
        player2_dice = random.randint(1, 6)
        self.number2 = player2_dice


    def get_player2(self):
        return int(self.number2)
    

    def player3_roll(self):
        player3_dice = random.randint(1, 6)
        self.number3 = player3_dice


    def get_player3(self):
        return int(self.number3)


# Creating three object

dice1 = Dice()
dice2 = Dice()
dice3 = Dice()

# Calling the roll function with specific object

dice1.player1_roll()
dice2.player2_roll()
dice3.player3_roll()

# Creating dictionary and adding values for players

player_dict = {"Player1": dice1.get_player1(), "Player2": dice2.get_player2(), "Player3": dice3.get_player3()}

def check_duplicates_and_remove_player():

    # While dictionary length is larger than 1 then keep running.
    # Checking equal values between players, when value is equal then roll again.
    # Player with lowest value will be removed from dictionary with pop() method

    while len(player_dict) > 1:
        print(player_dict)
        if dice1.get_player1() == dice2.get_player2():
            print("Player1 and player2 have to roll again")
            dice1.player1_roll()
            dice2.player2_roll()
            print("Player1:", dice1.get_player1())
            print("Player2:", dice2.get_player2())
            if dice1.get_player1() > dice2.get_player2():
                player_dict.pop("Player2")
            else:
                player_dict.pop("Player1")
        elif dice1.get_player1() == dice3.get_player3():
            print("Player1 and player3 have to roll again")
            dice1.player1_roll()
            dice2.player3_roll()
            print("Player1:", dice1.get_player1())
            print("Player3:", dice1.get_player3())
            if dice1.get_player1() > dice2.get_player3():
                player_dict.pop("Player3")
            else:
                player_dict.pop("Player1")
        elif dice2.get_player2() == dice3.get_player3():
            print("Player2 and player3 have to roll again")
            dice1.player2_roll()
            dice2.player3_roll()
            print("Player2:", dice2.get_player2())
            print("Player3:", dice1.get_player3())
            if dice1.get_player2() > dice2.get_player3():
                player_dict.pop("Player3")
            else:
                player_dict.pop("Player2")
        elif dice1.get_player1() == dice2.get_player2() == dice3.get_player3():
            print("All players have to roll again")
            dice1.player1_roll()
            dice1.player2_roll()
            dice2.player3_roll()
        else:

            # The min function returns the minimum value of an iterable according to the given key.
            # In this case it returns the key of player_dict with the minimum value.
            # player_dict.get allows you to access the corresponding value to the dictionary key,
            # which are iterated over when you iterate over player_dict.
            # The key argument to the min specifies what key you want to find the minimum on.

            player_dict.pop(min(player_dict, key=player_dict.get))


# Defining main

def main():

    # Calling check_duplicates_and_remove_player 

    check_duplicates_and_remove_player()

    # Iterating over dictionary keys() 

    for player in player_dict.keys():
        print("The winner is:", player)

# Calling main

main()
