# File: main.py
# Author: Steve Hommy
# Description: Main function

import random

filename = "Exercise7/exercise6/capitals.txt"
dictionary = {}

try:
    with open(filename) as file:
        for line in file:
            (key, value) = line.split()
            dictionary[key] = value
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist.\n"
    print(msg)

shuffle = list(dictionary.items())
random.shuffle(shuffle)
dictionary = dict(shuffle)
country_lst = list(dictionary)


print("The Capital quiz")
print("Write the capital of the country")
print()

while True:

    points = 0

    # With country lists index value checks if user input matches dictionarys
    # key value. Correct awnser gives user a point and íncorret awnser returns correct
    # awnser.

    for i in range(10):

        print(country_lst[i])

        user_input = input(": ")

        if user_input == dictionary[country_lst[i]]:
            print("Correct!")
            print()
            points += 1

        else:
            print("Wrong, correct awnser is", dictionary[country_lst[i]])
            print()

    print("Your score was", str(points) + "/10")
