# 플레이어의 움직임 및 관련 로직을 관리
import pygame
from setting import screen_height, image_path
import os

class Player:
    def __init__(self, x, y):
        """플레이어 객체 초기화"""
        self.orginal_image = pygame.image.load(os.path.join(image_path, "Cube.png"))  # Cube.png 이미지 로드
        self.orginal_image = pygame.transform.scale(self.orginal_image, (50, 50))  # 이미지 크기 조정
        self.image = self.orginal_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0  # 중력 값 초기화
        self.rotation_angle = 0  # 회전 각도 초기화
        self.is_jumping = False  # 점프 상태 플래그
        self.rotation_steps = 0  # 회전 단계 초기화

    def handle_movement(self):
        """플레이어의 움직임 및 물리 엔진 처리"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and not self.is_jumping :
            self.is_jumping = True
            self.gravity = -7  # 점프 시 중력 설정
            self.rotation_steps = 30  # 30번 회전 (6도씩 회전하여 180도 회전)
            

        # 중력 적용
        self.rect.y += self.gravity
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height  # 바닥에 닿으면 위치 고정
            self.gravity = 0  # 중력 초기화
            self.is_jumping = False  # 바닥에 닿으면 점프 상태 해제
        else:
            self.gravity += 0.4  # 중력 가속도

        # 회전 처리
        if self.is_jumping:
            if self.rotation_steps > 0 :
                self.rotation_angle -= 6 # 시계 방향으로 6도씩 회전
                self.rotation_steps -= 1
            else:
                self.is_jumping = False

    def get_rotated_image(self):
        """현재 회전된 이미지와 그 위치를 반환"""
        # 이미지 회전
        rotated_image = pygame.transform.rotate(self.orginal_image, self.rotation_angle)
        
        # 회전된 이미지의 중심점 보정
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        
        # 바닥에 닿았을 때 중심점 보정
        # if self.rect.bottom >= screen_height:
        #     rotated_rect.bottom = screen_height  # 바닥에 닿았을 때 위치 조정
        
        return rotated_image, rotated_rect
