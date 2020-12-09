from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

class PluralityModel(Model):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
        self.schedule = BaseScheduler(self)
        self.grid = MultiGrid(10, 10, torus=False)
        self.agentId = 0
        self.spawn_agents(VoterAgent, n_voters)
        self.partys = self.spawn_agents(PartyAgent, n_partys)

    def spawn_agents(self, agent_type, agent_amount):
        agents = []
        for i in range(agent_amount):
            coords = (self.random.randrange(0, 10), self.random.randrange(0, 10))
            agent = agent_type(self.agentId, coords, self)
            agents.append(agent)
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1
        return agents

    def step(self):
        self.schedule.step()

        winning_party = None
        winning_votes = 0
        for party in self.partys:
            if winning_votes <= party.votes:
                winning_party = party
                winning_votes = party.votes
        winning_party.winner = True

        print(f'Party with id {winning_party.name} won with {winning_votes} votes')
