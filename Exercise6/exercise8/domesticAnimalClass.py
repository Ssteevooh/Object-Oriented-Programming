# File name: domesticAnimalClass.py
# Author: Steve Hommy
# Description: Inherit Mammal Class and creating DomesticAnimal Class


from mammalClass import Mammal


class DomesticAnimal(Mammal):
    def __init__(self, animal_name, species, size, weight, id, noise, diet, owner):
        Mammal.__init__(self, animal_name, species, size, weight, id)
        self.noise = noise
        self.diet = diet
        self.owner = owner

    def __str__(self):
        return super().__str__() + f"""Noise of the animal: {self.noise}
        Diet: {self.diet}
        Owner: {self.owner}
        """

    def set_noise(self, noise):
        self.noise = noise

    def set_diet(self, diet):
        self.diet = diet

    def set_owner(self, owner):
        self.owner = owner

    def get_noise(self):
        return self.noise

    def get_diet(self):
        return self.diet

    def get_owner(self):
        return self.owner
