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

    def compare_stat(self, stat):
        player_1_stat = self.player1.cards[0][stat]
        player_2_stat = self.player2.cards[0][stat]
        if player_1_stat > player_2_stat:
            print("player 1 wins!")
            return "player 1 wins"
        elif player_1_stat < player_2_stat:
            print("player 2 wins!")
            return "player 2 wins!"
        else:
            print("it is a draw!")
            return "it is a draw!"
