class Challenge():
    def __init__(self, id, challenge, value, category, sobriety_score):
        self.id = id
        self.challenge = challenge
        self.value = value
        self.category = category
        self.sobriety_score = sobriety_score

    def extract_challenges(self, excel):
        

