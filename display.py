from turtle import width
import pygame
import os
pygame.font.init()
pygame.mixer.init()
from constants import *
import asteroid

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game display.
  
  
  # def __init__():
  #   pass
  
  def draw_window():
    asteroid_list = []
    clock = pygame.time.Clock()
    run = True
    while run:
      clock.tick(FPS)
      # TIMER_COUNT += 1

      # if TIMER_COUNT % 600 == 0:
      #   rock = asteroid()
      #   rock.randomize()
      #   asteroid_list.append(rock)

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
      "Assets", "Pictures", "Backgrounds", "Background.png")), 
      (WIDTH, HEIGHT))
  WIN.blit(SPACE, (0,0))

  SPACESTATION = pygame.transform.scale(pygame.image.load(
    os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
    "Assets", "Pictures", "Space-Station", "Space Station.png")), 
    (SPACESTATION_SIZE))
  WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))
    # for rock in asteroid_list:
    #   rock.handle_movement()
  
  pygame.display.update()

def main():
  display = Display()
  Display.draw_window()

main()
