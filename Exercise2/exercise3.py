# File name: exercise1.py
# Author: Steve Hommy
# Description: Pseudocode where user inputs the exercise points and program prints out the grade.


# User inputs points
points = int(input("Insert maximum points: "))
# Printing out grade 
if points < 60:
    print("Grade 0")
elif points == 60:
    print("Grade 1")
elif points <= 72:
    print("Grade 2")
elif points <= 84:
    print("Grade 3")
elif points <= 96:
    print("Grade 4")
else:
    print("Grade 5")
