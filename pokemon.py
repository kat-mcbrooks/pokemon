import requests


class Pokemon:
    """
    Pokemon class with name, hp, attack, defense, speed, special attack and special defense
    """

    def __init__(self, num):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}/")
        pokemon_data = response.json()

        self.data = {
            "name": (pokemon_data["name"]).capitalize(),
            "hp": pokemon_data["stats"][0]["base_stat"],
            "experience": pokemon_data["base_experience"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "speed": pokemon_data["stats"][5]["base_stat"],
        }

    def get_stat(self, stat):
        return self.data[stat]
