import requests

import items
import factions
BASE_URL = "https://api.spacetraders.io/v2"
BASE_URL = "https://stoplight.io/mocks/spacetraders/spacetraders/96627693"  # comment out for prod
CONTRACTS_URL = "/my/contracts"


class Contract:
    def __init__(self, contract_data):
        self.id = contract_data['id']
        self.faction_symbol = contract_data['factionSymbol']  # this needs to be a faction object
        self.deadline = contract_data['terms']['deadline']
        self.on_accepted = contract_data['terms']['payment']['onAccepted']
        self.on_fulfilled = contract_data['terms']['payment']['onFulfilled']
        self.cargo_to_deliver = [TradeSymbol(trade_symbol) for trade_symbol in contract_data['terms']['deliver']]
        self.accepted = contract_data['accepted']
        self.fulfilled = contract_data['fulfilled']
        self.expiration = contract_data['expiration']

    def update(self):
        pass

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


def get_contracts(token = None):
    if token is not None:
        response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
    else:
        raise ValueError("You must provide a token")
    print(response.text)
    return [Contract(contract) for contract in response.json()['data']]

contracts = get_contracts('test_token')
print(contracts[0].cargo_to_deliver[0].trade_symbol)