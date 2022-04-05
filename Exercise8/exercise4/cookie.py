# File name: cookie.py
# Author: Steve Hommy
# Description: Create a Cookie Class


class Cookie:
    def __init__(self):
        self.bake = False
        self.frost = None
        self.flavor = ["Vanilla", "Chocolate", "Toffe"]

    def __str__(self):
        return f"""
        Cookie is baked: {self.bake}
        Cookie is frosted: {self.frost}
        """

    def set_bake(self):
        self.bake = True

    def get_bake(self):
        return self.bake

    def set_frost(self, choice):
        self.frost = self.flavor[choice]

    def get_frost(self):
        return self.frost
