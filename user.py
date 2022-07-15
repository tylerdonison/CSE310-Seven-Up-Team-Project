#currently overseen by Morgan
#class to handle the user inputs in game.


import pygame
import os
from constants import *
from menu import Menu


class User():
  # Class to keep track of user inputs 

  def __init__(self):
    self.input = ''


  def get_text(self, event):
    """Record letters pressed"""
    if event.key == pygame.K_BACKSPACE:
      if self.input == '':
        return
      else:
        input_list = list(self.input)
        del input_list[-1]
        self.input = ''.join(input_list)

    # Check if space bar or entered was pressed, if so then check guess
    elif event.key == pygame.K_RETURN:
      guess = self.input
      self.input = ''
      return guess
    
    # Add letters to word being typed
    else:
      self.input += event.unicode
    
  def display_typed_text(self, type):
    """Get the text typed by player and display it on screen"""
    if type == "game":
      font = pygame.font.SysFont('comicsans', 50)
      text = font.render(self.input, True, WHITE)
      text_rect = text.get_rect()
      text_rect.center = (WIDTH/2, HEIGHT-66)
      WIN.blit(text, text_rect)

    else:
      font = pygame.font.SysFont('comicsans', 50)
      text = font.render(self.input, True, WHITE)
      text_rect = text.get_rect()
      text_rect.center = (WIDTH/2, HEIGHT/2)
      WIN.blit(text, text_rect)

  def check_pause(self, event):
    if event.key == pygame.K_SPACE:
      return True
    else:
      return False
      


  