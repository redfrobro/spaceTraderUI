import datetime
import requests

import items
import faction
from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']

CONTRACTS_URL = "/my/contracts"


class Contracts:
    """List of agent contracts"""

    def __init__(self, token):
        self.token = token
        self.contracts = self.get_contracts(self.token)

    @staticmethod
    def get_contracts(token: str):
        """Get a list of contracts"""
        response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
        return [Contract.from_contract_data(contract) for contract in response.json()['data']]


class Contract:
    """A representation of a single contract"""

    def __init__(self, contract_id: str, faction_symbol: str, deadline: int, on_accepted: dict, on_fulfilled: dict,
                 cargo_to_deliver: list, accepted: bool, fulfilled: bool, expiration: datetime.datetime):
        self.id = contract_id
        self.faction_symbol = faction_symbol
        self.deadline = deadline
        self.on_accepted = on_accepted
        self.on_fulfilled = on_fulfilled
        self.cargo_to_deliver = cargo_to_deliver
        self.accepted = accepted
        self.fulfilled = fulfilled
        self.expiration = expiration

    def update(self):
        pass

    @classmethod
    def from_contract_data(cls, contract_data):
        """Create a Contract object from a contract data dict"""
        return cls(contract_id=contract_data['id'], faction_symbol=contract_data['factionSymbol'],
                   deadline=contract_data['terms']['deadline'],
                   on_accepted=contract_data['terms']['payment']['onAccepted'],
                   on_fulfilled=contract_data['terms']['payment']['onFulfilled'],
                   cargo_to_deliver=contract_data['terms']['deliver'],
                   accepted=contract_data['accepted'], fulfilled=contract_data['fulfilled'],
                   expiration=contract_data['expiration'])

    def __str__(self):
        return f"{self.id}: {self.faction_symbol}"

    def __repr__(self):
        return f"{self.id}: {self.faction_symbol}"


class ContractCargo:
    """A representation of the cargo to deliver for a contract"""

    def __init__(self, contract_cargo_data):
        self.good = items.Good(contract_cargo_data['good'])
        self.quantity = contract_cargo_data['quantity']

    def update(self):
        pass


class TradeSymbol:
    """A representation of a trade symbol"""

    def __init__(self, trade_symbol_data):
        self.trade_symbol = trade_symbol_data['tradeSymbol']
        self.destination_symbol = trade_symbol_data['destinationSymbol']
        self.units_required = trade_symbol_data['unitsRequired']
        self.units_fulfilled = trade_symbol_data['unitsFulfilled']

    def update(self):
        pass


def get_contracts(token):
    """Get a list of available contracts"""
    response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
    return [Contract.from_contract_data(contract) for contract in response.json()['data']]


if __name__ == "__main__":
    contract_list = Contracts('test_token')
    print(contract_list.contracts)
    contracts = get_contracts('test_token')
    print(contracts)
