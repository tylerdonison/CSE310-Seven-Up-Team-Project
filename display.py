import os
import pygame

# from words import Word
from constants import *
# from asteroid import Asteroid
# from user import User
# from space_station import Space_Station
# import random
# import sys

pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game display.
  
  def __init__(self):
    pass



  def draw_window(self):
    Timer = 0
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.run = False
          
    #draw background
    WIN.blit(SPACE, (0,0))

    # draw space station
    WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
      
    # pygame.display.update()

        
  # def asteroid_explosion(self, obj):
  #   frame_rate = 50
  #   image = explosion_anim[0]
  #   center = obj.center
  #   rect = image.rect(center)
  #   frame = 0
  #   last_update = pygame.time.get_ticks()
  #   now = pygame.time.get_ticks()


  #   if now - last_update > frame_rate:
  #       last_update = now
  #       frame += 1
  #       if frame == len(explosion_anim):
  #           return
  #       else:
  #           center = center
  #           image = explosion_anim[frame]
  #           rect = image.get_rect()
            
class Explosion():
    def __init__(self, obj):
        self.obj = obj
        self.size = (100,100)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = obj.center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                return
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Debugging
def main():
  display = Display()
  display.draw_window()

if __name__ == "__main__":
  main()

