import pygame
from pygame.sprite import Group

# import classes
from settings import Settings
from ship import Ship
from stats import Stats
from button import Button
from scoreboard import Scoreboard

# import functions
import game_functions as func


def run_game():
    # Initialize game and settings
    pygame.init()
    settings = Settings()

    # Create a display window called screen with dimensions
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make play button, stats instance, ship instance and scoreboard instance
    play_button = Button(screen, settings, "Play")
    stats = Stats(settings)
    ship = Ship(screen, settings)
    sb = Scoreboard(screen, settings, stats)

    # Group to store bullets and group to store aliens
    bullets = Group()
    aliens = Group()

    # Creating fleets of aliens
    func.create_fleet(settings, screen, aliens, ship)

    # Start the main loop for the game
    while True:
        # Accessing events triggered by keyboard and mouse
        func.ongoing_event(settings, screen, ship, aliens, bullets, stats, play_button, sb)

        if stats.game_active:
            # Updating ship position
            ship.update()

            # Updating bullets
            func.update_bullets(bullets, settings, screen, aliens, ship, stats, sb)

            # Updating aliens position
            func.update_aliens(screen, settings, aliens, ship, bullets, stats, sb)

        # Redrawing display per second
        func.update_display(settings, screen, ship, bullets, aliens, stats, play_button, sb)


run_game()