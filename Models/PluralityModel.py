from Models.VoteModel import VoteModel

class PluralityModel(VoteModel):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)

    # Resets vote 
    def early_step(self):
        self.reset_votes()

    # Calculates winner
    def late_step(self):
        self.compute_winner()