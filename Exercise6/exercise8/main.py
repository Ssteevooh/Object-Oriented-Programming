# File: main.py
# Author: Steve Hommy
# Description: Main function


from teacherClass import Teacher
from studentClass import Student
from domesticAnimalClass import DomesticAnimal
from wildAnimalClass import WildAnimal


def main():
    student = Student("Steve", "Male", 3, 324198, 3)
    teacher = Teacher("Sanna", "Female", 3, "Lecturer", +358954381273)
    dog = DomesticAnimal("Bob", "Dog", 60, 30, 1, "Bark", "Feed 2 times a day", "Steve")
    hamster = DomesticAnimal("Pier", "Hamster", 2, 5, 3, "Squeek", "Feed 1 times a day", "Steve")
    cat = DomesticAnimal("Snuf", "Cat", 20, 10, 2, "Miaw", "Feed 1 times a day", "Sanna")
    rabbit = DomesticAnimal("Nown", "Rabbit", 5, 10, 4, "Shhh", "Feed 1.5 times a day", "Sanna")
    tiger = WildAnimal("Nie", "Tiger", 40, 60, 3, "Rawr", "Feed 3 times a day", "Joe")
    lion = WildAnimal("Max", "Lion", 50, 80, 4, "Grawr", "Feed 4 times a day", "Joe")

    student_domestic_animals = [dog, hamster]
    student_wild_animals = [tiger, lion]
    teacher_domestic_animals = [cat, rabbit]
    teacher_wild_animals = [lion, tiger]

    student.set_domestic_animal(student_domestic_animals)
    student.set_wild_animal(student_wild_animals)

    teacher.set_domestic_animal(teacher_domestic_animals)
    teacher.set_wild_animal(teacher_wild_animals)

    print(f"""{student}
    domestic animals are:""")
    for student_domestic in student.get_domestic_animal():
        print(student_domestic)
    print("and wild animals are:")
    for student_wild in student.get_wild_animal():
        print(student_wild)

    print(f"""{teacher}
    domestic animals are:""")
    for teacher_domestic in teacher.get_domestic_animal():
        print(teacher_domestic)
    print("and wild animals are:")
    for teacher_wild in teacher.get_wild_animal():
        print(teacher_wild)


main()
