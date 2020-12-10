from Models.VoteModel import VoteModel

class PluralityModel(VoteModel):
    def __init__(self, n_partys, n_voters):
        super().__init__(n_partys, n_voters)
