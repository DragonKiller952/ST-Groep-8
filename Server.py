from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from Models.PluralityModel import PluralityModel
from Models.InstantRunoffModel import InstantRunoffModel
from Models.PrefrenceModel import PrefrenceModel

from Portrayals.AgentPortrayel import agent_portrayal
from Modules.HistogramModule import HistogramModule

# Interactive visulization
grid = CanvasGrid(agent_portrayal, 100, 100, 500, 500)
histogram = HistogramModule(list(range(10)), 200, 500)
params = { "n_partys": UserSettableParameter("slider", "Party's Amount", 10, 3, 10), 
           "n_voters": UserSettableParameter("slider", "Voters Amount", 1000, 10, 9990) }
server = ModularServer(PrefrenceModel, [grid, histogram], 'Prefrence Model', model_params=params)
