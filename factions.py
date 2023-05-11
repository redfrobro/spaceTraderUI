import requests

import items
from settings import settings
if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']



class Faction:
    """A class to represent a faction in the SpaceTraders API"""
    def __init__(self, symbol=None, name=None, description=None, headquarters=None, traits=None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.headquarters = headquarters
        self.traits = traits
        print(self.traits)

    def update(self):
        pass

    @classmethod
    def from_symbol(cls, symbol, token=None):
        """Create a Faction object from a faction symbol"""
        if token is not None:
            response = requests.get(BASE_URL + settings['FACTION_URL'] + f"/{symbol}", headers={'Authorization': f"Bearer {token}"})
        else:
            raise ValueError("You must provide a token")
        print(response.text)
        return cls.from_faction_data(response.json()['data'])

    @classmethod
    def from_faction_data(cls, faction_data):
        """Create a Faction object from a faction data dict"""
        return cls(faction_data['symbol'], faction_data['name'], faction_data['description'], faction_data['headquarters'], faction_data['traits'])

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
        response = requests.get(BASE_URL + settings['FACTIONS_URL'], headers={'Authorization': f"Bearer {token}"})
    else:
        raise ValueError("You must provide a token")
    print(response.text)
    return [Faction.from_faction_data(faction) for faction in response.json()['data']]


factions = get_factions('test_token')

print(factions[0].traits[0])