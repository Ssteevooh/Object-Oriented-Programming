# File name: exercise6.py
# Author: Steve Hommy
# Description: Function that counts the sum of the positive integers divisible by three


# Defining function
def sum_of_postive():
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
        # If number is 0 the program will print out sum of positive integers
        if number == 0:
            print("Sum of positive integers divisible by three is: " + str(total_number))
            break
        # If number is divisble by three and larger than 0 then sum
        elif number % 3 == 0 and number > 0:
            total_number += number


# Calling the function
sum_of_postive()
