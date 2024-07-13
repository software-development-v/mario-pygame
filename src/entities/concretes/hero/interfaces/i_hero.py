from abc import ABC, abstractmethod
from typing import Dict, Optional, Sequence

from src.enums import GameEvent, HeroAction, HeroLevel, HeroState
from src.utils import Camera

from ....abstractions import Element
from ....interfaces import ISprite
from ..managers import CocaBallManager


class IHero(ISprite, ABC):
    @abstractmethod
    def get_coca_ball_manager(self) -> CocaBallManager:
        pass

    @abstractmethod
    def get_pre_level(self) -> Optional[HeroLevel]:
        pass

    @abstractmethod
    def get_hero_level(self) -> HeroLevel:
        pass

    @abstractmethod
    def set_hero_level(self, hero_level: HeroLevel) -> None:
        pass

    @abstractmethod
    def get_hero_state(self) -> HeroState:
        pass

    @abstractmethod
    def set_hero_state(self, hero_state: HeroState) -> None:
        pass

    @abstractmethod
    def get_vel_x(self) -> float:
        pass

    @abstractmethod
    def set_vel_x(self, vel_x: float) -> None:
        pass

    @abstractmethod
    def add_vel_x(self, vel_x: float) -> None:
        pass

    @abstractmethod
    def get_vel_y(self) -> float:
        pass

    @abstractmethod
    def set_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def add_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def get_actions(self) -> Dict[HeroAction, bool]:
        pass

    @abstractmethod
    def set_actions(self, actions: Dict[HeroAction, bool]) -> None:
        pass

    @abstractmethod
    def set_action(self, action: HeroAction, value: bool) -> None:
        pass

    @abstractmethod
    def is_bouncing(self) -> bool:
        pass

    @abstractmethod
    def set_is_bouncing(self, is_bouncing: bool) -> None:
        pass

    @abstractmethod
    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: Sequence[Element],
        enemies: Sequence[ISprite],
        camera: Camera,
    ) -> None:
        pass

    @abstractmethod
    def is_borracho(self) -> bool:
        pass

    @abstractmethod
    def is_invulnerable(self) -> bool:
        pass

    @abstractmethod
    def borracho(self) -> None:
        pass

    @abstractmethod
    def grow(self, level: HeroLevel) -> None:
        pass

    @abstractmethod
    def decrease(self) -> None:
        pass
