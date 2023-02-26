from challenge import Challenge
import Player
import pandas as pd


if __name__ == '__main__':
    path = './Challenges.xlsx'
    df = Challenge.extract_challenges(path)
    list_challenge = Challenge.challenge_to_instance(df)
    for challenge in list_challenge:
        print(challenge.__repr__())
        
    print('hello')