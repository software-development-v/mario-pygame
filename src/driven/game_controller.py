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

    def load_game(self) -> None:
        # TODO: Implement this method so it loads the game
        pass

    def handle_collisions(self) -> None:
        # TODO: Implement this method to handle collisions between game entities
        pass

    def update(self) -> None:
        # TODO: Implement this method to update the game
        self.handle_collisions()
