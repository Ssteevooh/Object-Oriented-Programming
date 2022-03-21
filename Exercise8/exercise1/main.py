# File: main.py
# Author: Steve Hommy
# Description: Main function


from house import House


def main():
    house = House()
    print(house)

    house.set_wash_windows_and_bed_is_made()
    house.get_wash_windows_and_bed_is_made()

    house.set_vacuum_floors_and_clean_surfaces()
    house.get_vacuum_floors_and_clean_surfaces()

    house.set_shopping()
    house.get_shopping()

    house.set_enough_toilet_paper()
    house.get_enough_toilet_paper()

    print(house)


main()
