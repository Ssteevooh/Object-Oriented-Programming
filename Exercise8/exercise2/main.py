# File: main.py
# Author: Steve Hommy
# Description: Main function


from house import House


def ask_user():
    try:
        user_input = int(input("If yes then type 1 if not then type 2: "))
        if user_input == 1 or user_input == 2:
            return user_input
        raise ValueError()
    except ValueError:
        print("Wrong input! Type 1 for Yes and 2 for No")


def wash_windows_and_bed_is_made(house):
    while True:
        print("Would you like to wash windows and make bed?")
        asking_user = ask_user()
        if asking_user == 1:
            house.set_wash_windows_and_bed_is_made()
            house.get_wash_windows_and_bed_is_made()
            break
        elif asking_user == 2:
            print("Alright not doing this task then")
            break


def vacuum_floors_and_clean_surfaces(house):
    while True:
        print("Would you like to vacuum floors and clean surfaces?")
        asking_user = ask_user()
        if asking_user == 1:
            house.set_vacuum_floors_and_clean_surfaces()
            house.get_vacuum_floors_and_clean_surfaces()
            break
        elif asking_user == 2:
            print("Alright not doing this task then")
            break


def shopping(house):
    while True:
        print("Would you like to go grocery shopping?")
        asking_user = ask_user()
        if asking_user == 1:
            house.set_shopping()
            house.get_shopping()
            break
        elif asking_user == 2:
            print("Alright not doing this task then")
            break


def enough_toilet_paper(house):
    while True:
        print("Would you like to hoard toilet paper?")
        asking_user = ask_user()
        if asking_user == 1:
            house.set_enough_toilet_paper()
            house.get_enough_toilet_paper()
            break
        elif asking_user == 2:
            print("Alright not doing this task then")
            break


def main():
    house = House()
    print(house)

    print("Would you like to clean the house?")
    while True:
        asking_user = ask_user()
        if asking_user == 2:
            print("Alright I guess you are lazy for not cleaning the house")
            break
        elif asking_user == 1:
            print("Alright let's get cleaning\n")
            wash_windows_and_bed_is_made(house)
            vacuum_floors_and_clean_surfaces(house)
            shopping(house)
            enough_toilet_paper(house)
            break
    print(house)


main()
