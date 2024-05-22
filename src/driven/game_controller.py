from pygame import QUIT, display, event, quit
from pygame.time import Clock

from src.design.infraestructure import Infrastructure
from src.domain.game_manager import GameManager


class GameController:
    def __init__(
        self, game_manager: GameManager, infrastructure_game: Infrastructure
    ):
        self.game_manager = game_manager
        self.infrastructure_game = infrastructure_game

    def init_game(self, running: bool, clock: Clock) -> None:
        while running:
            self.events()
            self.update()
            self.draw(clock)

    def events(self) -> None:
        for e in event.get():
            if e.type == QUIT:
                display.quit()
                quit()
                exit()

    def handle_input(self) -> None:
        # TODO: Implement this method handle input that processes user input
        pass

    def update(self) -> None:
        self.handle_input()

    def draw(self, clock: Clock) -> None:
        self.infrastructure_game.render(clock)
