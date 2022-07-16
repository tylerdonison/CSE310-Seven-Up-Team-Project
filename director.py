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
from database import Database
pygame.init()
display = Display()
user_input = User()
station = Space_Station()
menu = Menu()
word = Word()
data = Database()
score = Score()

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
        self.player_score = score.get_score()

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
                if self.guess == asteroid.answer and 275 - asteroid.y < 275 and asteroid not in self.targets:
                    MUSIC.load("Assets/Sounds/Shoot_01.wav")
                    MUSIC.play()
                    self.targets.append(asteroid)
                    station.create_bullet(asteroid)
                    self.guess = None
                    score.update_score(len(asteroid.enemy_word) * 10)

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
            score.draw_score()


            # Display typed text
            user_input.display_typed_text("game")


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
                final_score = self.player_score
                choice = self.game_over_screen()
                if choice =="main":

                    self.run = False
   

            pygame.display.update()

        return True

    def game_over_screen(self):
        """When the game ends player will be taked to a game over screen where they can save their score
         and have the option to quit or go back to the main menu"""
        # MUSIC.load("Assets/Sounds/Jingle_Lose_00.wav")
        # MUSIC.play()
        display.game_over(self.player_score)
        loop = True
        clock = pygame.time.Clock() 

        ### Input box ###
        user_text = ''
        # create rectangle
        input_rect = pygame.Rect(WIDTH/2 + 40, HEIGHT/2 - 10, 200, 45)
        color_active = (102,102,102)
        color_passive = (198, 198, 198)
        color = color_passive
        active = False
        name = False
        saved = False

        SCORES = Button(image=None, pos=(WIDTH/2, HEIGHT/6 * 4), 
                    text_input="HIGH SCORES", font=menu._get_font(30), base_color="#b68f40", hovering_color="Grey")
        
        MAIN_MENU = Button(image=None, pos=(WIDTH/2, HEIGHT/6 * 5), 
                    text_input="MAIN MENU", font=menu._get_font(40), base_color="#b68f40", hovering_color="White")
        OPTIONS = (SCORES, MAIN_MENU)

        while loop:
            display.game_over(self.player_score)
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            for option in OPTIONS:
                option.changeColor(OPTIONS_MOUSE_POS)
                option.update(WIN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MAIN_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    # Go back to main function
                        self.play_again()
                    elif SCORES.checkForInput(OPTIONS_MOUSE_POS):
                        return self.after_game()

                    elif input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if event.type == pygame.KEYDOWN:
                # Check for backspace
                    if event.key == pygame.K_BACKSPACE:  
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]   

                    elif event.key == pygame.K_RETURN:
                        data.save_data(user_text, self.player_score)
                        user_text = ''  
                        saved = True
                    else:
                        user_text += event.unicode

            
            if active:
                color = color_active
            else:
                color = color_passive
          
            if name:
                data.save_data(name, self.player_score)


            if saved:
                save = pygame.font.SysFont('Arial', 20).render("Saved!", True, (255, 255, 255))
                WIN.blit(save, (WIDTH - 200, input_rect.y+5))
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(WIN, color,(WIDTH/2 + 40, HEIGHT/2 - 10, 200, 45))
        
            text_surface =FONT.render(user_text, True, (255, 255, 255))
            
            # render at position stated in arguments
            WIN.blit(text_surface, (input_rect.x+5, input_rect.y))
            
            # render input name text
            label = pygame.font.SysFont('Arial', 30).render("To save score, enter name:", True, (255, 255, 255))
            WIN.blit(label, (WIDTH/6 + 10, input_rect.y))

            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width()+10)
            
            pygame.display.update()
            clock.tick(FPS)
        

    def after_game(self):
        """Screen for showing high scores"""
        BG = pygame.transform.scale(pygame.image.load(os.path.join(ASSET_PATH, "Pictures", "Backgrounds", "nebula.jpg")), (WIDTH,HEIGHT))
        WIN.blit(BG, (0, 0))
        data.load_data()
 
        MENU_TEXT = pygame.font.SysFont('Arial', 55).render("HIGH SCORES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/8))

        MAIN_MENU = Button(image=None, pos=(WIDTH/2, HEIGHT/6 * 5), 
                    text_input="MAIN MENU", font=menu._get_font(40), base_color="#d7fcd4", hovering_color="White")
        BUTTONS = [MAIN_MENU]

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            WIN.blit(MENU_TEXT, MENU_RECT)
            pygame.display.update() 
            for button in BUTTONS:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)
            top_scores = data.get_data()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MAIN_MENU.checkForInput(MENU_MOUSE_POS):
                        self.play_again()
            
            if len(top_scores) >= 3:
                name_label = FONT.render(top_scores[0][0], 1, WHITE)
                WIN.blit(name_label, (275, 150))
                score_label = FONT.render(top_scores[0][1], 1, WHITE)
                WIN.blit(score_label, (600, 150))

                name_label1 = FONT.render(top_scores[1][0], 1, WHITE)
                WIN.blit(name_label1, (275, 200))
                score_label1 = FONT.render(top_scores[1][1], 1, WHITE)
                WIN.blit(score_label1, (600, 200))

                name_label2 = FONT.render(top_scores[2][0], 1, WHITE)
                WIN.blit(name_label2, (275, 250))
                score_label2 = FONT.render(top_scores[2][1], 1, WHITE)
                WIN.blit(score_label2, (600, 250))

            elif len(top_scores) == 2:
                name_label = FONT.render(top_scores[0][0], 1, WHITE)
                WIN.blit(name_label, (275, 150))
                score_label = FONT.render(top_scores[0][1], 1, WHITE)
                WIN.blit(score_label, (600, 150))

                name_label1 = FONT.render(top_scores[1][0], 1, WHITE)
                WIN.blit(name_label1, (275, 200))
                score_label1 = FONT.render(top_scores[1][1], 1, WHITE)
                WIN.blit(score_label1, (600, 200))

            elif len(top_scores) == 1:
                name_label = FONT.render(top_scores[0][0], 1, WHITE)
                WIN.blit(name_label, (275, 150))
                score_label = FONT.render(top_scores[0][1], 1, WHITE)
                WIN.blit(score_label, (600, 150))

            else:
                label = pygame.font.SysFont('Arial', 50).render("NO SCORES YET", 1, WHITE)
                WIN.blit(label, (WIDTH/2 - label.get_width() * .5, HEIGHT/3))

    def play_again(self):
        """If user chooses to return to menu after game they will directed to a new instance of the game"""
        new = Director()
        new.setup_game()


    def setup_game(self):
        # Sets variables based on difficulty chosen
        player_choice = menu.draw_window()
        self.difficulty = player_choice[1]
        self.mode = player_choice[0]
        self.health.determine_start_health(self.difficulty)
        self.start_game()


# def main():
#   """Directs user to the menu, game loop, etc.
#   """
#   director = Director()
#   director.game_over_screen()


# if __name__ == "__main__":
#   main()
