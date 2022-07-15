import pygame
import random
from constants import *
from display import Display
from mathematics import Mathematics
from user import User
from space_station import Space_Station
from asteroid import Asteroid
from words import Word
from menu import Menu
from health import Health
from button import Button
from score import Score
import sys
pygame.init()
display = Display()
user_input = User()
station = Space_Station()
menu = Menu()
word = Word()


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
        self.score = Score()
        self.mode = None


    def start_game(self):
        """The main game loop"""
        display.draw_window
        clock = pygame.time.Clock()  
        clock.tick(FPS)
        while self.run:
            self.timer += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    # Checking for a guess                   
                    self.guess = user_input.get_text(event)
                    # Checking for a pause
                    self.pause = user_input.check_pause(event)

            # If player pauses game, pause menu is shown
            if self.pause == True:
                self.pause = menu.pause_menu()


            # Check for bullet colliding with asteroid
            for asteroid in self.targets:
                if station.check_bullet_hit(asteroid):
                    MUSIC.load("Assets/Sounds/Explosion_02.wav")
                    MUSIC.play()
                    self.targets.remove(asteroid)
                    # To trigger explotion animation
                    asteroid.destroyed = True

            # Check for asteroid colliding with station
            for asteroid in self.asteroid_list[:]:
                if station.space_station_collide(asteroid):
                    MUSIC.load("Assets/Sounds/Explosion_03.wav")
                    MUSIC.play()
                    self.asteroid_list.remove(asteroid)
                    self.health.decrement_health()

            # Checking if guess is right
            for asteroid in self.asteroid_list:
                if self.guess == asteroid.answer and 300 - asteroid.y < 300 and asteroid not in self.targets:
                    MUSIC.load("Assets/Sounds/Shoot_01.wav")
                    MUSIC.play()
                    self.targets.append(asteroid)
                    station.create_bullet(asteroid)
                    self.guess = None
                    self.score.update_score(len(asteroid.enemy_word) * 10)

            # Adding enemies to screen
            if len(self.asteroid_list) == 0:
                for _ in range(10):
                    if self.mode == "typing":
                        enemy_word = word.get_word(self.difficulty)
                        rock = Asteroid(enemy_word, random.randint(-40, WIDTH - 200), random.randint(-2500, -150), random.randint(0, 2), enemy_word)
                        rock.size_by_word()
                    else:
                        math = Mathematics(self.difficulty)
                        math.math_setup()
                        enemy_word = math.get_problem()
                        answer = math.get_answer()
                        rock = Asteroid(enemy_word, random.randint(-70, WIDTH - 200), random.randint(-2000, -150), random.randint(0, 2), answer)

                    # rock.size_by_word()
                    self.asteroid_list.append(rock)                      

            display.draw_window()
            display.draw_pause_option()
            self.health.draw_health()
            self.score.draw_score()


            # Display typed text
            user_input.display_typed_text()


            for asteroid in self.asteroid_list:
                if asteroid.disappear:
                    self.asteroid_list.remove(asteroid)
                else:
                    asteroid.draw_asteroid()
                    asteroid.handle_movement()
                
            # Draw and move bullets 
            station.draw_bullet()
            station.handle_bullets()

            game_over = self.health.get_health()
            if game_over <= 0:
                """When the game ends player will be taked to a game over screen where they are shown
                    their score and have the option to quit or go back to the main menu"""
                # MUSIC.load("Assets/Sounds/Jingle_Lose_00.wav")
                # MUSIC.play()
                display.game_over(self.score.get_score())
                loop = True
                MAIN_MENU = Button(image=None, pos=(WIDTH/2, HEIGHT/6 * 4), 
                            text_input="MAIN MENU", font=menu._get_font(50), base_color="#b68f40", hovering_color="Grey")
                
                QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(ASSET_PATH, "Quit Rect.png")), pos=(WIDTH/2, HEIGHT/6 * 5), 
                            text_input="QUIT", font=menu._get_font(40), base_color="#d7fcd4", hovering_color="White")
                OPTIONS = (MAIN_MENU, QUIT_BUTTON)

                while loop:
                    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
                    pygame.display.update()
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
        # Sets variables based on difficulty chosen
        player_choice = menu.draw_window()
        self.difficulty = player_choice[1]
        self.mode = player_choice[0]
        self.health.determine_start_health(self.difficulty)
        self.start_game()


