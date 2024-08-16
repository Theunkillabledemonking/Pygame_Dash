# main.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, IMAGE_PATH
from map import setup_map
from player.py import handle_player_movement
from game_functions import load_images, check_collisions, calculate_progress

def run_game():
    """게임 실행을 위한 메인 함수"""
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Long Map with Obstacles")

    clock = pygame.time.Clock()

    # 이미지 로드
    background, player_img, obstacle_img = load_images(IMAGE_PATH)
    bg_width = background.get_width()

    # 배경음악 무한 반복 재생 시작
    pygame.mixer.music.play(-1)

    # 맵 설정
    player, obstacles = setup_map()

    # 게임 속도 및 중력 설정
    game_speed = 5
    y_vel = 0
    gravity = 1

    # 맵 길이 및 진행도 설정
    map_length = 5000
    distance_travelled = 0
    progress = 0

    # 폰트 설정
    font = pygame.font.Font(None, 36)

    # 게임 루프
    running = True
    bg_x = 0

    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 플레이어 이동 처리
        y_vel = handle_player_movement(player, y_vel, gravity)

        # 배경 스크롤
        bg_x -= game_speed
        if bg_x <= -bg_width:
            bg_x = 0

        # 장애물 이동
        for obstacle in obstacles:
            obstacle.left -= game_speed * dt

        # 충돌 처리
        if check_collisions(player, obstacles):
            running = False

        # 거리 및 진행도 계산
        distance_travelled += game_speed
        progress = calculate_progress(distance_travelled, map_length)

        # 화면 그리기
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + bg_width, 0))

        screen.blit(player_img, player)
        for obstacle in obstacles:
            screen.blit(obstacle_img, obstacle.topleft)

        # 진행도 표시 (화면 중앙 상단)
        progress_text = font.render(f"Progress: {int(progress)}%", True, (255, 255, 255))
        text_rect = progress_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(progress_text, text_rect)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    run_game()
