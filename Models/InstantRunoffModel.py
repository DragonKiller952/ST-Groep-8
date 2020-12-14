from Models.VoteModel import VoteModel

class InstantRunoffModel(VoteModel):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
       
    # Removes the losing team from the voting list and 
    # stops the simulation when a party has 50% or more of the votes
    def custom_strategy(self):
        self.partys.pop()
        winner = [party for party in self.partys if self.get_percentage(party.votes) > 50]
        if len(winner) == 1:
            self.running = False
