# File: main.py
# Author: Steve Hommy
# Description: Main function


from studentClass import Student
from teacherClass import Teacher


def main():
    student = Student("Steve", "Male", 3, 324198, 3)
    teacher = Teacher("Sanna", "Female", 3, "Lecturer", +358954381273)

    print(student, teacher)


main()
