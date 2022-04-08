import pytest
from game import Game
import random
from player import Player
from deck import Deck


@pytest.fixture
def game():
    """Returns a Game instance"""
    game = Game(Player("Kat"), Player("Jonty"), Deck())
    random.seed(
        1
    )  # stubbing the random here means the generate_hands will always return the same list of pokemon. This means player1 always wins first card
    game.generate_hands()
    return game


def test_generate_hands_gives_player1_10_cards(game):
    assert len(game.player1.cards) == 10


def test_generate_hands_gives_player2_10_cards(game):
    assert len(game.player2.cards) == 10


"""
thanks to the random.seed, we guarantee that player 1 card is always clefairy and player 2 card is always pikachu:
{'name': 'Clefairy', 'hp': 70, 'experience': 113, 'height': 6, 'weight': 75, 'speed': 35}
{'name': 'Pikachu', 'hp': 35, 'experience': 112, 'height': 4, 'weight': 60, 'speed': 90}
"""

# def test_choose_stat(game):
#     assert
def test_compare_pokemon_stat_hp_returns_player_with_highest_value(game):
    assert game.compare_stat("hp") == game.player1


def test_compare_pokemon_stat_experience_returns_player_with_highest_value(game):
    assert game.compare_stat("experience") == game.player1


def test_compare_pokemon_stat_height_returns_player_with_highest_value(game):
    assert game.compare_stat("height") == game.player1


def test_compare_pokemon_stat_weight_returns_player_with_highest_value(game):
    assert game.compare_stat("weight") == game.player1


def test_compare_pokemon_stat_speed_returns_player_with_highest_value(game):
    assert game.compare_stat("speed") == game.player2


def test_update_decks_gives_winner_the_card(game):
    losing_card = game.player2.cards[0]
    game.update_decks(game.player1)
    assert game.player1.cards[-2] == losing_card


def test_update_decks_shifts_winning_card_to_end(game):
    winning_card = game.player1.cards[0]
    game.update_decks(game.player1)
    assert game.player1.cards[-1] == winning_card


def test_update_decks_updates_both_player_decks(game):
    game.update_decks(game.player1)
    assert len(game.player1.cards) > len(game.player2.cards)


def test_update_decks_removes_losing_card_from_loser_deck(game):
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
    assert game.declare_winner() == game.player2
