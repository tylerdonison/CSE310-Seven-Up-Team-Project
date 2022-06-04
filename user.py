#currently overseen by Morgan
#class to handle the user inputs in game.

import pygame
from words import Word
import os
# from asciimatics.event import KeyboardEvent
from constants import *
from words import Word


class User():
  
  def __init__(self, screen):
    self.input = ''
    self.screen = screen
    self.word = Word()


  def check_text(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        self.input += pygame.key.name(event.key)

        #Check if word matches and return word if true 
        if self.word.word.startswith(self.input):
          if self.word.word == input:
            return self.input
          else:
            return False
    
  def display_typed_text(self):
    # Get the text typed by player and display it on screen
    font = pygame.font.Font('comicsans', 100)
    text = font.render(self.input, 1, (255, 255, 255))
    text_rect = text.get_rect(WIDTH/3)
    self.screen.blitz(text, text_rect)
    pygame.display.update()


  def sounds(self):
    missile_sound = pygame.mixer.Sound(os.path.join('sounds','Shoot_01.wav'))
    missile_sound.set_volume(1)

  

  
  #handle if word or solution is right, delete asteroid if true, maybe have indicator for failed word/solution
  
