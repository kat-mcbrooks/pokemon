import pytest
from player import Player, InsufficientAmount


def test_default_initial_amount():
    player = Player()
    assert player.balance == 0


def test_add_cash():
    player = Player()
    player.add_cash(10)
    assert player.balance == 10


def test_spend_cash():
    player = Player(10)
    player.spend_cash(5)
    assert player.balance == 5


def test_spend_cash_raises_error_if_insufficient_funds():
    player = Player()
    with pytest.raises(InsufficientAmount):
        player.spend_cash(5)


# def capital_case(x):
#     if not isinstance(x, str):
#         raise TypeError("Please provide a string arg")
#     return x.capitalize()


# def test_capital_case():
#     assert capital_case("semaphore") == "Semaphore"


# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)
