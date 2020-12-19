# Render text on screen
import pygame.font

class Button:
    def __init__(self, screen, settings, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensions of the button
        self.width, self.height = 200, 50
        self.color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Make button as rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        # Turn message into rendered image
        self.msg_img = self.font.render(msg, True, self.text_color, self.color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button then draw message
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)