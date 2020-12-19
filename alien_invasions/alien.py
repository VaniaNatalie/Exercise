import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start alien at top left corner with space
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw alien at current location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Move aliens
        self.x += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.x = self.x
