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
        # loop the steps that make up one round of the game, until either player reaches 50 points
        while (self.player1.points < 50) and (self.player2.points < 50):
            winner = self.compare_stat("hp")
            self.update_decks(winner)
            self.update_points(winner)
        self.declare_winner()

    def declare_winner(self):
        if self.player1.points > self.player2.points:
            print("Player 1 has won the game!")
        else:
            print("Player 2 has won the game!")
        return self.player1 if self.player1.points > self.player2.points else self.player2

    def update_points(self, winning_player):
        if winning_player == self.player1:
            self.player1.points += 10
            print(
                f"Current scores:\nPlayer one: {self.player1.points} points\nPlayer two: {self.player2.points} points"
            )
        elif winning_player == self.player2:
            self.player2.points += 10
            print(
                f"Current scores:\nPlayer one: {self.player1.points} points.\nPlayer two: {self.player2.points} points"
            )

    def generate_hands(self):
        self.deck.add_cards()  # create deck of 20 random pokemon cards
        first_half = self.deck.cards[:10]  # split the deck
        second_half = self.deck.cards[10:]
        self.player1.cards += first_half  # assign each half to each player
        self.player2.cards += second_half

    def update_decks(self, winning_player):
        """
        removes losing card from losing player's deck and adds it to the winning player's deck. Moves winning card to the end of winning player's deck.
        """
        if winning_player == 0:
            return
        winning_card = winning_player.cards[0]
        if winning_player == self.player1:
            losing_card = self.player2.cards[0]
            self.player2.cards.pop(0)
        elif winning_player == self.player2:
            losing_card = self.player1.cards[0]
            winning_card = self.player2.cards[0]
            self.player1.cards.pop(0)  # remove losing card from player1 deck

        winning_player.cards.append(losing_card)
        winning_player.cards.pop(0)
        winning_player.cards.append(winning_card)

    def compare_stat(self, stat):
        """
        compares a given stat on each player's first card, to determine which has higher value. Returns the winning player for this round, so that this can be passed into the update_decks method.
        """

        player1_stat = self.player1.cards[0][stat]
        player2_stat = self.player2.cards[0][stat]
        self.print_stats(self.player1.cards[0], self.player2.cards[0])
        if player1_stat > player2_stat:
            print(f"player 1 wins {self.player2.cards[0]['name']}!")
            return self.player1  # return self.player2
        elif player1_stat < player2_stat:
            print(f"player 2 wins {self.player1.cards[0]['name']}!")
            return self.player2  # return self.player1
        else:
            print("it is a draw!")
            return 0

    def print_stats(self, player1_card, player2_card):
        print(f"{player1_card['name']} vs. {player2_card['name']}")
        print(
            f"{player1_card['name']} has {player1_card['hp']} hp | {player2_card['name']} has {player2_card['hp']} hp"
        )


# game = Game()
# game.play()
