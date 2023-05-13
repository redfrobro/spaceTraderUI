from agent import Agent
from contract import Contracts
from faction import Faction
import settings


def test_agent():
    agent = Agent(token=settings.settings['AGENT_TOKEN'])
    assert type(agent.name) == str
    assert type(agent.faction) == Faction or agent.faction is None
    assert type(agent.headquarters) == str
    assert type(agent.credits) == int
    assert type(agent.account_id) == str
    assert type(agent.token) == str
    assert type(agent.ships) == list
    assert type(agent.contracts) == Contracts
