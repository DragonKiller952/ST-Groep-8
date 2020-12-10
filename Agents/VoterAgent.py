from mesa import Agent
from math import sqrt

class VoterAgent(Agent):
    def __init__(self, name, coords, vote_strategy, model):
        super().__init__(name, model)
        self.name = name
        self.coords = coords
        self.vote = None
        self.vote_strategy = vote_strategy

    def distance_to(self, party_coords):
        return sqrt((abs(self.coords[0] - party_coords[0])**2) + (abs(self.coords[1] - party_coords[1])**2))

    def step(self):
        self.vote_strategy(self)
