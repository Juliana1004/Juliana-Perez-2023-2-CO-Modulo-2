import pygame

import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__ (self):
        self.obstacles =[]

    def update(self, game):
        obstacle_type = random.randint(0,2)
        if obstacle_type == 0:
            if len(self.obstacles) == 0:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)
        elif obstacle_type == 1:
            if len(self.obstacles) == 0:
                cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(cactus)
        elif obstacle_type == 2:
            if len(self.obstacles) == 0:
                pajaro = Bird(BIRD)
                self.obstacles.append(pajaro)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)