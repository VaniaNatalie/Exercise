class Stats:
    def __init__(self, settings):
        self.settings = settings

        # Check if game is active
        self.game_active = False
        self.reset()

        self.high_score = 0

    def reset(self):
        self.num_ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1