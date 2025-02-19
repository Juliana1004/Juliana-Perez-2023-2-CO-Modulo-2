import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2
    def __init__(self, screen, message):
        screen.fill((171, 178, 185))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width - 150, self.half_screen_height)

    def update(self,game):
        self.handle_events_on_menu(game)
        pygame.display.update()

    def draw(self, screen, message, x = half_screen_width, y = half_screen_height):
        self.text = self.font.render(message, True, (253, 254, 254))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x,y)
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((171, 178, 185))

    def handle_events_on_menu(self,game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()