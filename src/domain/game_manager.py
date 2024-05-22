from src.domain.level_struct.level_manager import LevelManager


class GameManager:
    def __init__(self, level_manager: LevelManager):
        self._level_manager = level_manager

    def start_game(self) -> None:
        # TODO: Implement this method to start the game
        pass

    def handle_collisions(self) -> None:
        # TODO: Implement this method to handle collisions between game entities
        pass

    def update_game(self) -> None:
        self.handle_collisions()

    def end_game(self) -> None:
        # TODO: Implement this method to end the game
        pass
