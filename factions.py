import requests

import items
BASE_URL = "https://api.spacetraders.io/v2"
BASE_URL = "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"  # comment out for prod
FACTIONS_URL = "/factions"

class Faction:
    def __init__(self, faction_data):
        self.symbol = faction_data['symbol']
        self.name = faction_data['name']
        self.description = faction_data['description']
        self.headquarters = faction_data['headquarters']
        self.traits = [Trait(trait) for trait in faction_data['traits']]

    def update(self):
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"{self.name}: {self.description}"


class Trait:
    def __init__(self, trait_data):
        self.symbol = trait_data['symbol']
        self.name = trait_data['name']
        self.description = trait_data['description']

    def update(self):
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"{self.name}: {self.description}"


def get_factions(token=None):
    if token is not None:
        response = requests.get(BASE_URL + FACTIONS_URL, headers={'Authorization': f"Bearer {token}"})
    else:
        raise ValueError("You must provide a token")
    print(response.text)
    return [Faction(faction) for faction in response.json()['data']]


factions = get_factions('test_token')

print(factions[0].traits[0].name)