from constants import *
import pygame

<<<<<<< HEAD:cannon.py
class Cannon():
  """Class to handle the cannon object. The cannon will react to the userclass's controls. 
  This class will handle the visuals and the bullet objects.
  """
=======
class Space_Station():
>>>>>>> 912af6c257f7f3c1bf0d155dfde104260da9de6c:space_station.py
  
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