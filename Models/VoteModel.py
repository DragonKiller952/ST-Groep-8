from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

import functools as ft

class VoteModel(Model):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
        self.allcoords = []
        self.schedule = BaseScheduler(self)
        self.grid = MultiGrid(100, 100, torus=False)
        self.colors = ['green', 'red', 'purple', 'orange', 'brown', 'yellow', 'pink', 'cyan', 'lime', 'black']
        self.usedcolors = []
        self.agentId = 0
        self.voters = self.spawn_agents(VoterAgent, n_voters)
        self.partys = self.spawn_agents(PartyAgent, n_partys)

    def spawn_agents(self, agent_type, agent_amount):
        agents = []
        for i in range(agent_amount):
            coords = (self.random.randrange(0, 100), self.random.randrange(0, 100))
            while coords in self.allcoords:
                coords = (self.random.randrange(0, 100), self.random.randrange(0, 100))
            self.allcoords.append(coords)

            if agent_type == PartyAgent:
                color = self.random.choice(self.colors)
                while color in self.usedcolors:
                    color = self.random.choice(self.colors)
                self.usedcolors.append(color)
                agent = agent_type(self.agentId, coords, color, self.vote_strategy, self)
            else:
                agent = agent_type(self.agentId, coords, self.vote_strategy, self)
            agents.append(agent)
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1
        return agents

    def step(self):
        self.schedule.step()
        self.chose_winner()
        self.reset_votes()

    def chose_winner(self):
        self.partys = sorted(self.partys, key=lambda x: x.votes, reverse=True)
        for i, party in enumerate(self.partys):
            party.place = i + 1
            print(f'Party with id {party.name}({party.color}) got {party.votes} votes ({self.get_percentage(party.votes)}%) and placed {party.place}')
        winning_party = self.partys[0]
        print(f'Party with id {winning_party.name}({winning_party.color}) won with {winning_party.votes} votes ({self.get_percentage(winning_party.votes)}%) and is {winning_party.place} place')
        self.custom_strategy()

    def get_percentage(self, value):
        return round(value / len(self.voters) * 100, 2)

    def custom_strategy(self):
        self.partys.pop()

    def reset_votes(self):
        [party.reset() for party in self.partys]

    def vote_strategy(self, other):
        closest_party = ft.reduce(lambda a, b: a if other.distance_to(a.coords) < other.distance_to(b.coords) else b, self.partys)
        closest_party.votes += 1
        other.vote = closest_party
