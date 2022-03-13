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
    cat = DomesticAnimal("Snuf", "Cat", 20, 10, 2, "Miaw", "Feed 1 times a day", "Sanna")
    tiger = WildAnimal("Nie", "Tiger", 40, 60, 3, "Rawr", "Feed 3 times a day", "Joe")
    lion = WildAnimal("Max", "Lion", 50, 80, 4, "Grawr", "Feed 4 times a day", "Joe")

    student.set_domestic_animal(dog)
    student.set_wild_animal(tiger)

    teacher.set_domestic_animal(cat)
    teacher.set_wild_animal(lion)

    print(f"""{student}
    domestic animal is:
    {student.get_domestic_animal()}
    and wild animal:
    {student.get_wild_animal()}""")

    print(f"""{teacher}
    domestic animal is:
    {teacher.get_domestic_animal()}
    and wild animal:
    {teacher.get_wild_animal()}""")


main()
