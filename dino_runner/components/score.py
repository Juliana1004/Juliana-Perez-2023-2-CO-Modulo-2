import pygame

from dino_runner.utils.constants import FONT_STYLE

class Score:
    SCREEN_SCORE = (750,30)
    DEFAULT_SCORE = 0
    def __init__(self):
        self.score = self.DEFAULT_SCORE
        self.font = pygame.font.Font(FONT_STYLE, 25)
        self.text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.SCREEN_SCORE

    def update(self,game):
        self.score_counter(game)
        self.update_score(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect.center)

    def score_counter(self, game):
        self.text = self.font.render(f"HS: {game.winner} | Score:  {self.score}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.SCREEN_SCORE

    def update_score(self,game):
        if game.winner == self.score:
            game.winner +=1 
        self.score += 1
        if self.score % 100 == 0 and game.game_speed < 500:
            game.game_speed += 5

    def death_score(self, screen):
        self.text = self.font.render(f"My score: {self.score}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (600,350)
        screen.blit(self.text, self.text_rect.center)

    def max_score(self, game, screen):
        self.text = self.font.render(f"High score: {game.winner}", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (410,400)
        screen.blit(self.text, self.text_rect.center)

    def reset_score(self):
        self.score = self.DEFAULT_SCORE
      
