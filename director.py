import pygame
import random
from constants import *
from display import Display
from user import User
from space_station import Space_Station
from asteroid import Asteroid
from words import Word
from display import Explosion
# from score import Score 
# from health import Health


display = Display()
user_input = User()
station = Space_Station()
# rock = Asteroid()
word = Word()
# score = Score(50)
# health = Health()

class Director():

    def __init__(self):
        self.difficulty = None
        self.run = True
        self.pause = False
        self.guess = None
        self.asteroid_list = []
        self.targets = []
        self.timer = 0

    def start_game(self):
        display.draw_window
        clock = pygame.time.Clock()  
        clock.tick(FPS)
        while self.run:
            self.timer += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                # pause/unpause
                ### Call pause function in menu ###
                        self.pause = True
                    # Checking for a guess
                    else:
                        self.guess = user_input.get_text(event)

            # Display typed text


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
                    # health.decrement_health()

            # Checking if guess is right
            for asteroid in self.asteroid_list:
                if self.guess == asteroid.enemy_word and asteroid.y > 0 and asteroid not in self.targets:
                    self.targets.append(asteroid)
                    station.create_bullet(asteroid)
                    self.guess = None
                    # score.update_score

            # Adding enemies to screen
            while len(self.asteroid_list) < 7:
                enemy_word = word.get_word()
                rock = Asteroid(enemy_word, random.randrange(0, 400), random.randrange(-2000, -50), random.choice(asteroid_images))
                rock.randomize(True)
                self.asteroid_list.append(rock)

    
            display.draw_window()
            user_input.display_typed_text()

            for asteroid in self.asteroid_list:
                asteroid.draw_asteroid()
                asteroid.handle_movement()
                
            # Draw and move bullets 
            station.draw_bullet()
            station.handle_bullets()
            pygame.display.update()
        
        
