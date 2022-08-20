import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size)) # X-Y
        self.image.fill('darkgrey')
        self.rect = self.image.get_rect(topleft = pos)