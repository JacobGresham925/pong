import pygame
from pygame.sprite import Sprite


class Divider(Sprite):

    def __init__(self, ai_settings, screen):
        super(Divider, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create a divider at center of screen to divide it in half
        self.rect = pygame.Rect(0, 0, ai_settings.divider_width,
                                ai_settings.divider_height)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.color = ai_settings.divider_color

    def draw_divider(self):
        """Draw the divider on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
