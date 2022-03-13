# File name: participantOfOopCourse.py
# Author: Steve Hommy
# Description: Create a ParticipantOfOopCourse Class


class ParticipantOfOopCourse:
    def __init__(self, name, gender, class_number):
        self.__name = name
        self.__gender = gender
        self.__class_number = int(class_number)

    def __str__(self):
        return f"""
        Name: {self.__name}
        Gender: {self.__gender}
        Class Number: {self.__class_number}
        """

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_class_number(self, class_number):
        self.__class_number = class_number

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_class_number(self):
        return self.__class_number
