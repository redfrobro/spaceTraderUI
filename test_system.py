from agent import Agent
from contract import Contracts
from faction import Faction
from system import System, Waypoint
import settings


def test_from_data():
    system = System.from_data(
        {'symbol': 'X1-DF55', 'sectorSymbol': 'X1', 'type': 'STAR', 'x': 0, 'y': 0, 'waypoints': [],
         'factions': []})
    assert type(system.symbol) == str
    assert type(system.sector_symbol) == str
    assert type(system.x) == int
    assert type(system.y) == int
    assert type(system.system_type) == str
    assert type(system.waypoints) == list
    assert type(system.factions) == list


def test_from_symbol():
    assert False


def test_get_system_from_token():
    assert False
