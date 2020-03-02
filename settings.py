# game options and settings

import pygame as pg

# Constants
TITLE = 'The Broken Link'
WIDTH   = 1400
HEIGHT  = 1000
FPS     = 30
pg.mixer.init()


# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 80, WIDTH , 40)]


# Colors
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
AAA     = (131, 211, 16)
TREE    = (115, 14, 1)
ROAD    = (152, 153, 155)
block_color = (53,115,255)
BRIGHTCOLOR = (245, 66, 218)
