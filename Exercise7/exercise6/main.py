# File: main.py
# Author: Steve Hommy
# Description: Main function

import random
import os

filename = "capitals.txt"
countrys = {}

try:
    with open(filename) as f:
        for line in f:
            (key, capital) = line.split(" : ")
            (val, space) = capital.split("\n")
            countrys[key] = val
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist.\n"
    print(msg)

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))