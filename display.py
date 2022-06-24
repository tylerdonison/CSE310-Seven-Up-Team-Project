import os
import pygame
import sys

from words import Word
from constants import *
from asteroid import Asteroid
from health import Health
from score import Score
from button import Button
from menu import Menu

pygame.display.set_caption("Seven-Up Space")

class Display():
  #class to handle game display.
  
  def __init__(self):
    self.run = True
    self.pause = False
    self.draw_window()
  
  def draw_window(self):
    Timer = 0
    asteroid_list = []
    clock = pygame.time.Clock()

    # Draw the startup cast before entering game loop  

    SPACE = pygame.transform.scale(pygame.image.load(
          os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
          ASSET_PATH, "Pictures", "Backgrounds", "Background.PNG")), 
          (WIDTH * 1.1, HEIGHT))

    # Shift the image to the left so that it can fit the whole screen
    WIN.blit(SPACE, (-50,0))

    SPACESTATION = pygame.transform.scale(pygame.image.load(
          os.path.join(#"CSE310-Seven-Up-Team-Project-main", 
          ASSET_PATH, "Pictures", "Space-Station", "Space Station.png")), 
          (SPACESTATION_SIZE))
          
    WIN.blit(SPACESTATION, (WIDTH/2-(SPACESTATION_SIZE[0]/2), HEIGHT-(SPACESTATION_SIZE[0]/2)+100))

    # Draw the score and the health
    score = Score()
    health = Health(10)

    while self.run:

      # Look for quit and pause events
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            # pause/unpause
            self.pause = not self.pause #True
            ####### CHERYL ADD ######## 
            # show pause menu
            pause_menu()
        if event.type == pygame.QUIT:
          self.run = False
          pygame.quit()

      if not self.pause:
        clock.tick(FPS)
        Timer += 1
        print(Timer)
        if Timer % 60 == 0:
          test_list = ["boy", "girl", "dog", "apple", "horse"]
          word = Word(test_list)
          word.setup_sentence()
          # rock = Asteroid(word)
          rock = Asteroid()
          rock.randomize(True)
          asteroid_list.append(rock)

        

          #cannon hit event
          #correct typed event

        #handle win?

        
        for rock in asteroid_list:
          WIN.blit(rock.used_image, (rock.x, rock.y))
          
          word_text = ROCK_FONT.render(rock.problem.problem, 1, WHITE)
          WIN.blit(word_text, rock.center)
          rock.handle_movement()
          
        pygame.display.update()

###### CHERYL ADD ####### 
# PAUSE MENU
def pause_menu(self):
  WIN.blit(Display.BG, (0, 0))

  MENU_TEXT = self._get_font(50).render("PAUSED", True, "#b68f40")
  MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))

  CONTINUE_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 2.5), 
                      text_input="CONTINUE", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
  RESTART_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Options Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 3.75), 
                      text_input="RESTART", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
  QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 5), 
                      text_input="QUIT", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
  BUTTONS = (CONTINUE_BUTTON, RESTART_BUTTON, QUIT_BUTTON) 
  
  while True:
      MENU_MOUSE_POS = pygame.mouse.get_pos()
      WIN.blit(MENU_TEXT, MENU_RECT)

      for button in BUTTONS:
          button.changeColor(MENU_MOUSE_POS)
          button.update(WIN)
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                  self.pause = False
              if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                  # Clear screen
                  pygame.display.update()
                  Menu()
              if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                  pygame.quit()
                  sys.exit()

      pygame.display.update()

# Debugging
def main():
  display = Display()

if __name__ == "__main__":
  main()

