import pytest
from pokemon import Pokemon


@pytest.fixture
def squirtle():
    """Returns a Pokemon instance using number 7"""
    return Pokemon(7)


@pytest.fixture
def venusaur():
    """Returns a Pokemon instance using number 3"""
    return Pokemon(3)


# @pytest.mark.parametrize(
#     "expected",
#     [
#         (30, 10, 20),
#         (20, 2, 18),
#     ],
# )


def test_has_hp(venusaur):
    assert venusaur.hp == 80


def test_has_name(squirtle):
    assert squirtle.name == "squirtle"


# def test_compare_pokemon_stat(squirtle, venusaur, 'hp'):
#   assert squirtle.compare(venusaur, hp)
