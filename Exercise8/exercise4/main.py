# File: main.py
# Author: Steve Hommy
# Description: Main function


from cookie import Cookie
import random


while True:
    flavor_list = ["Vanilla", "Chocolate", "Toffe"]
    chosen_flavor = input("Choose flavor Vanilla, Chocolate, Toffe: ")
    if chosen_flavor in flavor_list:
        break


def main(chosen_flavor):
    choice = random.randint(0, 2)
    cookie_list = []

    for object in range(10):
        object = Cookie()
        cookie_list.append(object)

    # Bakes every cookie in the list one by one
    baked = 0
    for object in cookie_list:
        object.set_bake()
        baked += 1
        if baked == len(cookie_list):
            print("All cookies baked")
            print()

    # Frosts every cookie in the list one by one
    frosted = 0
    for object in cookie_list:
        object.set_frost(choice)
        frosted += 1
        if frosted == len(cookie_list):
            print("All cookies frosted")
            print()

    # Checks if the flavor is the same
    # If it's wrong do it all again
    test_cookie = cookie_list[0]
    if test_cookie.get_frost() != chosen_flavor:
        print("Flavor is wrong, everything has to be done again")
        main(chosen_flavor)

    # If flavor is right
    else:
        print("All cookies are correctly done")
        for object in cookie_list:
            print(object)


main(chosen_flavor)
