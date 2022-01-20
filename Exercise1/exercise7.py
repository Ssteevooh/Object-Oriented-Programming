# File name: exercise7.py
# Author: Steve Hommy
# Description: Arithmetic progression with a common difference of 3

def arithmetic_progression():

    procession_list = []

    max_value = int(input("Give maximum value: "))
    for i in range(1, max_value):
        if i % 3 == 0:
            procession_list.append(i)

    print("Procession is: " + str(procession_list))
    print("Number of terms is: " + str(len(procession_list)))
    print("Sum of term is: " + str(sum(procession_list)))
    print("Sum of squared terms is: " + str(sum(i * i for i in procession_list)))


arithmetic_progression()
