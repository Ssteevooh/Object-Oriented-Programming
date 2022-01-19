# File name: exercise5.py
# Author: Steve Hommy
# Description: Function that counts the number of even integers


# Defining function
def even_integers():
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
        # If number is 0 the program will print out total of even integers and stops the loop
        if number == 0:
            print("Number of even integers: " + str(total_number))
            break
        # If number is negative then add one number
        elif number % 2 == 0:
            total_number = total_number + 1


# Calling the function
even_integers()
