# File name: exercise2.py
# Author: Steve Hommy
# Description: Listing items

# Importing random module
import random

# Asking user for range of items that will be on list
number_of_elements = int(input("Enter number of elements in list: "))

# Creating lists
number_list = []
word_list = []

# Appending intgeres and strings to the list
for i in range(number_of_elements):
    number = int(input("Enter number: "))
    number_list.append(number)
for i in range(number_of_elements):
    word = input("Type anything: ")
    word_list.append(word)

# Prints out lists
print(number_list)
print(word_list)

# Filling the number list with randomly generated numbers
for i in range(len(number_list)):
    number_list[i] = random.randint(0,100)
print(number_list)
