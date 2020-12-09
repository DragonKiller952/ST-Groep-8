from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from Portrayals.AgentPortrayel import agent_portrayal
from Models.PluralityModel import PluralityModel

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
params = { "n_partys": UserSettableParameter("slider", "Party's Amount", 3, 1, 5),
           "n_voters": UserSettableParameter("slider", "Voters Amount", 10, 1, 50) }
server = ModularServer(PluralityModel, [grid], 'Plurality Model', model_params=params)
