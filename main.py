import pygame, sys
from settings import *
from level import Level


#Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
 ##test_tile = pygame.sprite.Group(Tile((100,100),200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()
    # test_tile.draw(screen)        
    # draw all elements
    # update all
    pygame.display.update()
    clock.tick(60)