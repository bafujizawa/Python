class Pirate:

    def __init__( self , name ):
        self.name = name
        self.stamina = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStamina: {self.stamina}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.stamina
        return self

    def powerattack(self, ninja):
        if self.health < 80:
            pass
        else:
            ninja.health -= (self.stamina * 1.5)

    def walk_the_plank(self):
        if self.health <= 2:
            self.health = 0
        else:
            print("I'm not finished yet!")

    def hook_attack(self, ninja):
        ninja.health -= 25
        return self

    def combo_attack(self, ninja):
        self.attack(ninja)
        self.powerattack(ninja)

    def defend(self):
        pass
