from mesa import Agent

class VoterAgent(Agent):
    def __init__(self, name, coords, model):
        super().__init__(name, model)
        self.name = name
        self.coords = coords
        self.vote = None

    def distance_to(self, agent_coords, party_coords):
        return abs(agent_coords[0] - party_coords[0]) + abs(agent_coords[1] - party_coords[1])

    def step(self):
        closest_party = None
        closest_distance = 99
        for party in self.model.partys:
            if closest_distance >= self.distance_to(self.coords, party.coords):
                closest_party = party
                closest_distance = self.distance_to(self.coords, party.coords)
        closest_party.votes += 1
