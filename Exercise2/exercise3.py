# File name: exercise3.py
# Author: Steve Hommy
# Description: Pseudocode where user inputs the exercise points and program prints out the grade


def grade_calculator():
    while True:
        try:
            points = int(input("Insert exercise points: "))
            if points < 0 or points > 120:
                raise ValueError
            break
        except ValueError:
            print("Error: exercise points cannot be < 0 or > 120.")
    if points >= 108:
        print("Grade 5")
    elif points >= 96:
        print("Grade 4")
    elif points >= 84:
        print("Grade 3")
    elif points >= 72:
        print("Grade 2")
    elif points >= 60:
        print("Grade 1")
    else:
        print("Grade 0")

grade_calculator()

