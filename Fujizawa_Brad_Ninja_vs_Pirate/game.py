from mimetypes import init
import random

from classes.ninja import Ninja
from classes.pirate import Pirate


class Game:

    def __init__(self) -> None:
        self.ninja = Ninja('Michaelanglo')
        self.pirate = Pirate('Jack Sparrow')

    def show_stats(self):
        self.pirate.show_stats()
        self.ninja.show_stats()
    
    def pirate_attack_ninja(self):
        self.pirate

    def ninja_attack_pirate(self):
        self.ninja.attack(self.pirate)

    @classmethod
    def display_all_character(cls):
        for character in cls.all_character:
            print('*' * 80)
            character.display_info()
            print('-' * 25)

    @staticmethod
    def show_stats(player):
        print(player.show_stats)


class Fighter:
    
    def  __init__(self, name) -> None:
        self.name = name
        

    def show_stats(self):
        print(f"Name: {self.name}\nStamina: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, opponent):
        opponent.health -= self.strength
        return self

    def power_attack(self, opponent):
        opponent.health -= self.strength * 1.5

    def quick_attack(self, opponent):
        opponent.health -= self.strength + self.speed

    def combo_attack(self, opponent):
        self.quick_attack(opponent)
        self.power_attack(opponent)

class Pirate(Fighter):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100

    # def show_stats(self):
    #     return super().show_stats()


class Ninja(Fighter):
    def  __init__(self, name) -> None:
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100

    

blackbeard = Pirate('Blackbeard')
donatello = Ninja('Donatello')

blackbeard.attack(donatello)

donatello.show_stats()