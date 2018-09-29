
import pygame
from settings import Settings
from paddles import Paddle
import game_functions as gf
from ball import Ball
from divider import Divider
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")
    stats = GameStats(ai_settings)
    winner = stats.winner
    play_button = Button(screen, "PLAY GAME", "PONG", "AI -- NO WALLS", winner)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make paddles, ball, divider
    divider = Divider(ai_settings, screen)
    ball = Ball(ai_settings, screen)
    paddles = Paddle(ai_settings, screen, divider, ball)
    effect = pygame.mixer.Sound('audio/pop2.wav')

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, paddles, play_button, sb)
        if ai_settings.game_active:
            gf.update_paddles(paddles)
            gf.update_ball(ball, ai_settings, paddles, divider, stats, sb, effect, play_button)
        gf.update_screen(ai_settings, screen, paddles, ball, divider, play_button, sb)


run_game()
