import pytest
from deck import Deck


@pytest.fixture
def deck():
    return Deck()


def test_add_cards(deck):
    deck.add_cards()
    print(deck.cards[0])
    assert len(deck.cards) == 20


def test_add_cards_adds_pokemon_data(deck):
    deck.add_cards()
    assert isinstance(deck.cards[0]["name"], str)


def test_add_cards_adds_2nd_pokemon_data(deck):
    deck.add_cards()
    assert isinstance(deck.cards[1]["hp"], int)


def test_add_cards_adds_2nd_pokemon_data_speed(deck):
    deck.add_cards()
    assert isinstance(deck.cards[1]["speed"], int)


def test_add_cards_adds_2nd_pokemon_data_experience(deck):
    deck.add_cards()
    assert isinstance(deck.cards[1]["experience"], int)
