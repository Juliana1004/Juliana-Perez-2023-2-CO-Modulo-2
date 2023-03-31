import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING

class Dinosour(Sprite):
    def __init__(self):
        self.image_1 = RUNNING[0]
        self.image_2 = RUNNING[1]
        self.dino_rect = self.image_1.get_rect()
        self.dino_rect_2 = self.image_2.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.dino_run = True

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image_1, (self.dino_rect.x, self.dino_rect.y))
                
