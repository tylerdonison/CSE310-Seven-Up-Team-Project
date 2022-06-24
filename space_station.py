from constants import *
import os
import pygame
from bullet import Bullet

class Space_Station():
  """Class to handle the space station object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """

  
  def __init__(self):
    self.bullets = []
    self.target = []
    self.mask = self.mask = pygame.mask.from_surface(SPACESTATION)
    self.x = WIDTH/2-(SPACESTATION_SIZE[0]/2) 
    self.y = HEIGHT-(SPACESTATION_SIZE[0]/2)+100



  def shoot(self, x):
    # Creates a bullet with starting coordinates
    bullet = Bullet(x + 10, 600)
    self.bullets.append(bullet)
  

  def draw_bullet(self):
    # Handles drawing more than one bullet on the screen at once
    for bullet in self.bullets:
      bullet.draw()

  def move_bullets(self, obj):
      for bullet in self.bullets:
        bullet.move(-4)
        if bullet.collision(obj):
            # Delete asteroid from list, explosion image
            self.bullets.remove(bullet)
            return obj
        else:
          return None
            

  def space_station_collide(self, obj):
  # Checks if pixels overlap so objects look like they collide
    split = self.x / 6
    offset_left = 0 + split + split
    offset_right = WIDTH - split - split

    if obj.x < 300:
      difference = 300 - obj.x 
      limit = difference * 1.176470 - 10
      if obj.y > HEIGHT - limit:
        return True
    
    if obj.x < 900 and obj.x > 600:
      difference = 300 - obj.x 
      limit = difference / 1.176470 - 10
      if obj.y > HEIGHT - limit:
        return True

    if obj.x >= offset_left and obj.x <= offset_right and obj.y > HEIGHT / 2 - 70:
      return True


###########################################################################
# Add bullet movement to display, where game loops or where enmies are drawn
# space_station.move_bullets(asteroid object)   


  
  

