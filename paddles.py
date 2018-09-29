import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):

    def __init__(self, ai_settings, screen, divider, ball):
        super(Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.divider = divider
        self.divider_rect = divider.rect
        self.ball = ball
        self.ball_rect = ball.rect

        self.rect1 = pygame.Rect(0, 0, ai_settings.paddle_width, ai_settings.paddle_height)
        self.rect2 = pygame.Rect(0, 0, ai_settings.paddle_height, ai_settings.paddle_width)
        self.rect3 = pygame.Rect(0, 0, ai_settings.paddle_height, ai_settings.paddle_width)
        self.rect4 = pygame.Rect(0, 0, ai_settings.paddle_width, ai_settings.paddle_height)
        self.rect5 = pygame.Rect(0, 0, ai_settings.paddle_height, ai_settings.paddle_width)
        self.rect6 = pygame.Rect(0, 0, ai_settings.paddle_height, ai_settings.paddle_width)
        self.color1 = ai_settings.paddle_color1
        self.color2 = ai_settings.paddle_color2

        # Adjust positions of paddles
        self.rect1.centerx = 0 + ai_settings.paddle_width / 2
        self.rect1.centery = self.screen_rect.bottom / 2
        self.rect2.centerx = self.divider_rect.centerx / 2
        self.rect2.centery = 0 + ai_settings.paddle_width / 2
        self.rect3.centerx = self.divider_rect.centerx / 2
        self.rect3.centery = self.screen_rect.bottom - ai_settings.paddle_width / 2
        self.rect4.centerx = self.screen_rect.right - ai_settings.paddle_width / 2
        self.rect4.centery = self.screen_rect.bottom / 2
        self.rect5.centerx = self.screen_rect.right - (self.divider_rect.centerx / 2)
        self.rect5.centery = 0 + ai_settings.paddle_width / 2
        self.rect6.centerx = self.screen_rect.right - (self.divider_rect.centerx / 2)
        self.rect6.centery = self.screen_rect.bottom - ai_settings.paddle_width / 2

        # Store a decimal value for the paddle's center
        self.center1 = float(self.rect1.centery)
        self.center2 = float(self.rect2.centerx)
        self.center3 = float(self.rect3.centerx)
        self.center4 = float(self.rect4.centery)
        self.center5 = float(self.rect5.centerx)
        self.center6 = float(self.rect6.centerx)
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # ai movement flags
        self.ai_right = False
        self.ai_left = False
        self.ai_up = False
        self.ai_down = False

    def draw_paddle(self):
        """Draw the paddle on the screen"""
        pygame.draw.rect(self.screen, self.color1, self.rect1)
        pygame.draw.rect(self.screen, self.color1, self.rect2)
        pygame.draw.rect(self.screen, self.color1, self.rect3)
        pygame.draw.rect(self.screen, self.color2, self.rect4)
        pygame.draw.rect(self.screen, self.color2, self.rect5)
        pygame.draw.rect(self.screen, self.color2, self.rect6)

    def update(self):
        """Update paddles, position based on movement flags."""
        if self.moving_up and self.rect1.top > 0:
            self.center1 -= self.ai_settings.paddle_speed_factor
        if self.moving_down and self.rect1.bottom < self.screen_rect.bottom:
            self.center1 += self.ai_settings.paddle_speed_factor
        if self.moving_right and self.rect2.right < self.divider_rect.left:
            self.center2 += self.ai_settings.paddle_speed_factor
        if self.moving_left and self.rect2.left > 0:
            self.center2 -= self.ai_settings.paddle_speed_factor
        if self.moving_right and self.rect3.right < self.divider_rect.left:
            self.center3 += self.ai_settings.paddle_speed_factor
        if self.moving_left and self.rect3.left > 0:
            self.center3 -= self.ai_settings.paddle_speed_factor

        # ai flag updater
        if self.rect4.centery < self.ball_rect.centery:
            self.ai_down = True
            self.ai_up = False
        if self.rect4.centery > self.ball_rect.centery:
            self.ai_up = True
            self.ai_down = False
        if self.rect5.centerx < self.ball_rect.centerx:
            self.ai_right = True
            self.ai_left = False
        if self.rect5.centerx > self.ball_rect.centerx:
            self.ai_left = True
            self.ai_right = False

        """Update ai paddles, based upon the ball"""
        if self.ai_up and self.rect4.top > 0:
            self.center4 -= self.ai_settings.ai_speed_factor
        if self.ai_down and self.rect4.bottom < self.screen_rect.bottom:
            self.center4 += self.ai_settings.ai_speed_factor
        if self.ai_right and self.rect5.right < self.screen_rect.right:
            self.center5 += self.ai_settings.ai_speed_factor
        if self.ai_left and self.rect5.left > self.divider_rect.right:
            self.center5 -= self.ai_settings.ai_speed_factor
        if self.ai_right and self.rect6.right < self.screen_rect.right:
            self.center6 += self.ai_settings.ai_speed_factor
        if self.ai_left and self.rect6.left > self.divider_rect.right:
            self.center6 -= self.ai_settings.ai_speed_factor

        self.rect1.centery = self.center1
        self.rect2.centerx = self.center2
        self.rect3.centerx = self.center3
        self.rect4.centery = self.center4
        self.rect5.centerx = self.center5
        self.rect6.centerx = self.center6
