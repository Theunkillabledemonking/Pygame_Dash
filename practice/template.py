import pygame, sys, os
from untils import *

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite): # 2차원 이미지
    def __init__(self, pos, width, height, img_path):
        self.image = load_image(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        
block = Block((0, 0), 34, 34, os.path.join('image','block.png'))
block2 = Block((34, 0), 34, 34, os.path.join('image','block.png'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightblue')
    screen.blit(block.image, block.rect)
    
    screen.blit(block2.image, block2.rect)
    clock.tick(FPS)
    pygame.display.update()