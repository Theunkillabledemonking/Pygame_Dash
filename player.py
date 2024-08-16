# player.py

import pygame
from settings import SCREEN_HEIGHT

def handle_player_movement(player, y_vel, gravity):
    """플레이어의 점프 및 중력 적용"""
    keys = pygame.key.get_pressed()
    player.top += y_vel
    y_vel += gravity
    if player.bottom >= SCREEN_HEIGHT:
        y_vel = 0
        if keys[pygame.K_SPACE]:
            y_vel = -18
    return y_vel
