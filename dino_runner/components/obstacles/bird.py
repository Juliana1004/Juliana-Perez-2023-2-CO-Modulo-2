import pygame

from dino_runner.components.obstacles.obstacle import Obstacle 
from dino_runner.utils.constants import BIRD


class Bird:
    def __init__(self):
        self.image =
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325