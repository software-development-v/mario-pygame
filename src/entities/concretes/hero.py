from typing import Dict, List

from pygame import Surface, time

from src.enums import GameEvent, HeroLevel, HeroState
from src.utils.classes import Position
from src.utils.constants import ANIMATION_INTERVAL, INIT_IMAGE_INDEX

from ..interfaces import IDrawable


class Hero(IDrawable):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[List[Surface]]]],
        position: Position,
    ) -> None:
        self.surfaces = surfaces
        self.hero_level = HeroLevel.NORMAL
        self.hero_state = HeroState.IDLE
        self.hero_phase = 0
        self.current_image_index = INIT_IMAGE_INDEX
        self.animatoin_interval = ANIMATION_INTERVAL
        self.last_update = time.get_ticks()
        self.position = position

    def draw(self, screen: Surface) -> None:
        screen.blit(
            self.surfaces[self.hero_level][self.hero_state][self.hero_phase][
                self.current_image_index
            ],
            self.position.to_tuple(),
        )

    def update(self, game_events: Dict[GameEvent, bool]) -> None:
        pass
