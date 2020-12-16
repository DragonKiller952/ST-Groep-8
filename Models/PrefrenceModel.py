from Models.VoteModel import *
from Models.InstantRunoffModel import InstantRunoffModel

class PrefrenceModel(VoteModel):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
       
    # Removes the losing team from the voting list and 
    def early_step(self):
        if self.partys[0].votes != 0:
            self.reset_votes()
            self.partys.pop()

    # stops the simulation when a party has 50% or more of the votes
    def late_step(self):
        self.compute_winner()
        winner = [party for party in self.partys if self.get_vote_percentage(party.votes) > 50]
        if len(winner) == 1:
            self.running = False

    # Votes for it's prefrence axis (x or y) or uses the normal strategy
    def vote_strategy(self, voting_agent):
        axis = voting_agent.axis
        if axis == 0 or axis == 1:
            prefrence_party = ft.reduce(lambda a, b: a if abs(voting_agent.coords[axis] - a.coords[axis]) < abs(voting_agent.coords[axis] - b.coords[axis]) else b, self.partys)
            prefrence_party.votes += 1
            voting_agent.vote = prefrence_party
            voting_agent.chose_prefrence = True
        else:
            super().vote_strategy(voting_agent)
            voting_agent.chose_prefrence = False
