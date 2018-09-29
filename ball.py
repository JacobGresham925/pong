import pygame
import random


class Ball:

    def __init__(self, ai_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ball in middle of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ball's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Starting movement of ball
        self.movex = random.uniform(-1.0, 1.0) * 1.25
        self.movey = random.uniform(-1.0, 1.0) * 1.25

    def draw_ball(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.centerx -= self.movex
        self.centery -= self.movey
        self.rect.x = self.centerx
        self.rect.y = self.centery

    def center_ball(self):
        """Center the ball on the screen."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery

        if self.movex < 0:
            self.movex -= 0.02
        if self.movex > 0:
            self.movex += 0.02
        if self.movey < 0:
            self.movey -= 0.02
        if self.movey > 0:
            self.movey += 0.02

        self.movex = random.uniform(-1.0, 1.0) * 1.25
        self.movey = random.uniform(-1.0, 1.0) * 1.25
