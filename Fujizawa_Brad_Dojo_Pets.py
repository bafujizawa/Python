class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet('Salem', 'cat', 'can talk, sassy')
        self.treats = treats
        self.pet_food = pet_food

    def walk():
        # Use pet.play()
        pass
    
    def feed():
        pass
    # use pet.feed()

    def bathe():
        pass
        # pet.bathe()

class Pet:

    def __init__(self, name, type, tricks, health=100, energy=100) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self, time=30):
        self.energy = self.energy * (time / 3)

    def eat(self):
        self.energy = self.energy
