# File name: teacherClass.py
# Author: Steve Hommy
# Description: Inherit ParticipantOfOopCourse Class and create Teacher Class


from participantOfOopCourse import ParticipantOfOopCourse


class Teacher(ParticipantOfOopCourse):
    def __init__(self, name, gender, class_number, academic_rank, phone_number):
        ParticipantOfOopCourse.__init__(self, name, gender, class_number)
        self.__academic_rank = academic_rank
        self.__phone_number = int(phone_number)

    def __str__(self):
        return super().__str__() + f"""Academic rank: {self.__academic_rank}
        Phone number: {self.__phone_number}
        """

    def set_academic_rank(self, academic_rank):
        self.__academic_rank = academic_rank

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_academic_rank(self):
        return self.__academic_rank

    def get_phone_number(self):
        return self.__phone_number
