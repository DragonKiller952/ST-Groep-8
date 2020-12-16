from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent


def agent_portrayal(agent):
    assert agent is not None

    portrayal = {'Shape': 'circle',
                 'Layer': 0}

    if type(agent) is PartyAgent:
        portrayal['w'] = 0.8
        portrayal['h'] = 0.8
        portrayal['Filled'] = 'true'
        portrayal['Color'] = agent.color
        portrayal['Shape'] = 'rect'
    elif type(agent) is VoterAgent:
        portrayal['r'] = 0.5 if agent.chose_prefrence else 0.8
        portrayal['Color'] = agent.vote.color if agent.vote is not None else 'blue'

    return portrayal
