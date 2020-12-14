from Models.VoteModel import VoteModel

class InstantRunoffModel(VoteModel):
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
