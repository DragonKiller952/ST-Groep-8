from mesa import Agent
from math import sqrt

class VoterAgent(Agent):
    def __init__(self, name, coords, color, vote_strategy, model):
        super().__init__(name, model)
        self.name = name
        self.coords = coords
        self.color = color
        self.vote_strategy = vote_strategy
        self.model = model
        
        self.vote = None
        self.axis = self.random.randrange(0, 2)
        self.chose_prefrence = False

    # Calculates distance from self to target
    def distance_to(self, target):
        return sqrt((abs(self.coords[0] - target[0])**2) + (abs(self.coords[1] - target[1])**2))

    def step(self):
        self.vote_strategy(self)
