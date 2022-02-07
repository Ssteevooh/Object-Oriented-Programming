# File name: exercise5.py
# Author: Steve Hommy
# Description: Calculate average grade


def students():
    student_list = []
    grade_list = []
    while True:
        # The lower() method returns a string where all characters are lower case
        # the strip() method remove spaces at the beginning and at the end of the string
        add_student = str(input("Want to input more students (Y/N): ")).lower().strip()
        try:
            if add_student[0] == "y":
                student_name = input("Give name: ")
                student_grade = int(input("Give grade: "))
                try:
                    if student_grade < 0 or student_grade > 5:
                        raise ValueError
                    student_list.append(student_name)
                    grade_list.append(student_grade)
                except ValueError:
                    print("Error: grade cannot be < 0 or > 5.")
            elif add_student[0] == "n":
                average = sum(grade_list) / len(student_list)
                # the zip() brings elements of the same index from multiple iterable 
                # objects together as elements of the same tuples
                for name, grade in zip(student_list, grade_list):
                    print(name + " grade is", grade)
                    # Formating average grade into 2 decimal
                print("Average grade of students is: " + " {:.2f}".format(average))
                break
            else:
                print("Invalid input")
        except Exception as error:
            print("Please input Y or N: ")
            print(error)

students()