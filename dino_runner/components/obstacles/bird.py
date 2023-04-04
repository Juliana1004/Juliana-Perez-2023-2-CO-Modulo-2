import random
import pygame


from dino_runner.components.obstacles.obstacle import Obstacle 
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0,1)
        self.flying = True
        self.step_index = 0
        super().__init__(image, self.type)
        self.y_pos = random.randrange(50,300,62)
        self.rect.y = self.y_pos
        self.rect.x = SCREEN_WIDTH
        print(self.rect.y)

    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x,self.rect.y))
        self.step_index += 1