import pygame
import os

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1920
screen_height = 1080 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Geometry Dash")

# 배경음악 파일 로드
background_music = pygame.mixer.music.load("C:\\Users\\USER\\Desktop\\Geometry Dash\\image\\stereoMadness.wav")

# 배경음악 무한 반복 재생 시작
pygame.mixer.music.play(-1)

# FPS
clock = pygame.time.Clock()

# 이미지 경로 설정
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, "images")

# 배경 이미지 설정
background = pygame.image.load("C:\\Users\\USER\\Desktop\\Geometry Dash\\image\\Background-GeometricBlue.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# 플레이어 캐릭터 설정 (고정된 위치)
player = pygame.Rect((screen_width // 2) - 50, screen_height - 150, 50, 50)
player_img = pygame.image.load('C:\\Users\\USER\\Desktop\\Geometry Dash\\image\\Cube.png')
player_img = pygame.transform.scale(player_img, (50, 50))

# 장애물 설정
obstacle = pygame.Rect(screen_width, screen_height - 30 , 120, 30)
obstacle_img = pygame.image.load("C:\\Users\\USER\\Desktop\\Geometry Dash\\image\\spikes.png")
obstacle_img = pygame.transform.scale(obstacle_img, (100, 30))

# 게임 속도 및 중력 설정
game_speed = 7
y_vel = 0
gravity = 1

# 게임 루프
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 캐릭터는 고정, 점프 처리만
    keys = pygame.key.get_pressed()
    player.top += y_vel
    y_vel += gravity
    if player.bottom >= screen_height:
        y_vel = 0
        if keys[pygame.K_SPACE]:
            y_vel = -20 
    
    # 장애물 이동
    obstacle.left -= game_speed

    # 장애물이 화면을 벗어나면 재설정
    if obstacle.right < 0:
        obstacle.left = screen_width
    
    # 충돌 처리
    if player.colliderect(obstacle):
        print("Collision detected!")
        running = False  # 충돌 시 게임 종료
    
    # 화면 그리기
    screen.blit(background, (0, 0))
    screen.blit(player_img, player)
    screen.blit(obstacle_img, obstacle.topleft)
    
    pygame.display.update()

pygame.quit()
