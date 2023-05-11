import pytest
import agent

"""tests for the app"""


def agent_test():
    """test the agent class"""
    test_agent = agent.Agent('tester_mctest', 'COSMIC')
    assert test_agent.credits == 0
    assert test_agent.name == "tester_mctest"
    failed_agent = agent.Agent()
    assert failed_agent is None




