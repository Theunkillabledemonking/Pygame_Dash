# 장애물의 생성, 이동, 충돌 처리 등 관리

import pygame

def create_obstacles():
    """초기 장애물 설정"""
    obstacles = [
        pygame.Rect(900, 450, 30, 30),
        pygame.Rect(1200, 450, 30, 30),
        pygame.Rect(1600, 450, 30, 30)
    ]
    return obstacles

def move_obstacles(obstacles, game_speed, dt, screen_width):
    """장애물 이동 및 화면 밖으로 나간 장애물 처리"""
    for obstacle in obstacles:
        obstacle.left -= game_speed * dt
        if obstacle.right < 0 :
            obstacle.left = screen_width + obstacle.width