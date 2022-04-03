import pytest
from game import Game
import random
from player import Player
from deck import Deck


@pytest.fixture
def game():
    """Returns a Game instance"""
    game = Game(Player(), Player(), Deck())
    random.seed(1)  # subbing the random here means the generate_hands will always return the same list of pokemon
    game.generate_hands()
    return game


def test_generate_hands_gives_10_cards_player1(game):
    assert len(game.player1.cards) == 10


def test_generate_hands_gives_10_cards_player2(game):
    assert len(game.player2.cards) == 10


def test_compare_pokemon_stat(game):
    assert (
        game.compare_stat("hp") == game.player1
    )  # thanks to the random.seed, we guarantee that player 1 card is always clefairy (hp:70 ) and player 2 card is always pikachu (hp:35 )


def test_end_turn_gives_winner_the_card(game):
    losing_card = game.player2.cards[0]
    game.update_decks(game.player1)
    assert game.player1.cards[-1] == losing_card


def test_end_turn_removes_losing_card_from_loser_deck(game):
    losing_card = game.player2.cards[0]
    print(losing_card)
    print(game.player2.cards)
    game.update_decks(game.player1)
    assert game.player2.cards.count(losing_card) == 0


def test_update_points_player1(game):
    game.update_points(game.player1)
    assert game.player1.points == 10


def test_update_points_player2(game):
    game.update_points(game.player2)
    assert game.player2.points == 10


def test_declare_winner(game):
    for _ in range(5):
        game.update_points(game.player2)
    assert game.declare_winner() == "player 2 has won the game!"
