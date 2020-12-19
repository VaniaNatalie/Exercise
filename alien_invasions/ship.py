import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.bmp')

        # Initiate the image and screen as a rect (rectangle) for easier control in the coordinates
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start position of ship will be at bottom of screen and center in x axis
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Self movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the position to the screen position specified
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Move ship if moving_right or moving_left is True and make ship position
        # not exceeding screen size
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed

        # Update rect object from self.center
        self.rect.centerx = self.center

    def recenter_ship(self):
        self.center = self.screen_rect.centerx