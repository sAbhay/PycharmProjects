import pygame
from pygame.locals import *

running = True

size = (500, 500)

pygame.init()

flags = DOUBLEBUF
screen = pygame.display.set_mode((size[0], size[1]), flags)
screen.set_alpha(None)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 250, 250))
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, 50, 50))
    pygame.display.update()

pygame.quit()