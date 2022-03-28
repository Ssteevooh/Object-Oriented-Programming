# File name: cookie.py
# Author: Steve Hommy
# Description: Create a Cookie Class


class Cookie:
    def __init__(self, bake, frost):
        self.bake = bake
        self.frost = frost

    def __str__(self):
        return f"""
        Cookie is baked: {self.bake}
        Cookie is frosted: {self.frost}"""

    def set_bake(self):
        self.bake = False

    def get_bake(self):
        return self.bake

    def set_frost(self):
        self.frost = False

    def get_frost(self):
        return self.frost

