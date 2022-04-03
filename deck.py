from pokemon import Pokemon
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self):
        numbers = random.sample(range(1, 152), 20)
        for num in numbers:
            pokemon = Pokemon(num)
            self.cards.append(pokemon.data)
