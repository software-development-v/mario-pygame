from src.utils.constants import INIT_GAME_POINTS


class ScoreManager:
    def __init__(
        self
    ):
        self.points_game = INIT_GAME_POINTS

    def get_points(self) -> int:
        return self.points_game

    def add_points(self, points: int) -> None:
        self.points_game += points
