import requests

from settings import settings
import faction
import fleet
import contract


if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Agent:
    def __init__(self, name: str = None, agent_faction: str = None, token: str = None):
        headers = {'Content-Type': 'application/json'}
        self.faction = None
        self.ships = None

        # this entire if statement needs to be reworked
        if token is not None:
            headers['Authorization'] = f"Bearer {token}"
            response = requests.get(BASE_URL + settings['AGENT_URL'],  headers=headers)
            print(response.text)
            self.name = response.json()['data']['symbol']
            self.account_id = response.json()['data']['accountId']
            self.credits = response.json()['data']['credits']
            self.headquarters = response.json()['data']['headquarters']
            self.token = token
            self.faction = faction.Faction.from_symbol(response.json()['data']['faction'], self.token)
            self.ships = fleet.Fleet.from_ship_data(response.json()['data']['ships'], self.token)
            self.contracts = contract.Contracts(self.token)

        elif name is not None and agent_faction is not None:
            # create a new agent
            data = {'symbol': name,
                    'faction': agent_faction}
            response = requests.post(BASE_URL + settings['REGISTER_URL'], json=data, headers=headers)

            # this is probably wrong, AI wrote this
            if response.status_code == 400:
                raise ValueError("The name you provided is already in use")
            elif response.status_code == 409:
                raise ValueError("The faction you provided is invalid")
            elif response.status_code == 201:
                print(response.text)
                self.name = response.json()['data']['agent']['symbol']
                self.account_id = response.json()['data']['agent']['accountId']
                self.credits = response.json()['data']['agent']['credits']
                self.headquarters = response.json()['data']['agent']['headquarters']
                self.token = response.json()['data']['token']
                self.faction = faction.Faction.from_symbol(agent_faction, self.token)
                self.contracts = contract.Contracts(self.token)
        else:
            raise ValueError("You must provide either a name and faction or a token")




# to be deleted later
if __name__ == '__main__':
    teser = Agent('tester_mctest', 'COSMIC')
