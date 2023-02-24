class Player():
    def __init__(self, name, score, actual_challenge=None, passed_challenges=None):
        self.name = name
        self.score = score
        self.actual_challenge = actual_challenge
        self.passed_challlenges = [] if passed_challenges is None else passed_challenges
        self.passed_challlenges = passed_challenges