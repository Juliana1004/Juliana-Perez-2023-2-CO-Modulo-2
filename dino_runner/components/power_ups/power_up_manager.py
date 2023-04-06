import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3,5)
        self.when_appears = random.randint(50,70)
        self.count = 0

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.score:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if self.count == 0:
                    game.player.type = SHIELD_TYPE
                else:
                    game.player.type = HAMMER_TYPE
                # Muestra la hora actual
                power_up.star_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_time = power_up.star_time + (self.duration * 1000)

                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50, 70)
        self.count = 0

    def generate_power_up(self):
        self.when_appears += random.randint(200, 300)
        power_up_type = random.randint(0,1)
        print(power_up_type)
        if power_up_type == 0:
            self.count = 0
            power_up = Shield()
            self.power_ups.append(power_up)
        else:
            self.count = 1
            power_up = Hammer()
            self.power_ups.append(power_up)