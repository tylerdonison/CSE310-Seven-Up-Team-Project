import os
import pygame

from words import Word
from constants import *
from asteroid import Asteroid
from user import User
from space_station import Space_Station
import random
import sys

pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game display.
  
  def __init__(self):
    self.run = True
    self.pause = False



  def draw_window(self):
    Timer = 0
    asteroid_list = []
    objects = []
    hit = False
    station = Space_Station()
    user_input = User()
    clock = pygame.time.Clock()
    while self.run:

      # Look for quit and pause events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            # pause/unpause
            self.pause = not self.pause
            
  

      if not self.pause:
        clock.tick(FPS)
        Timer += 1
        
        # if Timer % 60 == 0:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.run = False
              

        #draw background
        WIN.blit(SPACE, (0,0))

        # draw space station
        WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
          
        
        word = Word()
        if len(asteroid_list) == 0:
          for i in range(7):
            enemy_word = word.get_word()
            rock = Asteroid(enemy_word, random.randrange(0, 400), random.randrange(-2000, -50), random.choice(asteroid_images))
            rock.randomize(True)



            # List of asteroids
            asteroid_list.append(rock)



        # Drawing asteroids on screen
        for asteroid in asteroid_list:
          asteroid.draw_asteroid()
          asteroid.handle_movement()



        # Checking for a guess
        guess = user_input.get_text()

        # Checking if guess is right
        for asteroid in asteroid_list:
          if guess == asteroid.enemy_word and asteroid.y > 0:
            objects.append(asteroid)
            station.create_bullet(asteroid)



        station.draw_bullet()
        station.handle_bullets()


        for obj in objects:
          if station.check_asteroid_hit(obj):
            exp = Explosion(obj)
            exp.update()
            objects.remove(obj)
            asteroid_list.remove(obj)


        for asteroid in asteroid_list[:]:
          if station.space_station_collide(asteroid):
            asteroid_list.remove(asteroid)

        # Display typed text
        user_input.display_typed_text()

        
        # asteroid_hit = station.move_bullets(self.object)
        
        # if station.move_bullets == True:
        #   asteroid_list.remove(self.object)
       

          

        pygame.display.update()
    sys.exit()

        
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

