import requests
import random


class Pokemon:
    """
    Pokemon class with name, hp, attack, defense, speed, special attack and special defense
    """

    def __init__(self, num):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}/")
        pokemon = response.json()
        self.name = pokemon["name"]
        self.hp = pokemon["stats"][0]["base_stat"]
        self.experience = pokemon["base_experience"]
        self.height = pokemon["height"]
        self.weight = pokemon["weight"]
        self.speed = pokemon["stats"][5]["base_stat"]  # access the speed base stat from within the stats key
