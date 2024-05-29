from typing import Dict

from pygame import Surface

from src.entities import Element, IEntity
from src.enums import Level, World
from src.utils import Position

from .background import IBackground


class LevelData:

    def __init__(
        self,
        world: World,
        level: Level,
        time: int,
        background: IBackground,
        background_music: str,
        player_start_position: Position,
        enemies: Dict[Position, IEntity],
        elements: Dict[Position, Element],
        power_ups: Dict[Position, IEntity],
    ) -> None:

        self.world: World = world
        self.level: Level = level
        self.time: int = time
        self.background: IBackground = background
        self.background_music: str = background_music
        self.player_start_position: Position = player_start_position
        self.enemies: Dict[Position, IEntity] = enemies
        self.elements: Dict[Position, Element] = elements
        self.power_ups: Dict[Position, IEntity] = power_ups

    def get_background(self) -> Surface:
        return self.background.get_background()
