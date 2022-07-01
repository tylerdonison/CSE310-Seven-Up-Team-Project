import random
from mathematics import Mathematics
from constants import *

class Asteroid():

    def __init__(self, enemy_word, x, y, used_image):
        self.used_image = used_image
        self.size = (100, 100)
        self.rotation = random.randint(0,361)
        self.x = x
        self.y = y
        self.center = (-200,-200)
        self.enemy_word = enemy_word
        self.mask = pygame.mask.from_surface(self.used_image)


    def randomize(self, randomize_size=False):
        if randomize_size:
            random_size = random.randint(100,200)
            self.size = (random_size, random_size)
        else:
            self.size = self.size_by_word()
        self.rotation = random.randint(0,361)

        
    def size_by_word(self):
        length = len(self.enemy_word)
        self.size = length * LETTER_SIZE


    def handle_movement(self):
        self.y += ASTEROID_VEL
        self.rotation += 1
        if self.rotation > 360:
            self.rotation = 0
        self.center = (self.size[0]/2+self.x + 5, self.size[1]/2+self.y)

    
    def draw_asteroid(self):
        WIN.blit(self.used_image, (self.x, self.y))          
        word_text = ROCK_FONT.render(self.enemy_word, 1, WHITE)
        WIN.blit(word_text, self.center)