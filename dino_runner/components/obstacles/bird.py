import random


from dino_runner.components.obstacles.obstacle import Obstacle 
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.image = image
        self.type = 0
        self.flight_index = 0
        super().__init__(image, self.type) 
        self.rect.y = random.randrange(50,300)

    def draw(self, screen):
        if self.flight_index > 10:
            self.flight_index = 0
        self.image = BIRD[0] if self.flight_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x,self.rect.y))
        self.flight_index += 1