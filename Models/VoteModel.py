from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent
from Agents.VoterAgent import VoterAgent

import functools as ft
import Helper as hp

class VoteModel(Model):
    # Init of the model with the slider values n_partys and n_voters
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
        self.schedule = BaseScheduler(self)
        self.grid = MultiGrid(100, 100, torus=False)
        self.agentId = 0

        self.all_colors = ['green', 'red', 'purple', 'orange', 'brown', 'yellow', 'pink', 'cyan', 'lime', 'black']
        self.used_colors = []

        self.all_coords = list((i, j) for i in range(100) for j in range(100))
        self.used_coords = []
            
        self.partys = self.spawn_agents(PartyAgent, n_partys, hp.id_coord, hp.id_color)
        self.voters = self.spawn_agents(VoterAgent, n_voters, hp.unique_random, hp.standard_color)

    # Spawning of agents (party or voter agents) while setting amount, coords and color 
    def spawn_agents(self, agent_type, agent_amount, agent_coords, agent_color):
        agents = []
        for i in range(agent_amount):            
            # Generating random agent coordinates and colors and creating a new agent in the simulation
            coords = agent_coords(self, self.all_coords, self.used_coords)
            color = agent_color(self, self.all_colors, self.used_colors)

            # Creating a new agent with the generated properties and passing the vote strategy and refrence to this model to the voter agent
            agent = agent_type(self.agentId, coords, color, self.vote_strategy, self)
            agents.append(agent)
            
            # Placing the agent on the grid and adding them to the schedule and upping the agentId 
            self.schedule.add(agent)
            self.grid.place_agent(agent, coords)
            self.agentId += 1
        return agents
        
    # Step event that acts as an update over time(ticks)
    def step(self):
        self.early_step()
        self.schedule.step()
        self.late_step()

    # Step event before each schedule
    def early_step(self):
        return

    # Step event after each schedule
    def late_step(self):
        return   

    # Sorting party's on vote count and chosing winner
    def compute_winner(self):
        self.partys = sorted(self.partys, key=lambda x: x.votes, reverse=True)
        for i, party in enumerate(self.partys):
            party.place = i + 1
        winning_party = self.partys[0]
        return winning_party

    # Getting the vote percentage based on the amount of votes
    def get_vote_percentage(self, votes_amount):
        return round(votes_amount / len(self.voters) * 100, 2)

    # Reseting the votes of all party's
    def reset_votes(self):
        [party.reset() for party in self.partys]

    # Default voting strategy for chosing the closest party, voting strategy's gets injected into VoterAgents
    def vote_strategy(self, voting_agent):
        closest_party = ft.reduce(lambda a, b: a if voting_agent.distance_to(a.coords) < voting_agent.distance_to(b.coords) else b, self.partys)
        closest_party.votes += 1
        voting_agent.vote = closest_party
