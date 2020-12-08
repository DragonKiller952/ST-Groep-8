from mesa import Agent

class VoterAgent(Agent):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.name = name

    def step(self):
        print("{} activated".format(self.name))
