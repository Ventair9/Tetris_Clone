import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Tetris_Clone")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pygame.display.update()
        clock.tick(60)


"""def keys():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:

    if keys[pygame.K_RIGHT]:

    if keys[pygame.K_UP]:

    if keys[pygame.K_DOWN]:"""

