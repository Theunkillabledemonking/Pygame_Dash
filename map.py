import pygame
from setting import screen_width, screen_height, FPS, image_path, map_lenth
def setup_map():
    """맵 설정 및 요소 초기화"""
    player = pygame.Rect(100, screen_height - 150, 50, 50)
    obstacles = [
        pygame.Rect(900, 450, 30, 30),
        pygame.Rect(1200, 450, 30, 30),
        pygame.Rect(1600, 450, 30, 30)
    ]
    return player, obstacles