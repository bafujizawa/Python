import random

class Character:
    all_character = []
    def __init__(self, name, health=100, strength=10, defense=10, skill=10) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        Character.all_character.append(self)

    def display_info(self):
        print(f'name: {self.name}')
        print(f'name: {self.health}')
        print(f'name: {self.strength}')
        print(f'name: {self.defense}')
        print('-' * 25)
        return self

    def change_health(self, amount):
        self.health += amount
    
    def attack(self, opponent):
        if Character.roll(20) > 3:
            print(f'{self.name} is attacking {opponent.name}')
            damage = (self.strength - (opponent.defense / 5))
            print(f'{self.name} does {damage} to {opponent.name}')
            opponent.change_health(damage)
        else:
            print(f'{self.name} misses')
        return self

    def defend(self, attacker):
        if roll(20) < self.skill:
            


    @classmethod
    def display_all_character(cls):
        for character in cls.all_character:
            print('*' * 80)
            character.display_info()
            print('-' * 25)

    @staticmethod
    def roll(dice):
        return random.randint(dice)

david = Character('david')
cross = Character('cross', health=95, strength=8, defense=14)

david.attack(cross)

