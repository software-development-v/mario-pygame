import pygame

from utils.constants import FPS, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, WHITE_COLOR
from utils.text_utils import get_centered_message


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self) -> None:
        while self.running:
            self.update()
            self.events()
            self.draw()

    def update(self) -> None:
        return

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

    def draw(self) -> None:
        self.clock.tick(FPS)

        self.screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message("Hello, World")
        self.screen.blit(text, text_rect)

        pygame.display.update()
