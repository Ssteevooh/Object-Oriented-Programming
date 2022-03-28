# File: main.py
# Author: Steve Hommy
# Description: Main function

import random

filename = "Exercise8/exercise6/capitals.txt"
dictionary = {}

try:
    with open(filename) as file:
        for line in file:
            (key, value) = line.split()
            dictionary[key] = value
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist.\n"
    print(msg)

try:
    while True:
        points = 0
        for i in range(10):
            country, capital = random.choice(list(dictionary.items()))
            print(country)
            answer = input("Give capital: ")
            if answer == dictionary[country]:
                print("Correct!\n")
                points += 1
            else:
                print("Wrong answer the correct answer is:", dictionary[country])
                print()

        print("Score:\n" + str(points) + "/10")
        break
except TypeError:
    print("Input must be a string")
