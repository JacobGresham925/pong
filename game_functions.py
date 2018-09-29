import sys
import pygame
from time import sleep
import random


def check_keydown_events(event, paddles):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        paddles.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = True
    elif event.key == pygame.K_UP:
        paddles.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddles.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, paddles):
    """Respond to releases"""
    if event.key == pygame.K_RIGHT:
        paddles.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = False
    elif event.key == pygame.K_UP:
        paddles.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddles.moving_down = False


def check_events(ai_settings, paddles, play_button, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, play_button, mouse_x, mouse_y, sb)


def check_play_button(ai_settings, play_button, mouse_x, mouse_y, sb):
    button_pressed = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_pressed and not ai_settings.game_active:
        ai_settings.game_active = True
        sb.prep_level()
        sb.prep_playerscore()
        sb.prep_aiscore()


def ball_collision(ball, paddles, effect):
    effect.play()
    # Will speed up ball if it start off to slow
    if ball.movex < 0:
        if ball.movex > -0.5:
            ball.movex -= 0.5
    if ball.movex > 0:
        if ball.movex < 0.5:
            ball.movex += 0.5
    if ball.movey < 0:
        if ball.movey > -0.5:
            ball.movey -= 0.5
    if ball.movey > 0:
        if ball.movey < 0.5:
            ball.movey += 0.5

    # Speeds up ball every time it hits a paddle
    if ball.movex < 0:
        ball.movex -= 0.05
    if ball.movex > 0:
        ball.movex += 0.05
    if ball.movey < 0:
        ball.movey -= 0.05
    if ball.movey > 0:
        ball.movey += 0.05
    # Change direction of the ball
    if pygame.Rect.colliderect(ball.rect, paddles.rect1) or pygame.Rect.colliderect(ball.rect, paddles.rect4):
        ball.movex *= -1
    else:
        ball.movey *= -1


def update_paddles(paddles):
    paddles.update()


def update_ball(ball, ai_settings, paddles, divider, stats, sb, effect, play_button):
    ball.update()
    if pygame.Rect.colliderect(ball.rect, paddles.rect1) or pygame.Rect.colliderect(ball.rect, paddles.rect2):
        ball_collision(ball, paddles, effect)
    if pygame.Rect.colliderect(ball.rect, paddles.rect3) or pygame.Rect.colliderect(ball.rect, paddles.rect4):
        ball_collision(ball, paddles, effect)
    if pygame.Rect.colliderect(ball.rect, paddles.rect5) or pygame.Rect.colliderect(ball.rect, paddles.rect6):
        ball_collision(ball, paddles, effect)

    if ball.rect.centerx < 0:
        stats.aiscore += 1
        ball_reset(ball, sb)
    if ball.rect.centerx > 1200:
        stats.playerscore += 1
        ball_reset(ball, sb)
        ai_settings.ai_speed_factor += 0.05
    if ball.rect.centery < 0 and ball.rect.centerx < divider.rect.centerx:
        stats.aiscore += 1
        ball_reset(ball, sb)
    if ball.rect.centery < 0 and ball.rect.centerx > divider.rect.centerx:
        stats.playerscore += 1
        ball_reset(ball, sb)
        ai_settings.ai_speed_factor += 0.05
    if ball.rect.centery > 800 and ball.rect.centerx < divider.rect.centerx:
        stats.aiscore += 1
        ball_reset(ball, sb)
    if ball.rect.centery > 800 and ball.rect.centerx > divider.rect.centerx:
        stats.playerscore += 1
        ball_reset(ball, sb)
        ai_settings.ai_speed_factor += 0.05
    if stats.playerscore == 7 or stats.aiscore == 7:
        if stats.playerscore == 7:
            stats.winner = "PLAYER WINS"
            winner = stats.winner
            play_button.prep_winner(winner)
        if stats.aiscore == 7:
            stats.winner = "AI WINS"
            winner = stats.winner
            play_button.prep_winner(winner)
        ai_settings.game_active = False
        ball_reset(ball, sb)
        stats.playerscore = 0
        stats.aiscore = 0
        ai_settings.ai_speed_factor = 0.8
        ball.movex = random.uniform(-1.0, 1.0) * 1.25
        ball.movey = random.uniform(-1.0, 1.0) * 1.25


def ball_reset(ball, sb):
    ball.center_ball()
    sb.prep_level()
    sb.prep_playerscore()
    sb.prep_aiscore()
    sleep(0.5)


def update_screen(ai_settings, screen, paddles, ball, divider, play_button, sb):
    """Updates images on the screen and flip the new screen"""
    # Redraw screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw the paddles
    paddles.draw_paddle()
    ball.draw_ball()
    divider.draw_divider()
    sb.show_score()
    if not ai_settings.game_active:
        play_button.draw_button()
    pygame.display.flip()
