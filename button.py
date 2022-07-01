# Button Class for the Main Menu
# Thanks to https://github.com/baraltech/Menu-System-PyGame

import os
import pygame
from constants import ASSET_PATH, MUSIC


class Button():
	select_button_sound = os.path.join(ASSET_PATH, "Sounds", "Menu_Navigate_03.wav")
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, options_size=False):
		# Scale the image to the appropriate size to accomodate font size
		self.image = image
		if not options_size:
			try:
				self.image = pygame.transform.scale(image, (350, 75))
			except TypeError:
				# Pass: no image was given
				pass
		else:
			self.image = pygame.transform.scale(image, (200, 40))
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.played_sound = False

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
			if not self.played_sound:
				MUSIC.load(Button.select_button_sound)
				MUSIC.play()
				self.played_sound = True
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.played_sound = False