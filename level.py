from re import X
import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size  # row is 0-10
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
            #    print(f'{row_index},{col_index}:{cell}') for exact X value and row numbers
            # print(row_index) To view row data and number
            # print(row) To view just the rows

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)