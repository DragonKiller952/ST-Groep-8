from mesa import Agent

class PartyAgent(Agent):
    def __init__(self, name, coords, vote_strategy, model):
        super().__init__(name, model)
        self.name = name
        self.coords = coords
        self.votes = 0
        self.place = 0
