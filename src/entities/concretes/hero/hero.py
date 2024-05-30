from typing import Dict, List

from pygame import Surface, time

from src.enums import GameEvent, HeroLevel, HeroState
from src.utils.constants import ANIMATION_INTERVAL, INIT_IMAGE_INDEX, PLAYER_INIT_POS

from ...interfaces import IDrawable


class Hero(IDrawable):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[Surface]]],
    ) -> None:
        self.surfaces = surfaces
        self.hero_level = HeroLevel.NORMAL
        self.hero_state = HeroState.IDLE
        self.current_image_index = INIT_IMAGE_INDEX
        self.animatoin_interval = ANIMATION_INTERVAL
        self.last_update = time.get_ticks()

    def draw(self, screen: Surface) -> None:
        screen.blit(
            self.surfaces[self.hero_level][self.hero_state][
                self.current_image_index
            ],
            PLAYER_INIT_POS,
        )

    def update(self, game_events: Dict[GameEvent, bool]) -> None:
        pass
