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


def test_get_stat_hp(venusaur):
    assert venusaur.get_stat("hp") == 80


def test_get_stat_hp(squirtle):
    assert squirtle.get_stat("hp") == 44


def test_get_stat_name(squirtle):
    assert squirtle.get_stat("name") == "squirtle"


def test_compare_pokemon_stat(squirtle, venusaur):
    assert squirtle.compare(venusaur, "hp") == "venusaur wins!"
