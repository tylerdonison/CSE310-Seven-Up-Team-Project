from constants import *
import pygame

class Cannon():
  """Class to handle the cannon object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """
  
  def __init__(self):
    self.image = pygame.image.load(ASSET_PATH, "/Pictures/Cannon/Turret01.png")
    pass
  
  #shooting logic
  #shooting assets
  #handle bullets
