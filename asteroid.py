import random
from mathematics import Mathematics
from words import Word
from user import User
from constants import *

class Asteroid():

    def __init__(self, problem):
        image_1 = pygame.image.load(ASSET_PATH.join("name of picture file 1"))
        image_2 = pygame.image.load(ASSET_PATH.join("name of picture file 2"))
        image_3 = pygame.image.load(ASSET_PATH.join("name of picture file 3"))
        self.images =[image_1, image_2, image_3]
        self.used_image = "" #This allows a pygame call of WIN.blit(Asteroid.usedimage, (asteroid.x, asteroid.y))
        self.size = (100, 100)
        self.rotation = 0
        self.y = 0
        self.x = 0
        self.problem = problem
        self.user = User()

    def randomize(self, randomize_size=False):
        if randomize_size:
            random_size = random.randint(100,1000)
            self.size = (random_size, random_size)
        else:
            self.size = self.size_by_word()
        self.rotation = random.randint(0,361)
        self.used_image = pygame.transform.rotate(pygame.transform.scale(self.images[random.randint(0,3)], self.size), self.rotation)
        left_limit = BORDER_DISTANCE
        right_limit = (WIDTH - self.size - BORDER_DISTANCE)
        self.x = random.randint(left_limit, right_limit)
        
    def size_by_word(self):
        length = len(self.problem)
        self.size = length * LETTER_SIZE
    
    def handle_movement(self):
        self.x += ASTEROID_VEL
    
    def handle_collision(self):
        if self.problem.check_solution(self.user.typed_text()):
            del self
    
        
