import pytest
from player import Player

# with fixtures, each test is provided with a newly-initialized Player instance, and not one that has been used in another test.
@pytest.fixture
def player():
    """returns a player instance"""
    return Player("Kat")


def test_has_name(player):
    assert player.name == "Kat"


def test_cards_can_be_added(player):
    player.cards += ["squirtle", "ditto"]
    assert player.cards == ["squirtle", "ditto"]


def test_points_can_be_added(player):
    player.points += 5
    assert player.points == 5
