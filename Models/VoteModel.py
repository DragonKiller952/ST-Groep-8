from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

import functools as ft

class VoteModel(Model):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
        self.schedule = BaseScheduler(self)
        self.grid = MultiGrid(100, 100, torus=False)
        self.agentId = 0

        self.all_colors = ['green', 'red', 'purple', 'orange', 'brown', 'yellow', 'pink', 'cyan', 'lime', 'black']
        self.used_colors = []

        self.all_coords = list((i, j) for i in range(100) for j in range(100))
        self.used_coords = []
        
        default_spawn_positions = [(12, 75), (30, 60), (40, 80), (40, 90), (60, 80), (50, 35), (60, 35), (65, 15), (75, 40), (90, 45)]
    
        self.partys = self.spawn_agents(PartyAgent, n_partys, self.unique_random, default_spawn_positions)
        self.voters = self.spawn_agents(VoterAgent, n_voters, lambda *args: 'blue')

    # Spawning of part and voter agents while setting positions and colors
    def spawn_agents(self, agent_type, agent_amount, agent_color, spawn_positions=None):
        agents = []
        for i in range(agent_amount):            
            spawn_positions = self.all_coords if spawn_positions == None else spawn_positions
            coords = self.unique_random(spawn_positions, self.used_coords)
            color = agent_color(self.all_colors, self.used_colors)
            agent = agent_type(self.agentId, coords, color, self.vote_strategy, self)
            agents.append(agent)
            
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1
        return agents

    # Chosing random without duplicates
    def unique_random(self, choices, used):
        choice = self.random.choice(choices)
        while choice in used:
            choice = self.random.choice(choices)
        used.append(choice)
        return choice
        
    def step(self):
        self.early_step()
        self.schedule.step()
        self.late_step()

    def early_step(self):
        return

    def late_step(self):
        return   

    # Sorting party's on vote count and excuting custom winner logic methode
    def chose_winner(self):
        self.partys = sorted(self.partys, key=lambda x: x.votes, reverse=True)
        for i, party in enumerate(self.partys):
            party.place = i + 1
            print(f'Party with id {party.name}({party.color}) got {party.votes} votes ({self.get_percentage(party.votes)}%) and placed {party.place}')
        winning_party = self.partys[0]
        print(f'Party with id {winning_party.name}({winning_party.color}) won with {winning_party.votes} votes ({self.get_percentage(winning_party.votes)}%) and is {winning_party.place} place')

    def get_percentage(self, value):
        return round(value / len(self.voters) * 100, 2)

    # Reseting the votes of all party's
    def reset_votes(self):
        [party.reset() for party in self.partys]

    # Default voting strategy for the closest party, voting strategy's gets injected into VoterAgents
    def vote_strategy(self, other):
        closest_party = ft.reduce(lambda a, b: a if other.distance_to(a.coords) < other.distance_to(b.coords) else b, self.partys)
        closest_party.votes += 1
        other.vote = closest_party
