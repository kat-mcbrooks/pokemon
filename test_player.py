from re import M
import pytest
from player import Player, InsufficientAmount

# with fixtures, each test is provided with a newly-initialized Wallet instance, and not one that has been used in another test.
@pytest.fixture
def empty_player():
    """returns a player instance with a zero balance"""
    return Player()


@pytest.fixture
def player():
    """Returns a Player instance with a balance of 20"""
    return Player(20)


@pytest.mark.parametrize(
    "earned,spent,expected",
    [
        (30, 10, 20),
        (20, 2, 18),
    ],
)
def test_transations(earned, spent, expected):
    my_player = Player()
    my_player.add_cash(earned)
    my_player.spend_cash(spent)
    assert my_player.balance == expected


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
