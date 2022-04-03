import requests
import random


class Pokemon:
    """
    Pokemon class with name, hp, attack, defense, speed, special attack and special defense
    """

    def __init__(self, num):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}/")
        pokemon_data = response.json()
        self.data = {
            "name": pokemon_data["name"],
            "hp": pokemon_data["stats"][0]["base_stat"],
            "experience": pokemon_data["base_experience"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "speed": pokemon_data["stats"][5]["base_stat"],
        }

    def get_stat(self, stat):
        return self.data[stat]

    def compare_stat(self, other, stat):
        my_stat = self.get_stat(stat)
        opponent_stat = other.get_stat(stat)
        print(my_stat)
        # print(opponent_stat)
        # if self.data[stat] > other.data[stat]:
        #     return f'{self["name"]} wins!'
