import datetime
import requests

import item
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

    def __str__(self):
        return f"{self.contracts}"


class Contract:
    """A representation of a single contract"""

    def __init__(self, contract_id: str, faction_symbol: str, deadline: int, on_accepted: dict, on_fulfilled: dict,
                 cargo_to_deliver: list, accepted: bool, fulfilled: bool, expiration: datetime.datetime):
        self.id = contract_id
        self.faction_symbol = faction_symbol
        self.deadline = deadline
        self.on_accepted = on_accepted
        self.on_fulfilled = on_fulfilled
        self.cargo_to_deliver = [ContractCargo.from_contract_data(cargo) for cargo in cargo_to_deliver]
        self.accepted = accepted
        self.fulfilled = fulfilled
        self.expiration = expiration

    def update(self, contract_data: str):
        """Update the contract"""
        self.__init__(contract_id=contract_data['id'], faction_symbol=contract_data['factionSymbol'],
                      deadline=contract_data['terms']['deadline'],
                      on_accepted=contract_data['terms']['payment']['onAccepted'],
                      on_fulfilled=contract_data['terms']['payment']['onFulfilled'],
                      cargo_to_deliver=contract_data['terms']['deliver'],
                      accepted=contract_data['accepted'], fulfilled=contract_data['fulfilled'],
                      expiration=contract_data['expiration']
                      )

    def accept(self, token):
        """Accept a contract"""
        response = requests.post(BASE_URL + CONTRACTS_URL + f"/{self.id}/accept",
                                 headers={'Authorization': f"Bearer {token}"})
        self.update(response.json()['data']['contract'])

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
        return f"{self.accepted}, {self.faction_symbol}: {self.cargo_to_deliver} for {self.on_fulfilled}ᖬ at {self.deadline}"

    def __repr__(self):
        return f"{self.accepted}, {self.faction_symbol}: {self.cargo_to_deliver} for {self.on_fulfilled}ᖬ at {self.deadline}"


class ContractCargo:
    """A representation of the cargo to deliver for a contract"""

    def __init__(self, trade_symbol, destination_symbol, units_required, units_fulfilled):
        self.trade_symbol = trade_symbol
        self.destination_symbol = destination_symbol
        self.units_required = units_required
        self.units_fulfilled = units_fulfilled

    @classmethod
    def from_contract_data(cls, cargo_data):
        """Create a ContractCargo object from a contract cargo data dict"""
        return cls(trade_symbol=cargo_data['tradeSymbol'], destination_symbol=cargo_data['destinationSymbol'],
                   units_required=cargo_data['unitsRequired'], units_fulfilled=cargo_data['unitsFulfilled'])

    def update(self):
        pass

    def __str__(self):
        return f"{self.units_required} {self.trade_symbol} to {self.destination_symbol}"

    def __repr__(self):
        return f"{self.units_required} {self.trade_symbol} to {self.destination_symbol}"


def get_contracts(token):
    """Get a list of available contracts"""
    response = requests.get(BASE_URL + CONTRACTS_URL, headers={'Authorization': f"Bearer {token}"})
    return [Contract.from_contract_data(contract) for contract in response.json()['data']]


if __name__ == "__main__":
    # contract_list = Contracts('test_token')
    # print(contract_list.contracts)
    contracts = get_contracts(settings['AGENT_TOKEN'])
    print(contracts)
