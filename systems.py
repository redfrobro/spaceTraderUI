import requests

import items
import factions
from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Galaxy:
    """A representation of the galaxy"""
    def __init__(self, token):
        self.token = token
        self.systems = self.get_systems(self.token)
        self.factions = self.get_factions(token)
        self.items = self.get_items(token)

    @staticmethod
    def get_systems(token=None):
        """Get a list of systems"""
        if token is not None:
            response = requests.get(BASE_URL + settings['SYSTEMS_URL'], headers={'Authorization': f"Bearer {token}"})
        else:
            raise ValueError("You must provide a token")
        print(response.text)
        return [System.system_from_data(system) for system in response.json()['data']]


class System:
    """A representation of a single system"""

    def __init__(self, symbol, sector_symbol, system_type, x, y, waypoint_list: list, factions_list: list):
        self.symbol = symbol
        self.sector_symbol = sector_symbol
        self.type = system_type
        self.x = x
        self.y = y
        self.waypoints = waypoint_list
        self.factions = factions_list

    @staticmethod
    def system_from_data(system_data):
        """Create a System object from a system data dict"""
        return System(symbol=system_data['symbol'], sector_symbol=system_data['sectorSymbol'], system_type=system_data['type'],
                      x=system_data['x'], y=system_data['y'], waypoint_list=system_data['waypoints'],
                      factions_list=system_data['factions'])



    def __str__(self):
        return f"{self.symbol}: {self.type}"

    def __repr__(self):
        return f"{self.symbol}: {self.type}"




class Waypoint:
    """A representation of a waypoint"""

    def __init__(self, symbol: str, system_type: str, system_symbol: str, x: int, y: int, orbital_list: list,
                 faction_symbol: str, traits: list,
                 waypoint_chart_symbol: str, submitted_by, submitted_on, ):
        self.symbol = symbol
        self.system_type = system_type
        self.system_symbol = system_symbol
        self.x = x
        self.y = y
        self.orbitals = [Orbital(orbital['symbol']) for orbital in orbital_list]
        self.faction_symbol = faction_symbol
        self.traits = [Traits.traits_from_data(trait) for trait in traits]
        self.waypoint_chart_symbol = waypoint_chart_symbol
        self.submitted_by = submitted_by
        self.submitted_on = submitted_on

    @staticmethod
    def waypoint_from_data(waypoint_data):
        """Create a Waypoint object from a waypoint data dict"""
        return Waypoint(symbol=waypoint_data['symbol'], system_type=waypoint_data['system_type'],
                        system_symbol=waypoint_data['systemSymbol'], x=waypoint_data['x'], y=waypoint_data['y'],
                        faction_symbol=waypoint_data['factionSymbol'], orbital_list=waypoint_data['orbitals'],
                        traits=waypoint_data['traits'], waypoint_chart_symbol=waypoint_data['chart']['waypointSymbol'],
                        submitted_by=waypoint_data['chart']['submittedBy'],
                        submitted_on=waypoint_data['chart']['submittedOn'])


class Orbital:
    def __init__(self, symbol: str, ):
        self.symbol = symbol


class Traits:
    def __init__(self, symbol: str, name: str, description: str, ):
        self.symbol = symbol
        self.name = name
        self.description = description

    @staticmethod
    def traits_from_data(traits_data):
        """Create a Traits object from a traits data dict"""
        return Traits(symbol=traits_data['symbol'], name=traits_data['name'], description=traits_data['description'])

galaxy = Galaxy('fake_token')
print(galaxy.systems)