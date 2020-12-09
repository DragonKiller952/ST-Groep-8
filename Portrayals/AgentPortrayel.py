from Agents.PartyAgent import PartyAgent 

def agent_portrayal(agent):
    assert agent is not None

    portrayal = {'Shape': 'circle',
                 'Layer': 0,
                 'Color': 'blue',
                 'r': 0.5}
    
    if type(agent) is PartyAgent:
        portrayal['Filled'] = 'true'
        portrayal['Color'] = 'green' if agent.winner else 'blue'

    return portrayal