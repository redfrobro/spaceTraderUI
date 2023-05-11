import requests

from settings import settings

if settings['ENVIRONMENT'] == "DEV":
    BASE_URL = settings['DEV_BASE_URL']
else:
    BASE_URL = settings['BASE_URL']


class Agent:
    def __init__(self, name: str = None, faction: str = None, _token: str = None):
        headers = {'Content-Type': 'application/json'}

        if _token is not None:
            headers['Authorization'] = f"Bearer {_token}"
            print(headers)
            response = requests.get(BASE_URL + settings['AGENT_URL'],  headers=headers)
            print(response.text)
            self.name = response.json()['data']['symbol']
            self.account_id = response.json()['data']['accountId']
            self.credits = response.json()['data']['credits']
            self.headquarters = response.json()['data']['headquarters']

        elif name is not None and faction is not None:
            data = {'symbol': name,
                    'faction': faction}
            response = requests.post(BASE_URL + settings['REGISTER_URL'], json=data, headers=headers)
            print(response.text)
            self.name = response.json()['data']['agent']['symbol']
            self.account_id = response.json()['data']['agent']['accountId']
            self.credits = response.json()['data']['agent']['credits']
            self.headquarters = response.json()['data']['agent']['headquarters']
            self.token = response.json()['data']['token']
        else:
            raise ValueError("You must provide either a name and faction or a token")
        print(self.name)


teser = Agent('tester_mctest', 'COSMIC')
