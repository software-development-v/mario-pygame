from typing import List

from src.domain.level_struct.entity.obstacle import Obstacle
from src.domain.level_struct.entity.platform import Platform
from src.domain.level_struct.entity.powerup import PowerUp
from src.domain.level_struct.timer.timer import Timer
from src.domain.level_struct.entity.entity import Entity

class Level:
    def __init__(self, obstacles: List[Obstacle], platforms: List[Platform],
                 entities: List[Entity], power_ups: List[PowerUp],
                 background_sprite: str, timer: Timer):
        # Initialize the level with obstacles, platforms, entities, power-ups,
        # background sprite, and timer
        self.obstacles = obstacles
        self.platforms = platforms
        self.entities = entities
        self.power_ups = power_ups
        self.background_sprite = background_sprite
        self.timer = timer

    def check_game_over(self) -> None:
        # Check conditions for game over
        # Implement logic to determine if the game is over
        # For example:
        # if player.is_dead() or self.timer.is_expired():
        #     print("Game over!")
        pass

    def check_game_win(self) -> None:
        # Check conditions for game win
        # Implement logic to determine if the game is won
        # For example:
        # if all_enemies_defeated() and self.timer.is_not_expired():
        #     print("You win!")
        pass
