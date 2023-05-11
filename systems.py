import requests

import items
import factions
BASE_URL = "https://api.spacetraders.io/v2"
BASE_URL = "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"  # comment out for prod
SYSTEMS_URL = "/systems"


class Galaxy:
    def __init__(self, token=None):
        self.systems = self.get_systems(token)
        self.factions = self.get_factions(token)
        self.items = self.get_items(token)

    def get_systems(self, token=None):
        if token is not None:
            response = requests.get(BASE_URL + SYSTEMS_URL, headers={'Authorization': f"Bearer {token}"})
        else:
            raise ValueError("You must provide a token")
        print(response.text)
        return [System(system) for system in response.json()['data']]

    def get_factions(self, token=None):
        return factions.get_factions(token)

    def get_items(self, token=None):
        return items.get_items(token)


class System:
    def __init__(self):
        self.waypoints = [Waypoint(waypoint) for waypoint in self.get_waypoints()]


    def get_waypoints(self):
        pass
