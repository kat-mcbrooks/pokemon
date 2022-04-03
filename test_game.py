import pytest
from game import Game
import random


@pytest.fixture
def game():
    """Returns a Game instance with squirtle and venusaur"""
    return Game()


def test_get_random_pokemon(game):
    random.seed(10)  # means that the next randint call executed will always return 147, which is dratini pokemon
    # print(random.randint(1, 151))
    # game.get_pokemon
    assert game.get_pokemon() == "dratini"


def test_generate_hands_gives_10_cards(game):
    game.generate_hands()
    assert len(game.player1.cards) == 10


def test_generate_hands_gives_10_cards(game):
    game.generate_hands()
    assert len(game.player2.cards) == 10


def test_select_card(game):
    game.generate_hands()
    # print(game.player1.cards)
    # print(game.player1.cards[0])
    current_cards = game.select_cards(0)
    print(current_cards)
    assert current_cards[0]["name"] == "blastoise"
    assert current_cards[1]["name"] == "vaporeon"


# def test_compare_pokemon_stat(game):
#    game.generate_hands()
#    game.compare('hp')

# def test_compare_pokemon_stat(game):
#     game.compare_stat("hp")
#     # assert squirtle.compare_stat(venusaur, "hp") == "venusaur wins!"
