from constants import *
import os
import pygame
from asteroid import Asteroid

class Space_Station():
  """Class to handle the space station object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """
  
  class Bullet():

    def __init__(self, target):
        self.img = pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Cannon", "Turret01.png"))
        self.target = target
        asteroid = Asteroid(self.target)

    def draw(self):
      # draws the bullet
        WIN.blit(self.img, (self.x, self.y))

    def move(self, vel):
      # moves bullet towards asteroid
        self.y += vel

    def off_screen(self, height):
      # checks if the bullet is off screen
        return not(self.y <= height and self.y >= 0)

    def find_target(self):
      # finds which asteroid to shoot at
      pass


    def contact(self):
      pass


  
  

  #shooting assets
