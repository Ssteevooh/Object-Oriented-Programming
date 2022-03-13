# File: main.py
# Author: Steve Hommy
# Description: Main function

from dogClass import Dog


def main():
    dog1 = Dog("Bob", "Dog", 60, 30, 1, "Bark", "Feed 2 times a day", "Steve")
    dog2 = Dog("Snuf", "Dog", 40, 20, 2, "Bark", "Feed 3 times a day", "Joe")

    print(dog1, dog2)


main()
