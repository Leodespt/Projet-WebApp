class ListPlayer():
    def __init__(self, list_players):
        self.list_players = list_players

    # returns informations about a player though a string
    def __repr__(self):
        string_list = ""
        for player in self.list_players:
            string_list += player.__repr__()+ "\n\n\n"
        return  string_list
        