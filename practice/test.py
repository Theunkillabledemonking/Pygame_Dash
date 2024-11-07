import pygame

# 초기 설정
onblock = False
gravity = 1
vel_y = 0

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 점프 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if onblock or player_rect.bottom >= screen.get_rect().bottom:
                    vel_y = -20  # 점프 속도 설정
                    onblock = False  # 점프했으므로 공중에 있음

    # 중력 및 속도 적용
    vel_y += gravity
    player_rect.y += vel_y

    # 충돌 검사 전 onblock 초기화
    onblock = False

    # 블록과의 충돌 검사
    for i in squares_list:
        if player_rect.colliderect(i):
            if vel_y > 0:  # 캐릭터가 내려가는 중일 때만 처리
                onblock = True
                player_rect.bottom = i.top  # 위치 보정
                vel_y = 0  # 속도 초기화

    # 바닥과의 충돌 검사
    if player_rect.bottom >= screen.get_rect().bottom:
        onblock = True
        player_rect.bottom = screen.get_rect().bottom
        vel_y = 0

    # 화면 그리기
    screen.fill((0, 0, 0))
    # 여기서 플레이어와 블록을 그립니다.
    pygame.draw.rect(screen, (255, 0, 0), player_rect)
    for block in squares_list:
        pygame.draw.rect(screen, (0, 255, 0), block)

    pygame.display.update()
    clock.tick(60)
