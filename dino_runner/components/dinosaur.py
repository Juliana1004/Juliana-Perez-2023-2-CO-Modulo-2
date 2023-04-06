import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, HAMMER

RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
DUCK_IMAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}

class Dinosour(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    X_POS_HAMMER = -40
    Y_POS_HAMMER = 310
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False
        self.has_power_up = False
        self.power_up_time = 0
        self.image_hammer = HAMMER
        self.hammer_rect = self.image_hammer.get_rect()
        self.hammer_rect.x = self.X_POS_HAMMER
        self.hammer_rect.y = self.Y_POS_HAMMER
        self.hammer = False
        self.hammer_tries = 0

    def update(self, user_input, game):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif (user_input[pygame.K_a] and self.type == HAMMER_TYPE) and not self.dino_jump:
            self.launch_hammer()
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_duck= False
            self.dino_run = True

        if self.hammer and self.hammer_tries == 1:
            self.move_hammer(game)

        if self.step_index > 9:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
        if self.hammer and self.hammer_tries == 1:
            self.draw_hammer(screen)

    def run(self):
        self.image = RUN_IMAGE [self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMAGE[self.type]
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.8
        
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCK_IMAGE [self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = 340
        self.step_index += 1

    def reset(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.type = DEFAULT_TYPE
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck= False
        self.reset_hammer()

    def launch_hammer(self):
        self.has_power_up = False
        self.type = DEFAULT_TYPE
        self.hammer = True
        self.hammer_tries += 1

    def draw_hammer(self, screen):
        screen.blit(self.image_hammer, (self.hammer_rect.x, self.hammer_rect.y))

    def move_hammer(self, game):
        self.hammer_rect.x += game.hammer_speed

    def reset_hammer(self):
        self.hammer_rect.x = self.X_POS_HAMMER
        self.hammer_rect.y = self.Y_POS_HAMMER
        self.hammer = False
        self.hammer_tries = 0





