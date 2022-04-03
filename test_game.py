import pytest
from game import Game
from unittest.mock import patch
import random


@pytest.fixture
def game():
    """Returns a Game instance with squirtle and venusaur"""
    return Game()


def test_get_random_pokemon(game):
    random.seed(10)
    # print(random.randint(1, 151))
    # game.get_pokemon
    assert game.get_pokemon() == "dratini"

    # def test_compare_pokemon_stat(squirtle, venusaur):
    #   # assert squirtle.compare_stat(venusaur, "hp") == "venusaur wins!"
