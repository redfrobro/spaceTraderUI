import requests

import items
import factions

BASE_URL = "https://api.spacetraders.io/v2"
BASE_URL = "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"  # comment out for prod
CONTRACTS_URL = "/my/contracts"


class Contract:
    def __init__(self, contract_id=None, faction_symbol=None, deadline=None, on_accepted=None, on_fulfilled=None,
                 cargo_to_deliver=None, accepted=None, fulfilled=None, expiration=None):
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


contracts = get_contracts('test_token')
print(contracts)
