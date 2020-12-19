import pygame.font
from pygame.sprite import Group

# Import classes
from ship import Ship


class Scoreboard:
    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Drawing score, highscore, levels and num of ships
        self.prep_score()
        self.prep_high_score()
        self.prep_levels()
        self.prep_ships()

    def prep_score(self):
        # Turn score into rendered image
        rounded_score = round(self.stats.score, -1)
        # Insert commas into the number when converting to string
        score_str = '{:,}'.format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Displaying score on top right
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 30

    def prep_high_score(self):
        # Turn high score into rendered image
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(high_score)
        self.high_score_img = self.font.render(high_score_str, True,
                                               self.text_color, self.settings.bg_color)

        # Displaying highscore on top
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_levels(self):
        # Turn level into rendered image
        self.level_img = self.font.render(str(self.stats.level), True,
                                          self.text_color, self.settings.bg_color)

        # Displaying level below score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        # Drawing the score, highscore and levels
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)

        # Drawing number of ships left
        self.ships.draw(self.screen)

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.num_ships_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)