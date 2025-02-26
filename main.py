# Logan Ul
from abc import ABC, abstractmethod
import random


class Pet(ABC):
    def __init__(self, hunger: int = 50, happiness: int = 50, energy: int = 50, name: str = ''):
        super().__init__()
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value < 100 and value > 0:
            self.__hunger = value
        elif value > 100:
            print("Value cannot be larger than 100.")
            self.__energy = 100
        else:
            print("Value cannot be less than 0.")
            self.__energy = 0

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value < 100 and value > 0:
            self.__happiness = value
        elif value > 100:
            print("Value cannot be larger than 100.")
            self.__energy = 100
        else:
            print("Value cannot be less than 0.")
            self.__energy = 0

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 100 and value > 0:
            self.__energy = value
        elif value > 100:
            print("Value cannot be larger than 100.")
            self.__energy = 100
        else:
            print("Value cannot be less than 0.")
            self.__energy = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__hunger = value

    def feed(self):
        self.hunger -= 20
        self.energy += 10
        self.random_event()

    def play(self):
        self.happiness += 15
        self.energy -= 10
        self.random_event()

    def sleep(self):
        self.energy += 20
        self.hunger += 10
        self.random_event()

    def show_status(self):
        return f"{self.name}'s Status:\nHunger: {self.hunger}/10\nHappiness: {self.happiness}/100\nEnergy: {self.energy}/100"

    def random_event(self):
        choice = random.randrange(10)
        if choice > -1 and choice < 4:
            events = random.randrange(4)
            if events == 0:
                print("Your pet found a snack!(-10 hunger)")
                self.hunger -= 10
            elif events == 1:
                print("Your pet plays by itself!(+10 happiness)")
                self.happiness += 10
            elif events == 2:
                print("Your pet had a nightmare!(-10 energy)")
                self.energy -= 10
            else:
                print("Your pet found a toy!(+15 happiness)")
                self.happiness += 15

    @abstractmethod
    def special_ability(self):
        pass


class Dog(Pet):
    def __init__(self, hunger=50, happiness=50, energy=50, name=''):
        super().__init__(hunger, happiness, energy, name)

    def play(self):
        self.happiness += 20
        self.energy -= 10
        self.random_event()

    def special_ability(self):
        if self.happiness >= 80:
            print("Your pet was excited and forgot to eat(-10 hunger)")
            self.hunger -= 10
        else:
            print("Stat is not low enough.")


class Cat(Pet):
    def __init__(self, hunger=50, happiness=50, energy=50, name=''):
        super().__init__(hunger, happiness, energy, name)

    def sleep(self):
        self.energy += 30
        self.hunger += 5
        self.random_event()

    def special_ability(self):
        if self.energy <= 20:
            print("Your pet was tired and took a nap on its self")
            self.energy += 15
        else:
            print("Stat is not low enough")
