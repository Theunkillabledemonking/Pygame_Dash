import pygame, sys, os
from game import WIDTH, HEIGHT, TILE_SIZE, Game
pygame.init()
# WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def apply(self, target_rect):
        return pygame.Rect(target_rect.x + self.rect.x, target_rect.y + self.rect.y, target_rect.width, target_rect.height)
    
    def update(self, target_rect):
        x = -target_rect.centerx + WIDTH//2
        y = -target_rect.centery + HEIGHT//2
        x = min(x, 0) # 카메라 왼쪽 경계 제한
        x = max(x, WIDTH-self.width) # 카메라 오른쪽 경계 제한
        y = min(y, 0) # 카메라 위쪽 경계 제한
        y = max(y, HEIGHT-self.height) # 카메라 아래쪽 경계 제한
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(center = pos)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 6
        if keys[pygame.K_a]:
            self.rect.x -= 6
        if keys[pygame.K_s]:
            self.rect.y += 6
        if keys[pygame.K_w]:
            self.rect.y -= 6
            
class GameCamera(Game):
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        super().__init__(os.path.join(BASE_DIR, "map.txt"))
        self.player = pygame.sprite.GroupSingle(Player((WIDTH//2, HEIGHT//2)))
        self.map_width = len(self.map[0])*TILE_SIZE
        self.map_height = len(self.map)*TILE_SIZE
        self.camera = Camera(self.map_width, self.map_height)
        
    def update(self):
        self.player.update()
        self.camera.update(self.player.sprite.rect)
        
    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.image, self.camera.apply(block.rect))
            surface.blit(self.player.sprite.image, self.camera.apply(block.rect))
    
game = GameCamera()

if __name__ == '__main__':  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill('lightblue')
        game.update()
        game.draw(screen)
        clock.tick(FPS)
        pygame.display.update()