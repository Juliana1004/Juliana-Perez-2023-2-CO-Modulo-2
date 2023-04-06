import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, DEAD, FONT_STYLE, DEFAULT_TYPE, AROUND
from dino_runner.components.score import Score
from dino_runner.components.menu import Menu
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.dinosaur import Dinosour
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager


class Game:
    X_POS_CLOUD = SCREEN_WIDTH
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.hammer_speed = 50
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.around = AROUND
        self.cloud = CLOUD
        self.x_pos_cloud = self.X_POS_CLOUD
        self.y_pos_cloud = 100
        self.player = Dinosour()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen,"Press any key to start...")
        self.running = False
        self.score = Score()
        self.winner = 0
        self.death_count = 0
        self.power_up_manager = PowerUpManager()


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.score.update(self)       
        self.player.update(user_input, self)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(self.around, (0,0))
        self.draw_background()
        self.befog()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def befog(self):
        image_cloud = self.cloud
        self.screen.blit(image_cloud,(self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -SCREEN_WIDTH:
            self.y_pos_cloud = random.randrange(50,200)
            self.x_pos_cloud = self.X_POS_CLOUD
        self.x_pos_cloud -= self.game_speed


    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height= SCREEN_HEIGHT // 2
        if self.death_count == 0:
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
            self.menu.draw(self.screen, 'Press any key to start')
        else:
            self.screen.blit(DEAD, (half_screen_width - 70, half_screen_height - 220))
            self.menu.draw(self.screen, 'Game Over')
            self.draw_death()
            self.score.death_score(self.screen)
            self.score.max_score(self, self.screen)
        self.menu.update(self)

    def draw_death(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"My Deaths: {self.death_count}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (300,350)
        self.screen.blit(text, text_rect.center)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score.reset_score()
        self.player.reset()
        self.power_up_manager.reset_power_ups()

    def draw_power_up(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks())//1000)
            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.type.capitalize()} enable for {time_to_show} seconds', 500, 50)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE