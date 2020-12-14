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
        self.chose_winner()
        winner = [party for party in self.partys if self.get_percentage(party.votes) > 50]
        if len(winner) == 1:
            self.running = False

    # Votes for it's prefrence axis or uses the normal strategy
    def vote_strategy(self, other):
        if other.axis == 0 or other.axis == 1:
            prefrence_party = ft.reduce(lambda a, b: a if abs(other.coords[other.axis] - a.coords[other.axis]) < abs(other.coords[other.axis] - b.coords[other.axis]) else b, self.partys)
            prefrence_party.votes += 1
            other.vote = prefrence_party
            other.prefrence = True
        else:
            super().vote_strategy(other)
            other.prefrence = False
