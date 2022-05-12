import random

class DeckOfCards():

    def __init__(self) -> None:
        pass


class Card():

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
    
    @staticmethod
    def suit():
        random = random.randint(4)
        