class Team:

    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, test_player):
        for player in self.players:
            if player == test_player:
                return True
        else:
            return False
    
    def play_game(self, result):
        if result == True:
            self.points += 3
        
    