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
    self.object = ''



  def draw_window(self):
    Timer = 0
    asteroid_list = []
    station = Space_Station()
    user_input = User()
    clock = pygame.time.Clock()
    while self.run:

      # Look for quit and pause events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
          pygame.quit()
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
            # self.run = False
            pygame.quit()
              

        #draw background
        WIN.blit(SPACE, (0,0))

        # draw space station
        WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
          
        
        word = Word()
        if len(asteroid_list) == 0:
          for i in range(7):
            enemy_word = word.get_word()
            rock = Asteroid(enemy_word, random.randrange(0, 400), random.randrange(-1500, -50), random.choice(asteroid_images))
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
          if asteroid.enemy_word == guess:
            self.object = asteroid
            station.shoot(asteroid.x)

            # station.move_bullets(asteroid)
            # asteroid_list.remove(asteroid)


        for asteroid in asteroid_list[:]:
          station.move_bullets(self.object)
          station.draw_bullet()
          if station.space_station_collide(asteroid):
            asteroid_list.remove(asteroid)

        # Display typed text
        user_input.display_typed_text()

        
        # asteroid_hit = station.move_bullets(self.object)
        
        if station.move_bullets == True:
          asteroid_list.remove(self.object)
          self.object = ''

          

        pygame.display.update()

        




# Debugging
def main():
  display = Display()
  display.draw_window()

if __name__ == "__main__":
  main()

