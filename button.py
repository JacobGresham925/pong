import pygame.font


class Button:

    def __init__(self, screen, msg, msg2, msg3, winner):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 1200, 800
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.text_color2 = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont(None, 80)
        self.font3 = pygame.font.SysFont(None, 60)
        self.font4 = pygame.font.SysFont(None, 100)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Define in init to get rid of weak errors
        self.msg_image = 0
        self.msg_image_rect = 0
        self.msg2_image = 0
        self.msg2_image_rect = 0
        self.msg3_image = 0
        self.msg3_image_rect = 0
        self.winner_image = 0
        self.winner_image_rect = 0

        # The button message needs to be prepped only once.
        self.prep_msg(msg)
        self.prep_msg2(msg2)
        self.prep_msg3(msg3)
        self.prep_winner(winner)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_msg2(self, msg2):
        """Turn msg into a rendered image and center text on the button."""
        self.msg2_image = self.font2.render(msg2, True, self.text_color, self.button_color)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect.center
        self.msg2_image_rect.centery -= 100

    def prep_msg3(self, msg3):
        """Turn msg into a rendered image and center text on the button."""
        self.msg3_image = self.font3.render(msg3, True, self.text_color, self.button_color)
        self.msg3_image_rect = self.msg3_image.get_rect()
        self.msg3_image_rect.center = self.rect.center
        self.msg3_image_rect.centery -= 50

    def prep_winner(self, winner):
        """Turn msg into rendered image and center text"""
        self.winner_image = self.font4.render(winner, True, self.text_color2, self.button_color)
        self.winner_image_rect = self.winner_image.get_rect()
        self.winner_image_rect.center = self.rect.center
        self.winner_image_rect.centery -= 250

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
        self.screen.blit(self.msg3_image, self.msg3_image_rect)
        self.screen.blit(self.winner_image, self.winner_image_rect)
