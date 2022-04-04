# File: main.py
# Author: Steve Hommy
# Description: Main function

def zeroDiv(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Zero div error")

def valEr(var):
    try:
        return int(var)
    except ValueError:
        print("The argument does not contain numbers")

def naEr():
    try:
        print(x)
    except NameError:
        print("Variable is not defined")

def fiEr():
    try:
        with open("filename"):
            print("File found")
    except FileNotFoundError:
        print("Sorry, the file does not exist")

def keyInt():
    try:
        x = input("Try using KeyboardInterrupt: ")
    except KeyboardInterrupt:
        print ("KeyboardInterrupt exception is caught")
    else:
        print ("No exceptions are caught")


zeroDiv(1, 0)
valEr("fs")
naEr()
fiEr()
keyInt()