import pandas as pd
import numpy as np

class Challenge():
    def __init__(self, id, challenge, value, category, sobriety_score):
        self.id = id
        self.challenge = challenge
        self.value = value
        self.category = category
        self.sobriety_score = sobriety_score

    def extract_challenges(self, path):
        
        # read the Excel file and store the contents in a Pandas DataFrame
        df = pd.read_excel(path)
        i_id = 0
        challenge_list = []
        for c in df:
            challenge = Challenge(i_id,...)
            challenge_list.append(challenge)
        
        return challenge_list
        


