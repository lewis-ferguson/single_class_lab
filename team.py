

class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, player):
        self.players.append(player)
        return self.players
    
    
    
    def has_player(self, player_name):
        if player_name in self.players:
            print(player_name + " is in the list!")
        else:
            print("Player not found")       
                 
        
        
        # def has_player(self, player_name):
        # return player_name in self.players                      

    # def found_player(self, player_name):
    #     return self.players.count(player_name) > 0
    
    
    
    def play_game(self,game_won):
        if game_won:
            self.points += 3
        return self.points
