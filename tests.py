import pytest
import agent

"""tests for the app"""


def agent_test():
    """test the agent class"""
    test_agent = agent.Agent()
    assert test_agent.credits == 0
    assert test_agent.name == "tester_mctest"




