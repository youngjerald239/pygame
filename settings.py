level_map = [
'                            ',     #Rows for game level
'                            ',
'                            ',
' XX    XXX            XX    ',     #Each "X" represents a column
' XX                         ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size   # Level map * Tile size
print(screen_height)