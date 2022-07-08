import os
import pygame

# from words import Word
from constants import *
# from asteroid import Asteroid
# from user import User
# from space_station import Space_Station
# import random
# import sys

# WIN.set_caption("Seven-Up Space")

class Display():
  #class to handle game WIN.
  
  def __init__(self):
    pass



  def draw_window(self):
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.run = False
          
    #draw background
    WIN.blit(SPACE, (0,0))

    # draw space station
    WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
      

  def game_over(self):
    game_over_text = FONT.render(f"GAME OVER", True, (200,200,200))
    score_text = FONT.render(f"TOTAL SCORE: X", True, (200,200,200))
    # zombie_count_text = pygame.font.SysFont.render(f"ZOMBIE COUNT: {zombie_count}", True, (200,200,200))
    #Drawing elements
    WIN.fill((0, 0, 0))
    WIN.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/9))
    WIN.blit(score_text, (WIDTH/2 - (score_text.get_width()/2), (HEIGHT/4)))
    # WIN.blit(zombie_count_text, (WIDTH/2 - (zombie_count_text.get_width()/2), (HEIGHT/2 + zombie_count_text.get_height() * 2.5)))
    


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
  WIN.draw_window()

if __name__ == "__main__":
  main()

