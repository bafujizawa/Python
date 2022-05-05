class Ninja:

    def __init__( self , name ):
        self.name = name
        self.stamina = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStamina: {self.stamina}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.stamina
        return self

    def powerattack(self, pirate):
        if self.health < 80:
            pass
        else:
            pirate.health -= (self.stamina * 1.5)
        return self

    def throwing_star(self,pirate):
        pirate.health -= 25
        return self

    def combo_attack(self, pirate):
        self.attack(pirate)
        self.powerattack(pirate)

    def seppuku(self):
        if self.health <= 2:
            self.health = 0
        else:
            print("I'm not finished yet!")