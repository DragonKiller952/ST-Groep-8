from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

class PluralityModel(Model):
    def __init__(self, n_partys, n_voters):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=False)
        self.agentId = 0
        self.spawn_agents(PartyAgent, n_partys)
        self.spawn_agents(VoterAgent, n_voters)

    def spawn_agents(self, agent_type, agent_amount):
        for i in range(agent_amount):
            agent = agent_type(self.agentId, self)
            coords = (self.random.randrange(0, 10), self.random.randrange(0, 10))
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1

    def step(self):
        self.schedule.step()
        self.dc.collect(self)