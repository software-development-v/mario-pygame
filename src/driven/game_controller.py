from pygame import QUIT, display, event, quit
from pygame.time import Clock

from src.design.infraestructure import Infrastructure
from src.domain.game_manager import GameManager
from src.utils.constants import INIT_GAME_POINTS


class GameController:
    def __init__(
        self, game_manager: GameManager, infrastructure_game: Infrastructure
    ):
        self.game_manager = game_manager
        self.infrastructure_game = infrastructure_game
        self.points_game = INIT_GAME_POINTS

    def get_points(self) -> int:
        return self.points_game

    def add_points(self, points: int) -> None:
        self.points_game += points

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

    def handle_collisions(self) -> None:
        # TODO: Implement this method to handle collisions between game entities
        pass

    def update(self) -> None:
        self.handle_collisions()

    def draw(self, clock: Clock) -> None:
        self.infrastructure_game.render(clock)
