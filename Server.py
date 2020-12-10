from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from Portrayals.AgentPortrayel import agent_portrayal
from Models.PluralityModel import PluralityModel
from Models.InstantRunoffModel import InstantRunoffModel

grid = CanvasGrid(agent_portrayal, 100, 100, 500, 500)
params = { "n_partys": UserSettableParameter("slider", "Party's Amount", 3, 3, 10),
           "n_voters": UserSettableParameter("slider", "Voters Amount", 10, 10, 9990) }
server = ModularServer(InstantRunoffModel, [grid], 'Instantrunoff Model', model_params=params)
