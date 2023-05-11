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
    def __init__(self, token=None):
        self.systems = self.get_systems(token)
        self.factions = self.get_factions(token)
        self.items = self.get_items(token)

    @staticmethod
    def get_systems(token=None):
        """Get a list of systems"""
        if token is not None:
            response = requests.get(BASE_URL + settings['SYSTEM_URL'], headers={'Authorization': f"Bearer {token}"})
        else:
            raise ValueError("You must provide a token")
        print(response.text)
        return [System(system) for system in response.json()['data']]

    def get_factions(self, token=None):
        return factions.get_factions(token)  # TODO - this is a placeholder

    def get_items(self, token=None): # TODO - this is a placeholder
        return items.get_items(token)


class System:
    def __init__(self):
        self.waypoints = [Waypoint(waypoint) for waypoint in self.get_waypoints()]


    def get_waypoints(self):
        pass


class Waypoint:
    def __init__(self):
        pass


galaxy = Galaxy()