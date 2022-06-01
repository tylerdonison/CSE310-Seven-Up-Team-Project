
<<<<<<< HEAD

def main():
  """main file to direct user to the menu, game loop, etc."""
=======
import constants
from asteroid import Asteroid
from problem import Problem

def main():
  """Directs user to the menu, game loop, etc.
  """
>>>>>>> 0eec001... my understanding
  #go to menu
  print(constants.ASSET_PATH)
  problem = Problem()
  Asteroid(problem)

if __name__ == "__main__":
  main()
