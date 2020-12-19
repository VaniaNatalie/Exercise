class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 5

        # Alien settings
        self.alien_drop_speed = 0.5

        # How quickly game speeds up
        self.speedup = 1.2

        # How many times points are multiplied as levels increase
        self.points_multiplier = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Attributes changed with level change
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 5
        self.alien_points = 25

        # 1 for right, -1 for left
        self.alien_direction = 1

    def increase_speed(self):
        # Increase speed and points as we go up the levels
        self.ship_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_points = int(self.alien_points * self.points_multiplier)
