from typing import List

from pygame.surface import Surface

from src.domain.level_struct.entity.entity import Entity
from src.domain.level_struct.entity.obstacle import Obstacle
from src.domain.level_struct.entity.platform import Platform
from src.domain.level_struct.entity.powerup import PowerUp
from src.domain.level_struct.timer.timer import Timer


class Level:
    def __init__(
        self,
        obstacles: List[Obstacle],
        platforms: List[Platform],
        entities: List[Entity],
        power_ups: List[PowerUp],
        background_sprite: Surface,
        timer: Timer,
    ):
        self.obstacles = obstacles
        self.platforms = platforms
        self.entities = entities
        self.power_ups = power_ups
        self.background_sprite = background_sprite
        self.timer = timer

    def check_game_over(self) -> None:
        # TODO: Implement this method to check if the game is over
        pass

    def check_game_win(self) -> None:
        # TODO: Implement this method to check if the game is won
        pass
