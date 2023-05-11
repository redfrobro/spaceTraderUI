import requests

from settings import settings
import factions
import fleet
import contracts


if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Agent:
    def __init__(self, name: str = None, faction: str = None, token: str = None):
        headers = {'Content-Type': 'application/json'}
        self.faction = None

        if token is not None:
            headers['Authorization'] = f"Bearer {token}"
            response = requests.get(BASE_URL + settings['AGENT_URL'],  headers=headers)
            print(response.text)
            self.name = response.json()['data']['symbol']
            self.account_id = response.json()['data']['accountId']
            self.credits = response.json()['data']['credits']
            self.headquarters = response.json()['data']['headquarters']


        elif name is not None and faction is not None:
            # create a new agent
            data = {'symbol': name,
                    'faction': faction}
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
                self.faction = factions.Faction.from_symbol(faction, self.token)
        else:
            raise ValueError("You must provide either a name and faction or a token")

        self.ships = fleet.Fleet(self.token)
        self.contracts = contracts.Contracts(self.token)


# to be deleted later
if __name__ == '__main__':
    teser = Agent('tester_mctest', 'COSMIC')
