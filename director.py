import pygame
import random
from constants import *
from display import Display
from mathematics import Mathematics
from user import User
from space_station import Space_Station
from asteroid import Asteroid
from words import Word
from display import Explosion
from menu import Menu
# from score import Score 
from health import Health
from button import Button
import sys
pygame.init()
display = Display()
user_input = User()
station = Space_Station()
menu = Menu()
# rock = Asteroid()
word = Word()
# score = Score(50)
health = Health()
# math = Mathematics()
class Director():

    def __init__(self):
        self.difficulty = None
        self.run = True
        self.pause = False
        self.guess = None
        self.asteroid_list = []
        self.targets = []
        self.timer = 0
        self.health = Health()
        self.mode = None


    def start_game(self):
        clock = pygame.time.Clock()  
        clock.tick(FPS)
        while self.run:
            self.timer += 1
            display.draw_window()
            pygame.display.update() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                # pause/unpause
                ### Call pause function in menu ###
                        self.pause = True
                        menu.pause_menu()
                        
                    # Checking for a guess
                    else:
                        self.guess = user_input.get_text(event)
                        self.check_guess()
                        self.display_game_update()

    def check_guess(self):
        # Check for bullet colliding with asteroid
        for obj in self.targets:
            if station.check_asteroid_hit(obj):
                # exp = Explosion(obj)
                # exp.update()
                self.targets.remove(obj)
                self.asteroid_list.remove(obj)

        # Check for asteroid colliding with station
        for asteroid in self.asteroid_list[:]:
            if station.space_station_collide(asteroid):
                self.asteroid_list.remove(asteroid)
                self.health.decrement_health()

        # Checking if guess is right
        for asteroid in self.asteroid_list:
            if self.guess == asteroid.enemy_word and 300 - asteroid.y < 300 and asteroid not in self.targets:
                self.targets.append(asteroid)
                station.create_bullet(asteroid)
                self.guess = None
                # score.update_score

        # Adding enemies to screen
        if len(self.asteroid_list) == 0:
        # while len(self.asteroid_list) < 7:
            for i in range(10):
                enemy_word = word.get_word(self.difficulty)
                rock = Asteroid(enemy_word, random.randint(-70, WIDTH - 200), random.randint(-2000, -150), random.randint(0, 2))
                # rock.size_by_word()
                self.asteroid_list.append(rock)

    def display_game_update(self):
        display.draw_window()
        self.health.draw_health()
        # Display typed text
        user_input.display_typed_text()

        for asteroid in self.asteroid_list:
            asteroid.draw_asteroid()
            asteroid.handle_movement()
            
        # Draw and move bullets 
        station.draw_bullet()
        station.handle_bullets()

        game_over = self.health.get_health()
        if game_over <= 0:
            display.game_over()
            loop = True
            MAIN_MENU = Button(image=None, pos=(WIDTH/2, HEIGHT/6 * 4), 
                        text_input="MAIN MENU", font=menu._get_font(50), base_color="#b68f40", hovering_color="Grey")
            
            QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 5), 
                        text_input="QUIT", font=menu._get_font(40), base_color="#d7fcd4", hovering_color="White")
            OPTIONS = (MAIN_MENU, QUIT_BUTTON)

            while loop:
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                pygame.display.update()
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
                            if MAIN_MENU.checkForInput(OPTIONS_MOUSE_POS):
                            # Go back to main function
                                loop = False
                            elif QUIT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                pygame.quit()
                                sys.exit()
            self.run = False


        pygame.display.update()


    def setup_game(self):
        # # Sets variables based on difficulty chosen
        player_choice = menu.draw_window()
        self.difficulty = player_choice[1]
        self.mode = player_choice[0]
        self.health.determine_start_health(self.difficulty)
        self.start_game()
        
# def main():
#   """Directs user to the menu, game loop, etc.
#   """
#   director = Director()
#   director.setup_game()

# if __name__ == "__main__":
#   main()
