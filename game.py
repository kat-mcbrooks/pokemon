from pokemon import Pokemon
from player import Player
from deck import Deck
import random


class Game:
    def __init__(self, player1=Player(), player2=Player(), deck=Deck()):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    def generate_hands(self):
        self.deck.add_cards()
        first_half = self.deck.cards[:10]
        second_half = self.deck.cards[10:]
        self.player1.cards += first_half
        self.player2.cards += second_half

    def get_pokemon(self):
        num = random.randint(1, 151)
        pokemon = Pokemon(num)
        print(pokemon.data["name"])
        return pokemon.data["name"]

    def select_cards(self, idx):
        return [self.player1.cards[idx], self.player2.cards[idx]]

    def compare_stat(self, stat):
        my_poke = self.get_pokemon()
        opponent_poke = self.get_pokemon()
        if my_poke.data[stat] > opponent_poke.data[stat]:
            print("You win!")


# game = Game()
# game.get_pokemon()

# return
#   def compare_stat(self, other, stat):
#       my_stat = self.get_stat(stat)
#       opponent_stat = other.get_stat(stat)
#       print(my_stat)
#       # print(opponent_stat)
#       # if self.data[stat] > other.data[stat]:
#       #     return f'{self["name"]} wins!'
