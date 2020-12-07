import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt


class VoterAgent(Agent):
    """An agent with randomg generated voorkeur voor 3 standpunten."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def vote():

# berekent hoever hij van alles af zit
# berekent zijn gemiddeldes

#def step:
# Stemmen, als zijn eerste keus vervalt opnieuw stemmen gemiddelde veranderen naar 101

class Lijsttrekker(Agent):

class Votemodel(Model):
    def __init__(self, N):
        self.num_agents = N
        # Create agents
        for i in range(self.num_agents):
            a = VoterAgent(i, self)
#init staat, aantal voters en partijen meegeven
# Create agents
# Def step, wat moet het model elke stap van de simulatie doen (self.datacollector.collect(self)
#                                                               self.schedule.step())





