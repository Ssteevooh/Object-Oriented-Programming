# File name: exercise9.py
# Author: Steve Hommy
# Description: Function that returns a random number between 1-6 when calling it.

# Importing module
import random


# Defining function
def random_number():
    # random.randint return a random integer between 1 to 6
    return random.randint(1, 6)

# Calling the function
print(random_number())
