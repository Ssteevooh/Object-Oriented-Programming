# File: main.py
# Author: Steve Hommy
# Description: Main function

from student import Student
from pet import Pet
from car import Car


def main():
    student1 = Student("Steve", "Hommy", 1)
    student2 = Student("Jhon", "Snow", 2)
    pet1 = Pet("Dog", "Brak", 150)
    pet2 = Pet("Cat", "Snuf", 100)
    pet3 = Pet("Rabbit", "Snug", 50)
    pet4 = Pet("Fish", "Blub", 10)
    car1 = Car("Toyota", "Avensis", 200)
    car2 = Car("VW", "Golf", 150)

    print("Here are our students:\n", student1, student2)

    print("\nLet's give our student a pet and a car")

    student1.add_pets(pet1)
    student1.add_pets(pet2)
    student1.add_cars(car1)

    student2.add_pets(pet3)
    student2.add_pets(pet4)
    student2.add_cars(car2)

    print(student1.get_first_name() + " owns these:")
    student1.print_pets()
    student1.print_cars()

    print(student2.get_first_name() + " owns these:")
    student2.print_pets()
    student2.print_cars()

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

    print("\nLet's check if pets will fit into the car")
    if car1.get_boot_size() >= pet1.get_pet_size() + pet2.get_pet_size():
        print(student1.get_first_name() + " pets will fit")
    else:
        print(student1.get_first_name() + " pets won't fit we need a trailer")

    if car2.get_boot_size() >= pet3.get_pet_size() + pet4.get_pet_size():
        print(student2.get_first_name() + " pets will fit")
    else:
        print(student2.get_first_name() + " pets won't fit we need a trailer")


main()
