import requests

import item
from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Fleet:
    def __init__(self, token: str, ships: list = None):
        self.token = token
        self.ships = []
        if ships is not None:
            self.ships = [Ship.from_ship_data(ship) for ship in ships]
        else:
            self.update_ships()

    def update_ships(self):
        """Get a list of ships"""
        headers = {'Content-Type': 'application/json',
                   'Authorization': f"Bearer {self.token}"}
        response = requests.get(BASE_URL + settings['SHIPS_URL'], headers=headers)
        print(response.json())
        self.ships = [Ship.from_ship_data(ship) for ship in response.json()['data']]

    @classmethod
    def from_ship_data(cls, ship_data):
        """Create a Fleet object from a ship data dict"""
        return cls(ships=ship_data)

    def __str__(self):
        return f"{self.ships}"

    def __repr__(self):
        return f"{self.ships}"


class Ship:
    def __init__(self, symbol: str, crew: dict, frame: dict, reactor: dict, engine: dict, modules: list, mounts: list,
                 cargo: dict, fuel: dict):
        self.symbol = symbol
        self.crew = Crew(crew)
        self.frame = Frame.from_frame_data(frame)
        self.reactor = Reactor.from_reactor_data(reactor)
        self.engine = Engine.from_engine_data(engine)
        self.modules = [Module.from_module_data(module) for module in modules]
        self.mounts = [Mount.from_mount_data(mount) for mount in mounts]
        self.cargo = Cargo(cargo)
        self.fuel = Fuel(fuel)
        self.update()

    def refine(self, token):
        """Attempt to refine the raw materials on your ship"""
        response = requests.post(
            BASE_URL + settings['SHIPS_URL'] + f"/{self.symbol}/refine",
            headers={'Authorization': f"Bearer {token}"}
        )
        # this needs more work
        return response.json()

    def chart_system(self, token):
        """Chart a system"""
        response = requests.post(
            BASE_URL + settings['SHIPS_URL'] + f"/{self.symbol}/chart",
            headers={'Authorization': f"Bearer {token}"}
        )
        # this needs more work
        return response.json()

    def __str__(self):
        return f"{self.symbol}: {self.frame.name}"

    def __repr__(self):
        return f"{self.symbol}: {self.frame.name}"

    @classmethod
    def from_ship_data(cls, ship_data):
        """Create a Ship object from a ship data dict"""
        return cls(ship_data['symbol'], ship_data['crew'], ship_data['frame'], ship_data['reactor'],
                   ship_data['engine'], ship_data['modules'], ship_data['mounts'], ship_data['cargo'],
                   ship_data['fuel'])

    def update(self):
        pass


