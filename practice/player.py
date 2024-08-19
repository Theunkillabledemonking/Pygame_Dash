import pygame 
from untils import load_image
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite): # 플레이어 캐릭터 클래스
    def __init__(self, pos, width, height, img_path):
        super().__init__()
        self.image = load_image(img_path, (width, height)) # 플레이어 이미지 로드
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = vec(0, 0)
        self.gravity = 0.8
        self.pos = vec(pos)
        self.initial_jump = -11
        self.speed = 5
        self.on_ground = True
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.pos.y += self.direction.y
        self.rect.y = self.pos.y
    
    def update(self):
        self.direction.x = self.speed
        keys = pygame.key.get_pressed() # 키보드 입력 처리
        if keys[pygame.K_SPACE] and self.on_ground:
            self.direction.y = self.initial_jump
            self.on_ground = False