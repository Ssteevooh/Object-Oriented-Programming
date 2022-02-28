# File name: main.py
# Author: Steve Hommy
# Description: Main function file


from studentClass import Student
from mammalClass import Mammal
from diceClass import Dice


def dice_roll():
    global student1_dice, student2_dice

    student1_dice = 0
    student2_dice = 0

    # Looping twice and rolling the dice twice
    for i in range(0, 2):

        dice1 = Dice()
        dice2 = Dice()
        dice1.roll_the_dice()
        dice2.roll_the_dice()
        student1_dice += dice1.get_number()
        student2_dice += dice2.get_number()


# Creating dictionary where student name is the key and sum of the value is value
def student_dictionary():
    student_dict = {
        student1.get_first_name(): student1_dice,
        student2.get_first_name(): student2_dice
    }

    # looping through dictionary and printing out the key and the value
    for key in student_dict:
        print(key, "\nRolled:", student_dict[key])


def main():
    global student1, student2

    # Giving values to object
    student1 = Student("Steve", "Hommy", 1)
    student2 = Student("Tom", "Cruise", 2)
    print("Student1 status:", student1)
    print("Student2 status:", student2)

    mammal1 = Mammal("Bob", "Dog", 60, 30, 1)
    mammal2 = Mammal("Snuf", "Cat", 40, 20, 2)

    dice_roll()
    student_dictionary()

    # While the loop is true keep running until it meets break statement
    while True:
        if student1_dice == student2_dice:
            print("It's a tie. Both players have to roll again\n")
            dice_roll()
            student_dictionary()
        elif student1_dice > student2_dice:
            print(student1.get_first_name(), "Rolled higher number so it will get heavier mammal")
            print(student1.get_first_name(), "mammal is:", mammal1)
            print(student2.get_first_name(), "mammal is:", mammal2)
            break
        else:
            print(student2.get_first_name(), "Rolled higher number so it will get heavier mammal")
            print(student1.get_first_name(), "mammal is:", mammal2)
            print(student2.get_first_name(), "mammal is:", mammal1)
            break


main()
