

shield_regen_timer = 6


class PlayerInfo:
    def __init__(self):
        self.player_health = 100
        self.player_shields = 50
        self.shield_regen_cooldown = 6

    def update_player_info(self, damage_taken = 0):
        if damage_taken > self.player_shields:
            self.player_health -= self.player_shields - damage_taken
        self.player_shields -= damage_taken
        self.shield_regen_cooldown -= 6
        if self.shield_regen_cooldown <= 0:
            self.player_shields += 1
            self.shield_regen_cooldown = 6
