# File name: exercise10.py
# Author: Steve Hommy
# Description: Simple alarm clock


# Importing time module for localtime
import time

# Defining class
class Alarm():
    # __init__ allow the class to initialize the attributes of a class
    # Using the “self” keyword we can access the attributes and methods of the class in python
    def __init__(self, hours, minutes):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    # Checks if localtime equals the input time
    def set_timer(self):
        while self.keep_running:
            current_time = time.localtime()
            if (current_time.tm_hour == self.hours and current_time.tm_min == self.minutes):
                print("Ring! Ring! Ring!")
                return


# Defining main function
def main():
    set_hour = input("Enter the hour you want to wake up at: ")
    set_minute = input("Enter the minute you want to wake up at: ")
    alarm = Alarm(set_hour, set_minute)
    alarm.set_timer()
main()
