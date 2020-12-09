from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

import functools as ft

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
            agent = agent_type(self.agentId, coords, self.vote_strategy, self)
            agents.append(agent)
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1            
        return agents

    def step(self):
        self.schedule.step()
        self.chose_winner()

    def chose_winner(self):
        self.partys = sorted(self.partys, key=lambda x: x.votes, reverse=True)
        for i, party in enumerate(self.partys):
            party.place = i + 1
            print(f'Party with id {party.name} got {party.votes} votes and placed {party.place}')
        winning_party = self.partys[0]
        print(f'Party with id {winning_party.name} won with {winning_party.votes} votes and is {winning_party.place} place')

    def vote_strategy(self, other):
        closest_party = ft.reduce(lambda a, b: a if other.distance_to(a.coords) < other.distance_to(b.coords) else b, self.partys)
        closest_party.votes += 1
        other.vote = closest_party
