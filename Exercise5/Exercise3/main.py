# File name: main.py
# Author: Steve Hommy
# Description: Main function file


from diceClass import Dice


number_of_dices = int(input("How many dices will be rolled? "))


# Rolling the dice and then looping through the list
def player1_roll():

    global player1_dice
    print("Player1 rolling...")
    print("Player1 dices are")
    player1_dice = []
    for i in range(number_of_dices):
        dice1 = Dice()
        dice1.roll_the_dice()
        player1_dice.append(dice1.number)
    for dices1 in player1_dice:
        print(dices1, end=" ")


def player2_roll():

    global player2_dice
    print("\n\nPlayer2 rolling...")
    print("Player2 dices are")
    player2_dice = []
    for i in range(number_of_dices):
        dice2 = Dice()
        dice2.roll_the_dice()
        player2_dice.append(dice2.number)
    for dices2 in player2_dice:
        print(dices2, end=" ")


# Sum the list
def player1_dice_sum():

    player1_sum_of_dices = sum(player1_dice)
    print("\n\nPlayer1 sum of dices are", player1_sum_of_dices)
    return player1_sum_of_dices


def player2_dice_sum():

    player2_sum_of_dices = sum(player2_dice)
    print("Player2 sum of dices are", player2_sum_of_dices)
    return player2_sum_of_dices


# While the loop is true keep running until it meets break statement
def main():

    while True:
        player1_roll()
        player2_roll()
        if player1_dice_sum() == player2_dice_sum():
            print("It's a tie. Both players have to roll again\n")
        elif player1_dice_sum() > player2_dice_sum():
            print("Player1 has won!")
            break
        else:
            print("Player2 has won!")
            break


main()
