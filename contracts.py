import requests

import items
import factions
from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']

CONTRACTS_URL = "/my/contracts"


class Contracts:
    def __init__(self, token):
        self.token = token
        self.contracts = self.get_contracts(self.token)

    @staticmethod
    def get_contracts(token=None):
        """Get a list of contracts"""
        if token is not None:
            response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
        else:
            raise ValueError("You must provide a token")
        return [Contract.from_contract_data(contract) for contract in response.json()['data']]


class Contract:
    def __init__(self, contract_id, faction_symbol, deadline, on_accepted, on_fulfilled,
                 cargo_to_deliver, accepted, fulfilled, expiration):
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
        return cls(contract_id=['id'], faction_symbol=['faction'], deadline=['deadline'], on_accepted=['onAccepted'],
                   on_fulfilled=contract_data['onFulfilled'], cargo_to_deliver=contract_data['terms']['deliver'],
                   accepted=contract_data['accepted'], fulfilled=contract_data['fulfilled'],
                   expiration=contract_data['expiration'])

    def __str__(self):
        return f"{self.id}: {self.faction_symbol}"

    def __repr__(self):
        return f"{self.id}: {self.faction_symbol}"


class TradeSymbol:
    def __init__(self, trade_symbol_data):
        self.trade_symbol = trade_symbol_data['tradeSymbol']
        self.destination_symbol = trade_symbol_data['destinationSymbol']
        self.units_required = trade_symbol_data['unitsRequired']
        self.units_fulfilled = trade_symbol_data['unitsFulfilled']

    def update(self):
        pass


def get_contracts(token=None):
    if token is not None:
        response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
    else:
        raise ValueError("You must provide a token")
    print(response.text)
    return [Contract(contract) for contract in response.json()['data']]


if __name__ == "__main__":
    contract_list = Contracts('test_token')
    print(contract_list.contracts)
    contracts = get_contracts('test_token')
    print(contracts)
