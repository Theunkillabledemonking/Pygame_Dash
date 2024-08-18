# 게임의 엔트리 포인트로, 전체 게임 루프를 관리하고 다른 모듈을 호출

import pygame
import sys
from setting import screen_width, screen_height, FPS, image_path, map_length
from game_functions import check_collisions, load_images, calculate_progress
from player import Player
from obstacles import create_obstacles, move_obstacles
from game_map import setup_map

def run_game():
    """게임 실행을 위한 메인 함수"""
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Geometry Dash")

    clock = pygame.time.Clock()
    #폰트 설정
    font = pygame.font.Font(None, 36)
    
    # 이미지 및 배경음악 로드
    background, player_img, obstacle_img = load_images(image_path)
    bg_width = background.get_width()

    # 플레이어 초기화
    player = Player(100, screen_height - 150)

    # 맵 설정
    _, obstacles = setup_map()

    # 게임 루프
    running = True
    bg_x = 0
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 플레이어 움직임 처리
        player.handle_movement()

        # 배경 그리기
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + bg_width, 0))

        # 회전된 플레이어 이미지 그리기
        rotated_image, rotated_rect = player.get_rotated_image()
        screen.blit(rotated_image, rotated_rect.topleft)

        # 장애물 이동 및 그리기
        move_obstacles(obstacles, 5, dt, screen_width)
        for obstacle in obstacles:
            screen.blit(obstacle_img, obstacle.topleft)

        # 충돌 처리
        if check_collisions(player.rect, obstacles):
            print("충돌! 게임오버!")
            running = False

        # 진행도 계산 및 표시
        distance_travelled = 0
        progress = calculate_progress(distance_travelled, map_length)
        progress_text = font.render(f"Progress : {int(progress)}%", True, (255, 255, 255))
        text_rect = progress_text.get_rect(center=(screen_width // 2, 50))
        screen.blit(progress_text, text_rect)

        # 화면 업데이트
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()