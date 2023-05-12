import requests

import items
import faction
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

    @staticmethod
    def get_systems(token):
        """Get a list of systems"""
        response = requests.get(
            BASE_URL + settings['SYSTEMS_URL'],
            headers={'Authorization': f"Bearer {token}"}
        )
        print(response.json())
        return [System.system_from_data(system) for system in response.json()['data']]


class System:
    """A representation of a single system"""

    def __init__(self, symbol, sector_symbol, system_type, x, y, waypoint_list: list, factions_list: list):
        self.symbol = symbol
        self.sector_symbol = sector_symbol
        self.system_type = system_type
        self.x = x
        self.y = y
        if len(waypoint_list) > 5:
            self.waypoints = [Waypoint.waypoint_from_data(waypoint) for waypoint in waypoint_list]
        else:
            self.waypoints = [Waypoint.waypoint_from_partial_data(waypoint) for waypoint in waypoint_list]
        self.factions = factions_list

    @staticmethod
    def system_from_data(system_data):
        """Create a System object from a system data dict"""
        return System(symbol=system_data['symbol'], sector_symbol=system_data['sectorSymbol'],
                      system_type=system_data['type'],
                      x=system_data['x'], y=system_data['y'], waypoint_list=system_data['waypoints'],
                      factions_list=system_data['factions'])

    @staticmethod
    def system_from_symbol(symbol, token):
        """Create a System object from a system symbol"""
        response = requests.get(
            BASE_URL + settings['SYSTEMS_URL'] + f"/{symbol}",
            headers={'Authorization': f"Bearer {token}"}
        )
        return System.system_from_data(response.json()['data'])

    @staticmethod
    def get_system_from_token(token):
        '''Get a system from a token'''

    def __str__(self):
        return f"{self.symbol}"

    def __repr__(self):
        return f"{self.symbol}"


class Waypoint:
    """A representation of a waypoint"""

    def __init__(self, symbol: str, system_type: str, system_symbol: str, x: int, y: int, orbital_list: list = None,
                 faction_symbol: str = None, traits: list = None,
                 waypoint_chart_symbol: str = None, submitted_by=None, submitted_on=None, ):
        self.symbol = symbol
        self.system_type = system_type
        self.system_symbol = system_symbol
        self.x = x
        self.y = y
        if orbital_list is None:
            self.orbitals = []
        else:
            self.orbitals = [Orbital(orbital['symbol']) for orbital in orbital_list]
        self.faction_symbol = faction_symbol
        if traits is None:
            self.traits = []
        else:
            self.traits = [Traits.traits_from_data(trait) for trait in traits]
        self.waypoint_chart_symbol = waypoint_chart_symbol
        self.submitted_by = submitted_by
        self.submitted_on = submitted_on

    @staticmethod
    def waypoint_from_data(waypoint_data):
        """Create a Waypoint object from a waypoint data dict"""
        print(waypoint_data)
        return Waypoint(symbol=waypoint_data['symbol'], system_type=waypoint_data['systemType'],
                        system_symbol=waypoint_data['systemSymbol'], x=waypoint_data['x'], y=waypoint_data['y'],
                        orbital_list=waypoint_data['orbitals'], faction_symbol=waypoint_data['factionSymbol'],
                        traits=waypoint_data['traits'], waypoint_chart_symbol=waypoint_data['waypointChartSymbol'],
                        submitted_by=waypoint_data['submittedBy'], submitted_on=waypoint_data['submittedOn'])

    @staticmethod
    def waypoint_from_partial_data(waypoint_data):
        """Create a Waypoint object from a partial waypoint data dict"""
        return Waypoint(symbol=waypoint_data['symbol'], system_type=waypoint_data['type'],
                        system_symbol=waypoint_data['symbol'], x=waypoint_data['x'], y=waypoint_data['y'],
                        )


def get_market(self, token):
    """Get the market for a waypoint"""
    response = requests.get(
        BASE_URL + settings['SYSTEMS_URL'] + f"/{self.system_symbol}/waypoints/{self.symbol}/market",
        headers={'Authorization': f"Bearer {token}"}
    )
    return response.json()['data']


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


if __name__ == '__main__':
    galaxy = Galaxy('fake_token')
    print(galaxy.systems)

    # print(galaxy.systems[0].waypoints[0].get_market('fake_token'))
