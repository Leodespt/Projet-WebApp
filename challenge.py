import pandas as pd

class Challenge():
    # Initialise the challenge class
    def __init__(self, id, challenge, value, category, sobriety_score):
        self.id = id
        self.challenge = challenge
        self.value = value
        self.category = category
        self.sobriety_score = sobriety_score

    
    def extract_challenges(path):
        
        # define the column names
        column_names = ['Challenge', 'Value', 'Category', 'Sobriety score']
        # read the Excel file and store the contents in a Pandas DataFrame
        df = pd.read_excel(path,names = column_names)
        # return the dataframe
        return df

    def challenge_to_instance(df):
        # Initialise an empty challenge list
        challenge_list = []
        # For each row/challenge in the dataframe
        for index, challenge in df.iterrows():
            # Create a challenge instance
            c = Challenge(index,challenge['Challenge'],challenge['Value'],challenge['Category'],challenge['Sobriety score'])
            # Append the challenge to the list
            challenge_list.append(c)
        #return the challenge list
        return challenge_list

    # returns informations about a challenge though a string
    def __repr__(self):
        return "Id : {0}, \nChallenge : {1}, \nValue : {2}, Category : {3}, Sobriety score : {4}\n".format(self.id,self.challenge, self.value, self.category, self.sobriety_score)
        


