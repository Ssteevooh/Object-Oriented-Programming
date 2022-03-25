# File name: house.py
# Author: Steve Hommy
# Description: Create a House Class


class House:
    def __init__(self):
        self.bedroom_window = "Dirty"
        self.kitchen_window = "Dirty"
        self.bedroom_floor = "Dirty"
        self.kitchen_floor = "Dirty"
        self.bedroom_bed = "Unmade"
        self.bedroom_surfaces = "Dusty"
        self.kitchen_surfaces = "Dusty"
        self.bathroom_surfaces = "Dusty"
        self.kitchen_fridge = "Empty"
        self.bathroom_toilet_paper = "Running out"

    def set_wash_windows_and_bed_is_made(self):
        self.bedroom_window = "Clean"
        self.kitchen_window = "Clean"
        self.bedroom_bed = "Made"

    def get_wash_windows_and_bed_is_made(self):
        print("Washing the windows and making the bed")
        return self.bedroom_window, self.kitchen_window, self.bedroom_bed

    def set_vacuum_floors_and_clean_surfaces(self):
        self.bedroom_floor = "Clean"
        self.kitchen_floor = "Clean"
        self.bedroom_surfaces = "Clean"
        self.kitchen_surfaces = "Clean"
        self.bathroom_surfaces = "Clean"

    def get_vacuum_floors_and_clean_surfaces(self):
        print("Vacuuming the floor and cleaning surfaces")
        return self.bedroom_floor, self.kitchen_floor, self.bedroom_surfaces, self.kitchen_surfaces, self.bathroom_surfaces

    def set_shopping(self):
        self.kitchen_fridge = "Filled"
        self.bathroom_toilet_paper = "Enough"

    def get_shopping(self):
        print("Going shopping to refill fridge and buy more toilet paper")
        return self.kitchen_fridge, self.bathroom_toilet_paper

    def set_enough_toilet_paper(self):
        self.bathroom_toilet_paper = "More than enough"

    def get_enough_toilet_paper(self):
        print("We should prepare for the lockdown and buy more toilet paper")
        return self.bathroom_toilet_paper

    def __str__(self):
        return f"""
    Houses status:

    Bedroom:
    Window: {self.bedroom_window}
    Floor: {self.bedroom_floor}
    Bed: {self.bedroom_bed}
    Surfaces: {self.bedroom_surfaces}

    Kitchen:
    Window: {self.kitchen_window}
    Floor: {self.kitchen_floor}
    Fridge: {self.kitchen_fridge}
    Surfaces: {self.kitchen_surfaces}

    Bathroom:
    Surfaces: {self.bathroom_surfaces}
    Toilet paper: {self.bathroom_toilet_paper}
    """
