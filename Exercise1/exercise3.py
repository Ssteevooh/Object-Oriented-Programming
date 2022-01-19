# File name: exercise3.py
# Author: Steve Hommy
# Description: Sorting list in ascending order


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

# Sorting lists in ascending order
number_list.sort()
word_list.sort()

# Prints out lists
print(number_list)
print(word_list)
