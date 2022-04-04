# File: main.py
# Author: Steve Hommy
# Description: Main function

def zeroDiv(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def valEr(var):
    try:
        return int(var)
    except ValueError:
        print("The argument does not contain numbers")

def naEr(name):
    try:
        print(name)
    except NameError:
        print("Variable is not defined")

