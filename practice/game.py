import pygame, sys, os
from untils import *
from player import Player

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
TILE_SIZE = 34
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "image")

class Block(pygame.sprite.Sprite): # 맵의 블록을 나타내는 클래스
    def __init__(self, pos, width, height, img_path):
        super().__init__()
        self.image = load_image(img_path, (width, height)) # 블록 이미지 로드
        self.rect = self.image.get_rect(topleft = pos)

class Game:
    def __init__(self, map_path):
        from camera import Camera # 카메라 클래스 불러오기
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.map = self.read_file(map_path)
        self.map_width = len(self.map[0])*TILE_SIZE
        self.map_height = len(self.map)*TILE_SIZE
        self.camera = Camera(self.map_width, self.map_height)

        self.load_map()
        
    def read_file(self, path):
        file = ''
        with open(path, 'r') as f:
            file = f.read().splitlines() # 맵 파일을 읽어서 리스트로 반환
        return file
    
    def load_map(self):
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == 'B':
                    self.blocks.add(Block((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('image','block.png')))
                elif char == 'P':
                    self.player.add(Player((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('image','Cube.png')))
    
    def horizontal_movement(self):
        player = self.player.sprite
        player.pos.x += player.direction.x
        player.rect.x = player.pos.x
        for block in self.blocks:
            if block.rect.colliderect(player.rect):
                player.rect.right = block.rect.left
                player.pos.x = player.rect.x
                
    def vertical_movement(self):
        player = self.player.sprite
        player.apply_gravity()
        for block in self.blocks:
            if block.rect.colliderect(player.rect):
                if player.direction.y < 0 : # 위로 이동할 때 충돌
                    player.rect.top = block.rect.bottom
                    player.pos.y = player.rect.y
                    player.direction.y = 0
                if player.direction.y > 0 : # 아래로 충돌할 때 충돌
                    player.on_ground = True       
                    player.rect.bottom = block.rect.top
                    player.pos.y = player.rect.y
                    player.direction.y = 0
                    
        if player.on_ground and player.direction.y < 0 or player.direction.y > 0:
            player.on_ground = False
                    
    def update(self):
        self.horizontal_movement()                   
        self.vertical_movement()
        self.player.update()
        self.camera.update(self.player.sprite.rect)
    
    def draw(self, surface):
        for block in self.blocks:
            surface.blit(block.image, self.camera.apply(block.rect))
        surface.blit(self.player.sprite.image, self.camera.apply(self.player.sprite.rect))

# def draw_grid(surface):
#     for y in range(TILE_SIZE, WIDTH, TILE_SIZE):
#         pygame.draw.line(surface, 'red', (y, 0), (y, HEIGHT))
        
#     for x in range(TILE_SIZE, HEIGHT, TILE_SIZE):
#         pygame.draw.line(surface, 'blue', (0, x), (WIDTH, x))

if __name__ == '__main__':
    game = Game(os.path.join(BASE_DIR, 'map.txt'))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('lightblue')
        game.update()
        game.draw(screen)
        # draw_grid(screen)
        clock.tick(FPS)
        pygame.display.update()
        