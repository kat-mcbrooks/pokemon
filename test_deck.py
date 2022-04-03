import pytest
from deck import Deck


@pytest.fixture
def deck():
    return Deck()


def test_add_cards(deck):
    deck.add_cards()
    print(deck.cards[0])
    assert len(deck.cards) == 20


def test_add_cards_adds_pokemon(deck):
    deck.add_cards()
    assert isinstance(deck.cards[0]["name"], str)
