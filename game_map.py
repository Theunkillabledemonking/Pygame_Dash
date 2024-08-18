# 맵 구성요소, 맵 길이 설정 등 관리
import pygame
from obstacles import create_obstacles
from setting import screen_height

def setup_map():
    """맵 설정 및 요소 초기화"""
    player = pygame.Rect(100, screen_height - 150, 50, 50)
    obstacles = [
        pygame.Rect(900, 450, 30, 30),
        pygame.Rect(1200, 450, 30, 30),
        pygame.Rect(1600, 450, 30, 30)
    ]
    return player, obstacles