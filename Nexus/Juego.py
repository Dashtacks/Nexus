import pygame
from pygame.locals import *

# Tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

surf = pygame.Surface((50, 50))
surf.fill(RED)
rect = surf.get_rect()

# Dibuja el cuadrado en el centro    
surf_center = (SCREEN_WIDTH/2 - rect.width/2, SCREEN_HEIGHT/2 - rect.height/2)
screen.blit(surf, surf_center)
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False