import random
from mathematics import Mathematics
from words import Word
from user import User
from constants import *

class Asteroid():
    """This class is responsible for creating, moving, and destroying asteroids. It will randomly generate an asteroid image, give it a random size, 
    and continually rotate it. If the user's answer equals the solution to the problem on the asteroid, it will delete itself.
    """
    def __init__(self, problem):
        image_1 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_1.png"))
        image_2 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_2.png"))
        image_3 = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Asteroids", "Asteroid_3.png"))
        self.images = [image_1, image_2, image_3]
        self.used_image = "" #This allows a pygame call of WIN.blit(Asteroid.usedimage, (asteroid.x, asteroid.y))
        self.size = (100, 100)
        self.rotation = 0
        self.y = -200
        self.x = 0
        self.center = (-200,-200)
        self.problem = problem
        #self.user = User()

    def randomize(self, randomize_size=False):
        #This method is responsible for setting up the random values of the asteroid, inclusing size, initial rotation, asteroid image, and position
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
        
    def size_by_word(self):
        #This method is responsible for making asteroid's size match the given word. The idea is to have the word not clip out of the asteroid
        length = len(self.problem)
        self.size = length * LETTER_SIZE
    
    def handle_movement(self):
        #This method handles moving the asteroid toward the player and rotating it to make it look like it has an animation
        self.y += ASTEROID_VEL
        if self.rotation < 360:
            self.rotation +=1
        else:
            self.rotation = 0
        self.used_image = pygame.transform.rotate(pygame.transform.scale(self.images[random.randint(0,2)], self.size), self.rotation)
        self.center = (self.size[0]/2+self.x, self.size[1]/2+self.y)
    
    def handle_collision(self):
        #This method is responsible for deleting the asteroid in the event that the player types the correct solution.
        if self.problem.check_solution(self.user.typed_text()):
            del self
    
        
