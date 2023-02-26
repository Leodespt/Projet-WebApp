import datetime

class Timer():
    # Initialise the challenge class
    def __init__(self, start_time, interval):
        self.start_time = start_time
        self.interval = interval

    # Prend en parametre si oui ou non le bouton "Start Game" a été touché
    def game_start_time():
        # get the current date and time
        start = datetime.datetime.now()
        return start