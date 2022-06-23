import os
import pygame

from words import Word
from constants import *
from asteroid import Asteroid
from health import Health
from score import Score

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
            self.pause = not self.pause
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

# Debugging
def main():
  display = Display()

if __name__ == "__main__":
  main()

