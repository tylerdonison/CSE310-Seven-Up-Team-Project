from constants import *
import pygame

class Space_Station():
  
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
