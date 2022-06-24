#currently overseen by Morgan
#class to handle the user inputs in game.


import pygame
import os
from constants import *


class User():
  # Class to keep track of user inputs 

  def __init__(self):
    self.input = ''


  def get_text(self):
    # Record letters pressed
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        # Deletes letter after backspace 
        if event.key == pygame.K_BACKSPACE:
          if self.input == '':
            return
          else:
            input_list = list(self.input)
            del input_list[-1]
            self.input = ''.join(input_list)

        # Check if space bar or entered was pressed, if so then check guess
        elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
          guess = self.input
          self.input = ''
          return guess
          
        # Add letters to word being typed
        else:
          self.input += event.unicode
          
    
  def display_typed_text(self):
    # Get the text typed by player and display it on screen
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render(self.input, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH/2, HEIGHT-66)
    WIN.blit(text, text_rect)


      

  def sounds(self):
    missile_sound = pygame.mixer.Sound(os.path.join(ASSET_PATH, 'Sounds','Shoot_01.wav'))
    missile_sound.set_volume(1)

  

  