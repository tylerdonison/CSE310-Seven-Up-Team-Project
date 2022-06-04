from constants import *
import pygame

class Space_Station():
  """Class to handle the space station object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """
  
  class Bullet():
    def __init__(self) -> None:
        pass
    def shoot(self):
      pass
    def contact(self):
      pass

  def __init__(self):
    self.image = pygame.image.load(str.join(ASSET_PATH, "/Pictures/Cannon/Turret01.png"))
    pass
  

  #shooting assets
