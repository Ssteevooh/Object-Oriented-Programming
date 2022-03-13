# File name: animals.py
# Author: Steve Hommy
# Description: creating different animal Classes


from animalType import WildAnimal, DomesticAnimal


class Dog(DomesticAnimal):
    def __init__(self, name, species, size, weight, id, noise, diet, owner, color):
        DomesticAnimal.__init__(self, name, species, size, weight, id, noise, diet, owner)
        self.color = color

    def __str__(self):
        return super().__str__() + f"""Color: {self.color}
        """

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Cat(DomesticAnimal):
    def __init__(self, name, species, size, weight, id, noise, diet, owner, color):
        DomesticAnimal.__init__(self, name, species, size, weight, id, noise, diet, owner)
        self.color = color

    def __str__(self):
        return super().__str__() + f"""Color: {self.color}
        """

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Tiger(WildAnimal):
    def __init__(self, name, species, size, weight, id, noise, diet, zoo_keeper, speed):
        WildAnimal.__init__(self, name, species, size, weight, id, noise, diet, zoo_keeper)
        self.speed = int(speed)

    def __str__(self):
        return super().__str__() + f"""Speed: {self.speed}
        """

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed


class Lion(WildAnimal):
    def __init__(self, name, species, size, weight, id, noise, diet, zoo_keeper, speed):
        WildAnimal.__init__(self, name, species, size, weight, id, noise, diet, zoo_keeper)
        self.speed = int(speed)

    def __str__(self):
        return super().__str__() + f"""Speed: {self.speed}
        """

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed