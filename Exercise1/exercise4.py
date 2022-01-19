# File name: exercise4.py
# Author: Steve Hommy
# Description: Function which outputs total of negative integers


# Defining function
def negative_integers():
    total_number = 0
    # While loop running until the break statement executes
    while True:
        number = input("Please give an integer: ")
        # Checking if the input is a valid integer
        try:
            number = int(number)
        except ValueError:
            print("Invalid input")
            continue
        # If number is negative then add one number
        if number < 0:
            total_number = total_number + 1
        # If number is 0 the program will print out total of negative integers and stops the loop
        elif number == 0:
            print("Number of negative integers: " + str(total_number))
            break


# Calling the function
negative_integers()
