# File name: wildAnimalClass.py
# Author: Steve Hommy
# Description: Inherit Mammal Class and creating WildAnimal Class


from mammalClass import Mammal


class WildAnimal(Mammal):
    def __init__(self, animal_name, species, size, weight, id, noise, diet, zoo_keeper):
        Mammal.__init__(self, animal_name, species, size, weight, id)
        self.noise = noise
        self.diet = diet
        self.zoo_keeper = zoo_keeper

    def __str__(self):
        return super().__str__() + f"""Noise of the animal: {self.noise}
        Diet: {self.diet}
        Zoo keeper: {self.zoo_keeper}
        """

    def set_noise(self, noise):
        self.noise = noise

    def set_diet(self, diet):
        self.diet = diet

    def set_zoo_keeper(self, zoo_keeper):
        self.zoo_keeper = zoo_keeper

    def get_noise(self):
        return self.noise

    def get_diet(self):
        return self.diet

    def get_zoo_keeper(self):
        return self.zoo_keeper
