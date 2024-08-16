import pygame
import os

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Long Map with Obstacles")

# 배경음악 파일 로드
background_music = pygame.mixer.music.load(os.path.join("C:\\Users\\USER\\Desktop\\Geometry Dash\\image", "stereoMadness.wav"))

# 배경음악 무한 반복 재생 시작
pygame.mixer.music.play(-1)

# FPS
clock = pygame.time.Clock()

# 이미지 경로 설정
current_path = os.path.dirname(__file__) 
image_path = os.path.join("C:\\Users\\USER\\Desktop\\Geometry Dash\\image")

# 배경 이미지 설정 (길게 이어 붙일 배경 이미지)
background = pygame.image.load(os.path.join(image_path, "background_part1.png"))
bg_width = background.get_width()

# 플레이어 캐릭터 설정
player = pygame.Rect(100, screen_height - 150, 50, 50)
player_img = pygame.image.load(os.path.join(image_path, "Cube.png"))
player_img = pygame.transform.scale(player_img, (50, 50))

# 장애물 설정 (여러 장애물 추가 가능)
obstacles = [
    pygame.Rect(900, screen_height - 150, 30, 30),
    pygame.Rect(1200, screen_height - 150, 30, 30),
    pygame.Rect(1600, screen_height - 150, 30, 30)
]

obstacle_img = pygame.image.load(os.path.join(image_path, "spikes.png"))
obstacle_img = pygame.transform.scale(obstacle_img, (30, 30))

# 게임 속도 및 중력 설정
game_speed = 5
y_vel = 0
gravity = 1

# 맵 길이 및 진행도 설정
map_length = 10000  # 맵의 총 길이
distance_travelled = 0  # 플레이어가 이동한 거리
progress = 0  # 진행도 (0~100%)

# 폰트 설정
font = pygame.font.Font(None, 36)  # 폰트 크기 설정

# 게임 루프
running = True
bg_x = 0  # 배경의 x 좌표 (스크롤을 위한 변수)

while running:
    dt = clock.tick(60) / 1000  # 프레임 시간 계산 (초 단위)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 점프 처리
    keys = pygame.key.get_pressed()
    player.top += y_vel
    y_vel += gravity
    if player.bottom >= screen_height:
        y_vel = 0
        if keys[pygame.K_SPACE]:
            y_vel = -18 
    
    # 배경 스크롤
    bg_x -= game_speed
    if bg_x <= -bg_width:
        bg_x = 0

    # 장애물 이동 (스크롤링 효과를 위해 장애물도 이동)
    for obstacle in obstacles:
        obstacle.left -= game_speed * dt

    # 장애물이 화면을 벗어나면 재설정
    for obstacle in obstacles:
        if obstacle.right < 0:
            obstacle.left = screen_width + obstacle.width

    # 충돌 처리
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Collision detected!")
            running = False  # 충돌 시 게임 종료

    # 거리 및 진행도 계산
    distance_travelled += game_speed
    progress = min(distance_travelled / map_length * 100, 100)

    # 맵 클리어 확인
    if progress >= 100:
        print("Map cleared!")
        running = False  # 게임 클리어 시 종료

    # 화면 그리기
    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + bg_width, 0))  # 배경을 반복해서 그리기

    screen.blit(player_img, player)
    for obstacle in obstacles:
        screen.blit(obstacle_img, obstacle.topleft)

    # 진행도 표시 (화면 중앙 상단)
    progress_text = font.render(f"Progress: {int(progress)}%", True, (255, 255, 255))
    text_rect = progress_text.get_rect(center=(screen_width // 2, 50))  # 화면 중앙 상단에 위치
    screen.blit(progress_text, text_rect)
    
    pygame.display.update()

pygame.quit()
