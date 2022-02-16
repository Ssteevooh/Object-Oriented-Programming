# File name: exercise8_main.py
# Author: Steve Hommy
# Description: Main function file


from exercise8_carClass import Car


def main():

    car = Car()
    car.set_make()
    car.set_model()
    car.set_milage()
    car.set_price()
    car.set_color()
    car.set_maximum_load_limit()
    car.set_size_of_trunk()

    print("\nThis is your car:")
    print(car)


main()
