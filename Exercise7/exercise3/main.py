# File: main.py
# Author: Steve Hommy
# Description: Main function

from student import Student
from pet import Pet


def main():
    student1 = Student("Steve", "Hommy", 1)
    student2 = Student("Jhon", "Snow", 2)
    pet1 = Pet("Dog", "Brak")
    pet2 = Pet("Cat", "Snuf")
    pet3 = Pet("Rabbit", "Snug")
    pet4 = Pet("Fish", "Blub")

    print("Here are our students:\n", student1, student2)

    print("\nLet's give our student a pet")
    student1.add_pets(pet1)
    student1.add_pets(pet2)
    student2.add_pets(pet3)
    student2.add_pets(pet4)

    student1.print_pets()
    student2.print_pets()
    question = input("\nWould you like to remove one of these pets? ")
    if question == "yes":
        question2 = input("\nWhich student pet would you like to remove? ")
        if question2 == "Steve":
            student1.remove_pets()
        elif question2 == "Jhon":
            student2.remove_pets()
        else:
            print("\nHere are the pets that remain")
            student1.print_pets()
            student2.print_pets()

    print("\nHere are the pets that remain")
    student1.print_pets()
    student2.print_pets()


main()
