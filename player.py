import pygame

def handle_player_movement(player, y_vel, gravity):
    """플레이어의 움직임을 처리"""
    keys = pygame.key.get_pressed()
    player.top += y_vel
    y_vel += gravity
    if player.bottom >= 600: #Screen_height를 직접 참조하지 않고 설정된 높이를 사용
        y_vel = 0
        if keys[pygame.K_SPACE]:
            y_vel = -18
    return y_vel