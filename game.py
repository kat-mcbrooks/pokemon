from pokemon import Pokemon
from player import Player
from deck import Deck
import random


class Game:
    def __init__(self, player1=Player(), player2=Player(), deck=Deck()):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    def play(self):
        self.generate_hands()
        while (self.player1.points < 50) and (self.player2.points < 50):
            winner = self.compare_stat("hp")
            self.update_decks(winner)
            self.update_points

    def update_points(self, winning_player):
        if winning_player == self.player1:
            self.player1.points += 10
        elif winning_player == self.player2:
            self.player2.points += 10

    def generate_hands(self):
        self.deck.add_cards()
        first_half = self.deck.cards[:10]
        second_half = self.deck.cards[10:]
        self.player1.cards += first_half
        self.player2.cards += second_half

    def update_decks(self, winning_player):
        if winning_player == self.player1:
            losing_card = self.player2.cards[0]
            self.player1.cards.append(losing_card)
            self.player2.cards.pop(0)
        elif winning_player == self.player2:
            losing_card = self.player1.cards[0]
            self.player2.cards.append(losing_card)
            self.player1.cards.pop(0)

    def compare_stat(self, stat):
        player1_stat = self.player1.cards[0][stat]
        player2_stat = self.player2.cards[0][stat]
        if player1_stat > player2_stat:
            print(f"player 1 wins {self.player2.cards[0]['name']}!")
            return self.player1  # return self.player2.cards[0]
        elif player1_stat < player2_stat:
            print(f"player 2 wins {self.player1.cards[0]['name']}!")
            return self.player2  # return self.player1.cards[0]
        else:
            print("it is a draw!")
            return "it is a draw!"
