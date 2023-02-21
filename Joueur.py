# id_joueur
#
#       nom
#
#       score
#
#       defi_actuel
#
#       defi_realise (Liste de defi)


class Joueur():
    def __init__(self, name, score, actual_challenge, passed_challenges):
        self.name = name
        self.score = score
        self.actual_challenge = actual_challenge
        self.passed_challlenges = passed_challenges