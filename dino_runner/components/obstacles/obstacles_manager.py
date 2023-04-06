import pygame

import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE

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
        else:
            if len(self.obstacles) == 0:
                bird = Bird(BIRD)
                self.obstacles.append(bird)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)
                    
            if game.player.hammer_rect.colliderect(obstacle.rect):
                self.obstacles.remove(obstacle)
                game.player.reset_hammer()


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []