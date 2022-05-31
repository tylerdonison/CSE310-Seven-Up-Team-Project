#Currently overseen by Tyler
#Class to oversee the behavior of asteroids
#Typing solutions to be done elsewhere.

from game_math import Math
from words import Word

from constants import *
import pygame
import random

class Asteroid():

    # Normal asteroid
    __asteroid_1_1 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/a10005.png"))
    __asteroid_1_2 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/a10010.png"))
    __asteroid_1_3 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/a10015.png"))

    # Red asteroid
    __asteroid_2_1 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/b30005.png"))
    __asteroid_2_2 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/b30010.png"))
    __asteroid_2_3 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/b30015.png"))

    # Yellow asteroid
    __asteroid_3_1 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/c40005.png"))
    __asteroid_3_2 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/c40010.png"))
    __asteroid_3_3 = pygame.image.load(ASSET_PATH.join("/Pictures/Asteroids/large/c40015.png"))

    __images = [
            [__asteroid_1_1, __asteroid_1_2, __asteroid_1_3],
            [__asteroid_2_1, __asteroid_2_2, __asteroid_2_3],
            [__asteroid_3_1, __asteroid_3_2, __asteroid_3_3]
            ]

    def __init__(self, problem):
        # Pick an asteroid texture among the three provided.
        self.images = Asteroid.__images[random.randint(0,2)]
        self.used_image = "" #This allows a pygame call of WIN.blit(Asteroid.usedimage, (Asteroid.x, Asteroid.y))
        self.image_stepper = 0
        self.size = (100, 100)
        # self.rotation = 0

        # Top of the screen
        self.y = 0
        self.x = 0
        self.problem = problem

    def randomize(self, randomize_size=False):
        if randomize_size:
            random_size = random.randint(100,1000)
            self.size = (random_size, random_size)
        else:
            self._size_by_word()
        # self.rotation = random.randint(0,361)
        # self.used_image = pygame.transform.rotate(pygame.transform.scale(self.images[random.randint(0,3)], self.size), self.rotation)
        left_limit = BORDER_DISTANCE
        right_limit = (WIDTH - self.size - BORDER_DISTANCE)
        self.x = random.randint(left_limit, right_limit)
    
    def animate(self):
        """Make the asteroid rotate.
        """
        self.image_stepper += 1
        self.used_image = self.images[self.image_stepper % len(Asteroid.__images)]
        
    def _size_by_word(self):
        length = len(self.problem)
        size = length * LETTER_SIZE
        self.size(size, size)
    
    def handle_movement(self):
        self.x += ASTEROID_VEL
    
    #handle collision with player
