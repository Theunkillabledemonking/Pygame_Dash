# main

import pygame
from setting import screen_width, screen_height, FPS, image_path, map_lenth
from game_functions import check_collisions, load_images, calculate_progress
from player import handle_player_movement
from obstacles import create_obstacles, move_obstacles
from map import setup_map

def run_game():
    """게임 실행을 위한 메인 함수"""
    pygame.init()
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Geometry Dash")
    
    clock = pygame.time.Clock()
    
    # 이미지 및 배경음악 로드
    background, player_img, obstacle_img = load_images(image_path)
    bg_width = background.get_width()
    
    # 배경음악 무한 반복 재생 시작
    pygame.mixer.music.play(-1)
    
    # 맵 설정
    player, obstacles = setup_map()
    
    # 게임 속도 및 중력 설정
    game_speed = 5
    y_vel = 0
    gravity = 1
    
    # 진행도 및 거리 설정
    distance_travelled = 0
    progress = 0
    
    # 폰트 설정
    font = pygame.font.Font(None, 36)
    
    # 게임 루프
    running = True
    bg_x = 0
    
    while running:
        dt = clock.tick(FPS) /1000
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
        move_obstacles(obstacles, game_speed, dt, screen_width)
        
        # 충돌 처리
        if check_collisions(player, obstacles):
            print("충돌! 게임오버!")
            running = False
            
        # 거리 및 진행도 계산
        distance_travelled += game_speed
        progress = calculate_progress(distance_travelled, map_lenth)
        
        # 화면 그리기
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + bg_width, 0))
        
        screen.blit(player_img, player)
        for obstacle in obstacles:
            screen.blit(obstacle_img, obstacle.topleft)
            
        # 진행도 표시
        progress_text = font.render(f"Progress : {int(progress)}%", True, (255, 255, 255))
        text_rect = progress_text.get_rect(center=(screen_width // 2, 50))
        screen.blit(progress_text, text_rect)
        
        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    run_game()