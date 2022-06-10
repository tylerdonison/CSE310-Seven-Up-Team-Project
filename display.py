from turtle import width
import pygame
import os

from words import Word
pygame.font.init()
pygame.mixer.init()
from constants import *
from asteroid import Asteroid

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game display.
  
  def __init__(self):
    self.draw_window()
  
  def draw_window(self):
    Timer = 0
    asteroid_list = []
    clock = pygame.time.Clock()
    run = True
    while run:
      clock.tick(FPS)
      Timer += 1
      print(Timer)
      if Timer % 60 == 0:
        test_list = ["boy", "girl", "dog", "apple", "horse"]
        word = Word(test_list)
        word.setup_sentence()
        rock = Asteroid(word)
        rock.randomize(True)
        asteroid_list.append(rock)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
          pygame.quit()

        #cannon hit event
        #correct typed event

      #handle win?

      #draw background
      SPACE = pygame.transform.scale(pygame.image.load(
        os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
        "Assets", "Pictures", "Backgrounds", "Background.PNG")), 
        (WIDTH, HEIGHT))
      WIN.blit(SPACE, (0,0))

      SPACESTATION = pygame.transform.scale(pygame.image.load(
        os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
        "Assets", "Pictures", "Space-Station", "Space Station.png")), 
        (SPACESTATION_SIZE))
      WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
      for rock in asteroid_list:
        WIN.blit(rock.used_image, (rock.x, rock.y))
        
        word_text = ROCK_FONT.render(rock.problem.problem, 1, WHITE)
        WIN.blit(word_text, rock.center)
        rock.handle_movement()
        
      pygame.display.update()

def main():
  display = Display()
  Display.draw_window()

main()

