from pokemon import Pokemon
from player import Player
from deck import Deck


class Game:
    def __init__(self, player1=Player("Player 1"), player2=Player("Player 2"), deck=Deck()):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    def play(self):
        self.generate_hands()
        # loop the steps that make up one round of the game, until either player reaches 50 points
        round_count = 0  # track the round number so we can alternative which player chooses the stat
        print("FIRST ROUND...")
        while (self.player1.points < 50) and (self.player2.points < 50):
            print(f"{self.player1.cards[0]['name']} vs. {self.player2.cards[0]['name']}")
            chosen_stat = self.get_player_input_stat(round_count)
            winner = self.compare_stat(chosen_stat)  # returns winning_player or 0 if its a draw
            self.update_decks(winner)
            self.update_points(winner)
            round_count += 1
            print(f"NEXT ROUND, ROUND NO.{round_count}:")
        self.declare_winner()

    def get_player_input_stat(self, round):
        if round % 2 == 0:
            player = self.player1.name
            pokemon = self.player1.cards[0]["name"]
        else:
            player = self.player2.name
            pokemon = self.player2.cards[0]["name"]
        # print(f"{player} Please choose a pokemon stat from the following hp, experience, height, weight or speed")
        chosen_stat = input(
            f"{player}, choose a pokemon stat for this battle. What do you think {pokemon} is strongest in? You can choose hp, experience, height, weight or speed:\n"
        )
        return chosen_stat.lower()

    def declare_winner(self):
        if self.player1.points > self.player2.points:
            print(f"{self.player1.name} has won the game!")
        else:
            print(f"{self.player2.name} has won the game!")
        return self.player1 if self.player1.points > self.player2.points else self.player2

    def update_points(self, winning_player):
        if winning_player == 0:  # skip the update points if it is a draw
            return

        if winning_player == self.player1:
            self.player1.points += 10
            print(
                f"Current scores:\n{self.player1.name}: {self.player1.points} points\n{self.player2.name}: {self.player2.points} points"
            )
        elif winning_player == self.player2:
            self.player2.points += 10
            print(
                f"Current scores:\n{self.player1.name}: {self.player1.points} points.\n{self.player2.name}: {self.player2.points} points"
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
        if winning_player == 0:  # skip the update decks if it is a draw
            self.player1.cards.append(self.player1.cards[0])
            self.player1.cards.pop(0)
            self.player2.cards.append(self.player2.cards[0])
            self.player2.cards.pop(0)
            return
        winning_card = winning_player.cards[0]
        if winning_player == self.player1:
            losing_card = self.player2.cards[0]
            self.player2.cards.pop(0)  # remove losing card from player2 hand
        elif winning_player == self.player2:
            losing_card = self.player1.cards[0]
            self.player1.cards.pop(0)  # remove losing card from player1 deck

        winning_player.cards.append(losing_card)
        winning_player.cards.append(winning_card)
        winning_player.cards.pop(0)

    def compare_stat(self, stat):
        """
        compares a given stat on each player's first card, to determine which has higher value. Returns the winning player for this round, so that this can be passed into the update_decks method.
        """

        player1_stat = self.player1.cards[0][stat]
        player2_stat = self.player2.cards[0][stat]

        self.print_stats(self.player1.cards[0], self.player2.cards[0], stat)
        if player1_stat > player2_stat:
            print(f"{self.player1.name} wins {self.player2.cards[0]['name']}!")
            return self.player1
        elif player1_stat < player2_stat:
            print(f"{self.player2.name} wins {self.player1.cards[0]['name']}!")
            return self.player2
        else:
            print("it is a draw!")
            return 0

    def print_stats(self, player1_card, player2_card, stat):
        print(
            f"{player1_card['name']} has {player1_card[stat]} {stat} | {player2_card['name']} has {player2_card[stat]} {stat}"
        )


# when Python interpreter reads a file, it defines the __name__ variable. If game.py is ran as the main program i.e. $ python game.py, it will assign '__main__' but if game.py is imported e.g. in test files, it will assign __name__ = 'game' and therefore won't run the game script, which is what we want.
if __name__ == "__main__":
    game = Game(player1=Player("Kat"), player2=Player("Jonty"))
    game.play()
