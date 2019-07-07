




class PlayerInfo:
    def __init__(self):
        self.player_health = 100
        self.player_shields = 50

    def update_player_health(self, shields, health):

        self.player_shields = shields
        self.player_health = health