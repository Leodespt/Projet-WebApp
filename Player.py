class Player():
    def __init__(self, name, score, actual_challenge=None, passed_challenges=None):
        self.name = name
        self.score = score
        self.actual_challenge = actual_challenge
        self.passed_challenges = [] if passed_challenges is None else passed_challenges

    # returns informations about a player though a string
    def __repr__(self):
        return "Name : {0}, Score : {1}, \nActual Challenge : {2}, \nPassed Challenges : {3}\n".format(self.name, self.score, self.actual_challenge, self.passed_challenges)
        