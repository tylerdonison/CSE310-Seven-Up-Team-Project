# Main Menu
# Thanks to https://www.youtube.com/watch?v=GMBqjxcKogA
# https://github.com/baraltech/Menu-System-PyGame

import sys
import os
import pygame
from constants import * 
from button import Button
from display import Display

class Menu(Display):
    BG = pygame.transform.scale(pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Backgrounds", "nebula.jpg")), (WIDTH,HEIGHT))

    def __init__(self):
        # Set the default for the difficulty as easy
        # self.difficulty = "EASY"
        self.choices = []
        # Draw the main menu
        super().__init__()
        

    def _get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(os.path.join(ASSET_PATH, "font.ttf"), size)

    def play(self):

        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

      #      WIN.fill("black")

            PLAY_TEXT = self._get_font(45).render("This is the PLAY WIN.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            WIN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self._get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.draw_window()

            pygame.display.update()
        
    def options(self):
        WIN.blit(Menu.BG, (0, 0))

        OPTIONS_TEXT = self._get_font(45).render("DIFFICULTY", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)


        OPTIONS_BACK = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4.5), 
                            text_input="BACK", font=self._get_font(50), base_color="Grey", hovering_color="White")

        EASY = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5, HEIGHT/6 * 2.5), 
                            text_input="EASY", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        MEDIUM = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 2.5, HEIGHT/6 * 2.5), 
                            text_input="MEDIUM", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        HARD = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 4, HEIGHT/6 * 2.5), 
                            text_input="HARD", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)
        
        OPTIONS = (OPTIONS_BACK, EASY, MEDIUM, HARD)

        EASY = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5, HEIGHT/6 * 2.5), 
                            text_input="EASY", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        MEDIUM = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 2.5, HEIGHT/6 * 2.5), 
                            text_input="MEDIUM", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        HARD = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 4, HEIGHT/6 * 2.5), 
                            text_input="HARD", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)
        
        OPTIONS = (OPTIONS_BACK, EASY, MEDIUM, HARD)

        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # See if any of the options are being hovered over.
            # If so, change and update color
            for option in OPTIONS:
                option.changeColor(OPTIONS_MOUSE_POS)
                option.update(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for option in OPTIONS:
                        if option.text_input == "BACK" and option.checkForInput(OPTIONS_MOUSE_POS):
                            # Go back to main function
                            self.draw_window()
                        elif option.checkForInput(OPTIONS_MOUSE_POS):
                            # Update the difficulty
                            self.choices.append(option.text_input.lower())
                            MUSIC.load(Button.select_button_sound)
                            MUSIC.play()
                            return 



            pygame.display.update()

    def math_or_typing(self):
        # Player chooses which mode to play
        WIN.blit(Menu.BG, (0, 0))

        OPTIONS_TEXT = self._get_font(45).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))
        WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)


        OPTIONS_BACK = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4.5), 
                            text_input="BACK", font=self._get_font(50), base_color="Grey", hovering_color="White")

        TYPING = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 1.5, HEIGHT/6 * 2.5), 
                            text_input="TYPING", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        MATH = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/5 * 3.5, HEIGHT/6 * 2.5), 
                            text_input="MATH", font=self._get_font(30), base_color="#d7fcd4", hovering_color="White", options_size=True)

        OPTIONS = (OPTIONS_BACK, TYPING, MATH)

        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            # See if any of the options are being hovered over.
            # If so, change and update color
            for option in OPTIONS:
                option.changeColor(OPTIONS_MOUSE_POS)
                option.update(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for option in OPTIONS:
                        if option.text_input == "BACK" and option.checkForInput(OPTIONS_MOUSE_POS):
                            # Go back to main function
                            self.draw_window()
                        elif option.checkForInput(OPTIONS_MOUSE_POS):
                            # Update the difficulty
                            self.choices.append(option.text_input.lower())
                            MUSIC.load(Button.select_button_sound)
                            MUSIC.play()
                            self.options() 
                            return self.choices       
            pygame.display.update()


    # This is the main menu
    def draw_window(self):
        WIN.blit(Menu.BG, (0, 0))

        MENU_TEXT = self._get_font(50).render("GALACTIC TYPER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/6))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Play Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 3), 
                            text_input="PLAY", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Options Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 3.75), 
        #                     text_input="OPTIONS", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 4), 
                            text_input="QUIT", font=self._get_font(40), base_color="#d7fcd4", hovering_color="White")
        BUTTONS = (PLAY_BUTTON, QUIT_BUTTON) 
        
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
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # self.play()
                        pygame.display.update()
                        return self.math_or_typing()
                        
                    # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #     # Clear screen
                    #     pygame.display.update()
                    #     self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

