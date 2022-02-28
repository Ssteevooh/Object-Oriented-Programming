# File name: main.py
# Author: Steve Hommy
# Description: Main function file


from studentClass import Student
from mammalClass import Mammal


def main():

    # Giving values to object
    student1 = Student("Steve", "Hommy", 1)
    student2 = Student("Tom", "Cruise", 2)
    print("Student1 status:", student1)
    print("Student2 status:", student2)

    mammal1 = Mammal("Bob", "Dog", 60, 30, 1)
    mammal2 = Mammal("Snuf", "Cat", 40, 20, 2)

    # Creating dictionary where student id is the key and mammal is value
    student_dict = {
        student1.get_id(): mammal1,
        student2.get_id(): mammal2
    }

    # looping through dictionary and printing out the key and the value
    for key in student_dict:
        print("Student with ID:", key, "\nHas this mammal:", student_dict[key])


main()