class Frame:
    def __init__(self, symbol: str, name: str, description: str, condition: int, module_slots: int, fuel_capacity: int,
                 required_crew: int, required_power: int, required_slots: int = None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.condition = condition
        self.module_slots = module_slots
        self.fuel_capacity = fuel_capacity
        self.required_crew = required_crew
        self.required_power = required_power
        self.required_slots = required_slots

    def __str__(self):
        return f"{self.symbol}: {self.name}"

    def __repr__(self):
        return f"{self.symbol}: {self.name}"

    @classmethod
    def from_frame_data(cls, frame_data):
        """Create a Frame object from a frame data dict"""
        if 'slots' not in frame_data['requirements']:
            slots = None
        else:
            slots = frame_data['requirements']['slots']
        return cls(frame_data['symbol'], frame_data['name'], frame_data['description'], frame_data['condition'],
                   frame_data['moduleSlots'], frame_data['fuelCapacity'], frame_data['requirements']['crew'],
                   frame_data['requirements']['power'], slots)


class Reactor:
    def __init__(self, symbol: str, name: str, description: str, condition: int, power_output: int, required_crew: int,
                 required_power: int = None, required_slots: int = None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.condition = condition
        self.power_output = power_output
        self.required_crew = required_crew
        self.required_power = required_power
        self.required_slots = required_slots

    def __str__(self):
        return f"{self.symbol}: {self.name}"

    def __repr__(self):
        return f"{self.symbol}: {self.name}"

    @classmethod
    def from_reactor_data(cls, reactor_data):
        """Create a Reactor object from a reactor data dict"""
        if 'slots' not in reactor_data['requirements']:
            slots = None
        else:
            slots = reactor_data['requirements']['slots']

        if 'power' not in reactor_data['requirements']:
            power = None
        else:
            power = reactor_data['requirements']['power']

        return cls(reactor_data['symbol'], reactor_data['name'], reactor_data['description'], reactor_data['condition'],
                   reactor_data['powerOutput'], reactor_data['requirements']['crew'],
                   power, slots)


class Engine:
    def __init__(self, symbol: str, name: str, description: str, condition: int, speed: int, required_crew: int,
                 required_power: int, required_slots: int = None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.condition = condition
        self.speed = speed
        self.required_crew = required_crew
        self.required_power = required_power
        self.required_slots = required_slots

    def __str__(self):
        return f"{self.symbol}: {self.name}"

    def __repr__(self):
        return f"{self.symbol}: {self.name}"

    @classmethod
    def from_engine_data(cls, engine_data):
        """Create an Engine object from an engine data dict"""
        if 'slots' not in engine_data['requirements']:
            slots = None
        else:
            slots = engine_data['requirements']['slots']
        return cls(engine_data['symbol'], engine_data['name'], engine_data['description'], engine_data['condition'],
                   engine_data['speed'], engine_data['requirements']['crew'], engine_data['requirements']['power'],
                   slots)


class Module:
    def __init__(self, symbol: str, capacity: int, range: int, name: str, description: str, required_crew: int,
                 required_power: int, required_slots: int = None):
        self.symbol = symbol
        self.capacity = capacity
        self.range = range
        self.name = name
        self.description = description
        self.required_crew = required_crew
        self.required_power = required_power
        self.required_slots = required_slots

    def __str__(self):
        return f"{self.symbol}: {self.name}"

    def __repr__(self):
        return f"{self.symbol}: {self.name}"

    @classmethod
    def from_module_data(cls, module_data):
        """Create a Module object from a module data dict"""
        if 'slots' not in module_data['requirements']:
            slots = None
        else:
            slots = module_data['requirements']['slots']

        if 'power' not in module_data['requirements']:
            power = None
        else:
            power = module_data['requirements']['power']

        if 'range' not in module_data:
            range = 0
        else:
            range = module_data['range']

        if 'capacity' not in module_data:
            capacity = 0
        else:
            capacity = module_data['capacity']
        return cls(module_data['symbol'], capacity, range, module_data['name'],
                   module_data['description'], module_data['requirements']['crew'], power,
                   slots)


class Mount:
    def __init__(self, symbol: str, name: str, description: str, strength: int, deposits: list, required_crew: int,):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.strength = strength
        self.deposits = deposits
        self.required_crew = required_crew

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def from_mount_data(cls, mount_data):
        """Create a Mount object from a mount data dict"""
        if 'deposits' not in mount_data:
            deposits = None
        else:
            deposits = mount_data['deposits']
        return cls(mount_data['symbol'], mount_data['name'], mount_data['description'], mount_data['strength'],
                   deposits, mount_data['requirements']['crew'])


class Cargo:
    def __init__(self, cargo: dict):
        self.capacity = cargo['capacity']
        self.units = cargo['units']
        self.inventory = [item.Item.item_from_data(i) for i in cargo['inventory']]

    def __str__(self):
        return f"Cargo:{self.units}/{self.capacity} of {self.inventory}"

    def __repr__(self):
        return f"Cargo:{self.units}/{self.capacity}"


class Fuel:
    def __init__(self, fuel: dict):
        self.current = fuel['current']
        self.capacity = fuel['capacity']
        self.consumption = fuel['consumed']['amount']
        self.date_consumed = fuel['consumed']['timestamp']

    def __str__(self):
        return f"Fuel:{self.current}/{self.capacity}"

    def __repr__(self):
        return f"Fuel:{self.current}/{self.capacity}"


class Crew:
    def __init__(self, crew: dict):
        self.current = crew['current']
        self.required = crew['required']
        self.capacity = crew['capacity']
        self.rotation = crew['rotation']
        self.morale = crew['morale']
        self.wages = crew['wages']

    def __str__(self):
        return f"Crew:{self.current}/{self.capacity}"

    def __repr__(self):
        return f"Crew:{self.current}/{self.capacity}"


if __name__ == '__main__':
    fleet = Fleet(token=settings['AGENT_TOKEN'])
    print(fleet.ships[0].symbol)
    print(fleet.ships[0].crew.current)
    print(fleet.ships[0].frame.name)
    print(fleet.ships[0].frame)
    print(fleet.ships[0].reactor)
    print(fleet.ships[0].engine)
    print(fleet.ships[0].modules)
    print(fleet.ships[0].mounts)
    print(fleet.ships[0].cargo)
    print(fleet.ships[0].fuel)
    print(fleet.ships[0].crew)
    print(fleet.ships[0].chart_system(settings['AGENT_TOKEN']))