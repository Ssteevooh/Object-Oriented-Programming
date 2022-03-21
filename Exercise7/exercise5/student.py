# File name: student.py
# Author: Steve Hommy
# Description: Create a Student Class


class Student:
    def __init__(self, first_name, last_name, student_ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []
        self.__cars = []

    def set_first_name(self):
        self.__first_name = input("Student first name: ")

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self):
        self.__last_name = input("Student last name: ")

    def get_last_name(self):
        return self.__last_name

    def set_student_ID(self):
        self.__student_ID = input("Student ID: ")

    def get_student_ID(self):
        return self.__student_ID

    def add_pets(self, add_pet):
        try:
            if add_pet.get_owner() == None:
                self.__pets.append(add_pet)
                add_pet.set_owner(self.__first_name)
            else:
                print("Pet has an owner already")
        except ValueError:
            return print("Wrong value given")

    def remove_pets(self):
        for i in range(int(input("\nThere are " + str(len(self.__pets)) + " pets in a list.\nHow many would you like to remove? "))):
            for pets in self.__pets:
                print(pets)
            self.__pets.pop(int(input("\nFrist index is 0. Which pet would you like to remove from the list? ")))

    def print_pets(self):
        for pets in self.__pets:
            print(pets)

    def add_cars(self, add_car):
        if len(self.__cars) < 1:
            self.__cars.append(add_car)
            add_car.set_owner(self.__first_name)
        else:
            print("You already own 1 car")

    def remove_car(self):
        self.__cars.clear()

    def print_cars(self):
        for cars in self.__cars:
            print(cars)

    def __str__(self):
        return f"""
        First name: {self.__first_name}
        Last name: {self.__last_name}
        Student ID: {self.__student_ID}
        """
