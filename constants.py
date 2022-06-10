import os
import pygame
pygame.font.init()
pygame.mixer.init()

DEFAULT_PATH = os.path
ASSET_PATH = os.path.join("Assets")

LETTER_SIZE = 5
ASTEROID_VEL = 5
BORDER_DISTANCE = 10
WIDTH = 900
HEIGHT = 500

pygame.font.init()
pygame.mixer.init()

#This is a file that contains default values that can be called repeatedly.
#This file will also allow for easy testing of speeds, etc.

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Colors, maybe we need to agree on a theme.
#         RED   GREEN BLUE
WHITE =  (255,  255,  255)
BLACK =  (0,    0,    0)
RED =    (255,  0,    0)
GREEN =  (0,    255,  0) 
BLUE =   (0,    0,    255)
YELLOW = (255,  255,  0)
TEAL =   (0,    255,  255)
PURPLE = (255,  0,    255)
BROWN =  (255,  255,  0)

MAIN_FONT = pygame.font.SysFont("comicsans", 100) #can change, just showing that fonts can be made via this, first variable is the system's font, second is the size

FPS = 60
ASTEROID_VEL = 5
BORDER_DISTANCE = 10 #to spawn asteroids in the borders of the game
LETTER_SIZE = 5 #for use in asteroids

ASTEROID_HIT = pygame.USEREVENT + 1 #for collision between bullet and successful type?
CANNON_HIT = pygame.USEREVENT + 2   #for collision between asteriod and cannon
DEFAULT_PATH = os.path
ASSET_PATH = os.path.join("Assets")

SPACESTATION_SIZE = (WIDTH- (WIDTH/10), WIDTH- (WIDTH/10))

TIMER_COUNT = 0
ROCK_FONT = pygame.font.SysFont('comicsans', 40)
