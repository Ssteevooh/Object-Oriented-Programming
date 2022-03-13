# File name: studentClass.py
# Author: Steve Hommy
# Description: Inherit ParticipantOfOopCourse Class and create Student Class


from participantOfOopCourse import ParticipantOfOopCourse


class Student(ParticipantOfOopCourse):
    def __init__(self, name, gender, class_number, student_number, year_of_study):
        ParticipantOfOopCourse.__init__(self, name, gender, class_number)
        self.__student_number = int(student_number)
        self.__year_of_study = int(year_of_study)
        self.__domestic_animal = None
        self.__wild_animal = None

    def __str__(self):
        return super().__str__() + f"""Student number: {self.__student_number}
        Year of study: {self.__year_of_study}
        """

    def set_student_number(self, student_number):
        self.__student_number = student_number

    def set_year_of_study(self, year_of_study):
        self.__year_of_study = year_of_study

    def set_domestic_animal(self, domestic_animal):
        self.__domestic_animal = domestic_animal

    def set_wild_animal(self, wild_animal):
        self.__wild_animal = wild_animal

    def get_student_number(self):
        return self.__student_number

    def get_year_of_study(self):
        return self.__year_of_study

    def get_domestic_animal(self):
        return self.__domestic_animal

    def get_wild_animal(self):
        return self.__wild_animal
