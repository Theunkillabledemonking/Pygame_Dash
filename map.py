# map.py

import pygame
from settings import SCREEN_HEIGHT

def setup_map():
    """맵과 장애물 위치를 설정하는 함수"""
    player = pygame.Rect(100, SCREEN_HEIGHT - 150, 50, 50)

    obstacles = [
        pygame.Rect(900, SCREEN_HEIGHT - 150, 30, 30),
        pygame.Rect(1200, SCREEN_HEIGHT - 150, 30, 30),
        pygame.Rect(1600, SCREEN_HEIGHT - 150, 30, 30)
    ]

    return player, obstacles
