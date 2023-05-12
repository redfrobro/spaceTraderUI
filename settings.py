# Generic/Built-in
import os
# Other Libs
import dotenv
# Owned

__author__ = "ngodfrey"
__copyright__ = "Copyright 2023"

"""
    This file contains all the settings for the project.
"""

dotenv.load_dotenv()

settings = {'BASE_URL': "https://api.spacetraders.io/v2",
            'DEV_BASE_URL': "https://stoplight.io/mocks/spacetraders/spacetraders/96627693",
            'SYSTEMS_URL': "/systems",
            'FACTION_URL': "/factions",
            'SHIPS_URL': "/my/ships",
            'AGENT_URL': "/my/agent",
            'REGISTER_URL': "/register",
            'CONTRACTS_URL': "/my/contracts",
            'ENVIRONMENT': "PROD",  # DEV or PROD
            'TOKEN': os.environ.get("AGENT_TOKEN"),
            }
