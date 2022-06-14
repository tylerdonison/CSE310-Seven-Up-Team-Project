import random
from mathematics import Mathematics
from words import Word
from user import User
from constants import *

class Asteroid():

    def __init__(self):#, problem):
        image_1 = pygame.image.load(os.path.join("Assets", "Pictures", "Asteroids", "Asteroid_1.png"))
        image_2 = pygame.image.load(os.path.join("Assets", "Pictures", "Asteroids", "Asteroid_2.png"))
        image_3 = pygame.image.load(os.path.join("Assets", "Pictures", "Asteroids", "Asteroid_3.png"))
        self.images =[image_1, image_2, image_3]
        self.used_image = "" #This allows a pygame call of WIN.blit(Asteroid.usedimage, (asteroid.x, asteroid.y))
        self.size = (100, 100)
        self.rotation = 0
        self.y = -200
        self.x = 0
        self.center = (-200,-200)
  #      self.problem = problem
        #self.user = User()

    def randomize(self, randomize_size=False):
        if randomize_size:
            random_size = random.randint(100,200)
            self.size = (random_size, random_size)
        else:
            self.size = self.size_by_word()
        self.rotation = random.randint(0,361)
        self.used_image = pygame.transform.rotate(pygame.transform.scale(self.images[random.randint(0,2)], self.size), self.rotation)
        left_limit = BORDER_DISTANCE
        right_limit = (WIDTH - (BORDER_DISTANCE*10))
        self.x = random.randint(left_limit, right_limit)
        
    """def size_by_word(self):
        length = len(self.problem)
        self.size = length * LETTER_SIZE
    """

    def handle_movement(self):
        self.y += ASTEROID_VEL
        if self.rotation < 360:
            self.rotation +=1
        else:
            self.rotation = 0
        self.used_image = pygame.transform.rotate(pygame.transform.scale(self.images[random.randint(0,2)], self.size), self.rotation)
        self.center = (self.size[0]/2+self.x, self.size[1]/2+self.y)
    
    def handle_collision(self):
        if self.problem.check_solution(self.user.typed_text()):
            del self
    
        
