from abc import ABC, abstractmethod
from typing import Dict, List

from src.enums import GameEvent, HeroAction, HeroLevel, HeroState
from src.utils import Camera

from ....abstractions import Element
from ....interfaces import ISprite


class IHero(ISprite, ABC):
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
    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: List[Element],
        camera: Camera,
    ) -> None:
        pass
