from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from Portrayals.VoterPortrayal import voter_portrayal
from Models.PluralityModel import PluralityModel

grid = CanvasGrid(voter_portrayal, 10, 10, 500, 500)
server = ModularServer(PluralityModel,
                       [grid],
                       "My Model",
                       {'n_agents': 10})
