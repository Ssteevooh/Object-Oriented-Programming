# File name: exercise8.py
# Author: Steve Hommy
# Description: Simple implementation of Rock-Paper-Scissors game

# Importing module
import random


# Defining function
def rock_paper_scissors():

    player_points = 0
    computer_points = 0

    # While loop running until player or computer scores 3 points
    while True:
        player_choice = input("Give your choice (R, P, S): ")
        choices = ["R", "P", "S"]
        # random.choice returns a random element from choices
        computer_choice = random.choice(choices)
        print("Computer's choice is " + computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")

        elif player_choice == "R":
            if computer_choice == "S":
                print("Rock crushes Scissors")
                player_points += 1
            else:
                print("Paper covers Rock")
                computer_points += 1

        elif player_choice == "P":
            if computer_choice == "R":
                print("Paper covers Rock")
                player_points += 1
            else:
                print("Scissors cuts Paper")
                computer_points += 1

        elif player_choice == "S":
            if computer_choice == "P":
                print("Scissors cuts Paper")
                player_points += 1
            else:
                print("Rock crushes Scissors")
                computer_points += 1

        print("Computer " + str(computer_points) + " You " + str(player_points))

        if player_points == 3:
            print("You win!")
            break
        elif computer_points == 3:
            print("You lose!")
            break


# Calling the function
rock_paper_scissors()
