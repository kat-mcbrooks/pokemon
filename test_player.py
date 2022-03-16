import pytest
from player import Player, InsufficientAmount


@pytest.fixture
def empty_player():
    """returns a player instance with a zero balance"""
    return Player()


@pytest.fixture
def player():
    """Returns a Player instance with a balance of 20"""
    return Player(20)


def test_default_initial_amount(empty_player):
    assert empty_player.balance == 0


def test_add_cash(player):
    player.add_cash(10)
    assert player.balance == 30


def test_spend_cash(player):
    player.spend_cash(5)
    assert player.balance == 15


def test_spend_cash_raises_error_if_insufficient_funds(player):
    with pytest.raises(InsufficientAmount):
        player.spend_cash(25)


# def capital_case(x):
#     if not isinstance(x, str):
#         raise TypeError("Please provide a string arg")
#     return x.capitalize()


# def test_capital_case():
#     assert capital_case("semaphore") == "Semaphore"


# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)
