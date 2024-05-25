from typing import Tuple
from src.data.background.background import IBackground
from src.data.levels import Levels


class LevelData:
    level: Levels
    time = 0
    score = 0
    total_score = 0
    background: IBackground
    background_music: str
    player_start_position: Tuple[int, int]


    def __init__(
        self,
        level: Levels,
        time: int,
        background: IBackground,
        background_music: str,
        player_start_position: Tuple[int, int]
    ) -> None:
        self.level = level
        self.time = time
        self.background = background
        self.background_music = background_music
        self.player_start_position = player_start_position


    def get_background(self) -> IBackground:
        return self.background

