from mesa import Agent

class PartyAgent(Agent):
    def __init__(self, name, coords, color, vote_strategy, model):
        super().__init__(name, model)
        self.name = name
        self.coords = coords
        self.color = color
        self.votes = 0
        self.place = 0

    # Resets the vote count
    def reset(self):
        self.votes = 0