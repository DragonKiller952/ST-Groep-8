from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from Agents.PartyAgent import PartyAgent

class PluralityModel(Model):
    def __init__(self, n_agents):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10, 10, torus=True)
        for i in range(n_agents):
            a = PartyAgent(i, self)
            self.schedule.add(a)
            coords = (self.random.randrange(0, 10), self.random.randrange(0, 10))
            self.grid.place_agent(a, coords)
        # self.dc = DataCollector(model_reporters={"agent_count":
        #                             lambda m: m.schedule.get_agent_count()},
        #                         agent_reporters={"name": lambda a: a.name})

    def step(self):
        self.schedule.step()
        self.dc.collect(self)