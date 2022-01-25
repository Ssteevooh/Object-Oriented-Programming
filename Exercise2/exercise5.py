# File name: exercise5.py
# Author: Steve Hommy
# Description: 


name_list = []
points_list = []
students_in_course = int(input("How many students are in this course? "))

for i in range(students_in_course):
    student_name = input("Name of the student: ")
    name_list.append(student_name)
    student_points = int(input("Points of the student: "))
    points_list.append(student_points)

