import requests

import items
from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Fleet:
    def __init__(self, token: str = None):
        self.token = token
        self.ships = []
        self.update_ships()

    def update_ships(self):
        if self.token is None:
            raise ValueError("You must provide a token")
        headers = {'Content-Type': 'application/json',
                   'Authorization': f"Bearer {self.token}"}
        response = requests.get(BASE_URL + settings['SHIPS_URL'], headers=headers)
        print(response.text)
        self.ships = [Ship(ship) for ship in response.json()['data']]
        # print(self.ships)

    def __str__(self):
        return f"{self.ships}"

    def __repr__(self):
        return f"{self.ships}"

class Ship:
    def __init__(self, ship: dict):
        self.symbol = ship['symbol']
        print(ship)
        self.crew = Crew(ship['crew'])
        self.frame = Frame(ship['frame'])
        self.reactor = Reactor(ship['reactor'])
        self.engine = Engine(ship['engine'])
        self.modules = [Module(module) for module in ship['modules']]
        self.mounts = [Mount(mount) for mount in ship['mounts']]
        self.cargo = Cargo(ship['cargo'])
        self.fuel = Fuel(ship['fuel'])

    def update(self):
        pass


class Frame:
    def __init__(self, frame: dict):
        self.symbol = frame['symbol']
        self.name = frame['name']
        self.description = frame['description']
        self.condition = frame['condition']
        self.module_slots = frame['moduleSlots']
        self.fuel_capacity = frame['fuelCapacity']
        self.required_crew = frame['requirements']['crew']
        self.reqiured_power = frame['requirements']['power']
        self.required_slots = frame['requirements']['slots']


class Reactor:
    def __init__(self, reactor: dict):
        self.symbol = reactor['symbol']
        self.name = reactor['name']
        self.description = reactor['description']
        self.condition = reactor['condition']
        self.power_output = reactor['powerOutput']
        self.required_crew = reactor['requirements']['crew']
        self.required_power = reactor['requirements']['power']
        self.required_slots = reactor['requirements']['slots']


class Engine:
    def __init__(self, engine: dict):
        self.symbol = engine['symbol']
        self.name = engine['name']
        self.description = engine['description']
        self.condition = engine['condition']
        self.speed = engine['speed']
        self.required_crew = engine['requirements']['crew']
        self.required_power = engine['requirements']['power']
        self.required_slots = engine['requirements']['slots']


class Module:
    def __init__(self, module: dict):
        self.symbol = module['symbol']
        self.capacity = module['capacity']
        self.range = module['range']
        self.name = module['name']
        self.description = module['description']
        self.required_crew = module['requirements']['crew']
        self.required_power = module['requirements']['power']
        self.required_slots = module['requirements']['slots']


class Mount:
    def __init__(self, mount: dict):
        self.symbol = mount['symbol']
        self.name = mount['name']
        self.description = mount['description']
        self.strength = mount['strength']
        self.deposits = [deposit for deposit in mount['deposits']]
        self.required_crew = mount['requirements']['crew']
        self.required_power = mount['requirements']['power']
        self.required_slots = mount['requirements']['slots']


class Cargo:
    def __init__(self, cargo: dict):
        self.capacity = cargo['capacity']
        self.units = cargo['units']
        self.inventory = [items.Item(i) for i in cargo['inventory']]


class Fuel:
    def __init__(self, fuel: dict):
        self.current = fuel['current']
        self.capacity = fuel['capacity']
        self.consumption = fuel['consumed']['amount']
        self.date_consumed = fuel['consumed']['timestamp']



class Crew:
    def __init__(self, crew: dict):
        self.current = crew['current']
        self.required = crew['required']
        self.capacity = crew['capacity']
        self.rotation = crew['rotation']
        self.morale = crew['morale']
        self.wages = crew['wages']

    def update(self):
        pass


if __name__ == '__main__':
    fleet = Fleet(token='test_token')
    print(fleet.ships[0].symbol)
    print(fleet.ships[0].crew.current)
    print(fleet.ships[0].frame.name)