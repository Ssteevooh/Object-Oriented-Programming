# File name: exercise9.py
# Author: Steve Hommy
# Description: Function that returns a random number between 1-6 when calling it.

# Importing module
import random


# Defining function
def random_number(x, y):
    # random.randint return a random integer between x = 1 y = 6
    print("Random number is: " + str(random.randint(x, y)))


# Calling the function
random_number(1, 6)
