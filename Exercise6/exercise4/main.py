# File: main.py
# Author: Steve Hommy
# Description: Main function

from animals import *


def main():
    dog = Dog("Bob", "Dog", 60, 30, 1, "Bark", "Feed 2 times a day", "Steve", "black")
    cat = Cat("Snuf", "Cat", 20, 10, 2, "Miaw", "Feed 1 times a day", "Steve", "brown")
    tiger = Tiger("Nie", "Tiger", 40, 60, 3, "Rawr", "Feed 3 times a day", "Joe", 50)
    lion = Lion("Max", "Lion", 50, 80, 4, "Grawr", "Feed 4 times a day", "Joe", 40)

    print(dog, cat, lion, tiger)


main()
