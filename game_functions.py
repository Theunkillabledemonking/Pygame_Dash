# game_functions.py

import pygame

def load_images(image_path):
    """이미지와 음악을 로드하고 반환하는 함수"""
    background = pygame.image.load(os.path.join(image_path, "background_part1.png"))
    player_img = pygame.image.load(os.path.join(image_path, "Cube.png"))
    obstacle_img = pygame.image.load(os.path.join(image_path, "spikes.png"))

    # 배경음악 파일 로드
    pygame.mixer.music.load(os.path.join(image_path, "stereoMadness.wav"))

    return background, player_img, obstacle_img

def check_collisions(player, obstacles):
    """플레이어와 장애물 간의 충돌 체크"""
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Collision detected!")
            return True
    return False

def calculate_progress(distance_travelled, map_length):
    """진행도를 계산하는 함수"""
    return min(distance_travelled / map_length * 100, 100)
