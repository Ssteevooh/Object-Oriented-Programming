# File name: exercise4.py
# Author: Steve Hommy
# Description: Function which repeatedly reads integers until the user enters 0


# Defining function
def until_zero():
    number_list = []
    # While loop running until the break statement executes
    while True:
        number = int(input("Please give an integer: "))
        # If number is lower than 0 insert it into list
        if number < 0:
            number_list.append(number)
        # If number is 0 the program will print out length of list and stops the loop
        elif number == 0:
            print("Number of negative integers: " + str(len(number_list)))
            break


# Calling the function
until_zero()
