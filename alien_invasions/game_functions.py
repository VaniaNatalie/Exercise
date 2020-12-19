import pygame

# For player to exit game
import sys

# For giving time breaks
from time import sleep

# Import class
from bullet import Bullet
from alien import Alien


def ongoing_event(settings, screen, ship, aliens, bullets, stats, play_button, sb):
    # Accessing events triggered by keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Return tuple of x and y coordinates of mouse cursor when clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click_play_button(settings, screen, ship, bullets, aliens, stats, sb,
                              play_button, mouse_x, mouse_y)


def click_play_button(settings, screen, ship, bullets, aliens, stats, sb,
                      play_button, mouse_x, mouse_y):
    # Start new game when player clicks play button
    # Check if the coordinates where mouse is clicked overlaps with play button
    clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not stats.game_active:
        # Hide mouse cursor once games start
        # pygame.mouse.set_visible(False)

        # Reset values
        settings.initialize_dynamic_settings()
        stats.reset()
        stats.game_active = True

        # Updating scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_levels()
        sb.prep_ships()

        # Empty aliens and bullets
        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, aliens, ship)
        ship.recenter_ship()


def keydown(event, settings, screen, ship, bullets):
    # Move ship to right if press right or left arrow
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it to bullets group
        if len(bullets) < settings.bullets_allowed:
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)


def keyup(event, ship):
    # Stops movement if button is released
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_display(settings, screen, ship, bullets, aliens, stats, play_button, sb):
    # Drawing background color and ship
    screen.fill(settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make ship appear on screen
    ship.blitme()

    # Draw an alien group at the position defined
    aliens.draw(screen)

    # Draw score information
    sb.show_score()

    # Draw play button if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # For updating the display with recently drawn stuff
    pygame.display.flip()


def update_bullets(bullets, settings, screen, aliens, ship, stats, sb):
    # Updating bullet position
    bullets.update()

    # Deleting bullets
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    alien_bullet_collision(settings, screen, ship, bullets, aliens, stats, sb)


def alien_bullet_collision(settings, screen, ship, bullets, aliens, stats, sb):
    # Bullets colliding with aliens and destroying both upon collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # The bullet colliding with aliens become a key, with the aliens it collided with as the value

    # Create new fleet after fleet is finished (+1 level each created)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_levels()

        # Create fleet
        create_fleet(settings, screen, aliens, ship)
    if collisions:
        for alienss in collisions.values():
            stats.score += settings.alien_points * len(alienss)
            sb.prep_score()
        check_highscore(stats, sb)


def calculate_number_aliens(settings, alien_width):
    # Create left and right margin, with a space equal to the alien's width
    space_x = settings.screen_width - 2 * alien_width
    # Numbers of aliens, with space equals to one alien width separating each aliens
    number_aliens = int(space_x / (2 * alien_width))
    return number_aliens


def number_rows(settings, alien_height, ship):
    # Create upper and lower margin
    space_y = settings.screen_height - (3 * alien_height + ship.rect.height)
    # Number of alien rows, with space equals to one alien height separating each alien rows
    num_rows = int(space_y / (2 * alien_height))
    return num_rows


def create_alien(screen, settings, aliens, alienss, rows):
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alienss
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    alien = Alien(screen, settings)
    number_aliens = calculate_number_aliens(settings, alien.rect.width)
    num_rows = number_rows(settings, alien.rect.height, ship)
    # Creating the first row of aliens
    for rows in range(num_rows):
        for alienss in range(number_aliens):
            create_alien(screen, settings, aliens, alienss, rows)


def check_alien_edges(settings, aliens):
    # Actions after aliens reached the edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_aliens_direction(settings, aliens)
            break


def change_aliens_direction(settings, aliens):
    # Change alien direction when reached edge
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    # Go to left
    settings.alien_direction *= -1


def ship_hit(screen, settings, aliens, ship, bullets, stats, sb):
    if stats.num_ships_left > 0:
        # Remove ship limit upon collision with aliens group
        stats.num_ships_left -= 1
        # Update scoreboard
        sb.prep_ships()
    else:
        stats.game_active = False
        # Set mouse to visible again once game ends
        # pygame.mouse.set_visible(True)

    # Empty screen of any aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create new fleet and recenter ship
    create_fleet(settings, screen, aliens, ship)
    ship.recenter_ship()

    # Break upon losing one ship
    sleep(1)


def alien_hit_bottom(screen, settings, aliens, ship, bullets, stats, sb):
    screen_rect = screen.get_rect()
    # If aliens reach bottom of screen, call ship_hit function
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, settings, aliens, ship, bullets, stats, sb)
            break
            # There is no need to check other aliens if one already go over the bottom screen


def update_aliens(screen, settings, aliens, ship, bullets, stats, sb):
    # Updating aliens position
    check_alien_edges(settings, aliens)
    aliens.update()

    # Collisions between aliens group and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, settings, aliens, ship, bullets, stats, sb)

    # Aliens go over the bottom of screen
    alien_hit_bottom(screen, settings, aliens, ship, bullets, stats, sb)


def check_highscore(stats, sb):
    # Check if there's a new highscore
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()