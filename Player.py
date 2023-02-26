class Player():
    def __init__(self, name, score, actual_challenge=None, passed_challenges=None):
        self.name = name
        self.score = score
        self.actual_challenge = actual_challenge
        self.passed_challlenges = [] if passed_challenges is None else passed_challenges
        self.passed_challlenges = passed_challenges


    # Prend en parametre si oui ou non le bouton "Add player" a été touché
    # Prend également en parametre le contenu du Input dans lequel le nom du joueur a été inscrit (name)
    def add_player(name):
        player = Player(name,0)
        return player