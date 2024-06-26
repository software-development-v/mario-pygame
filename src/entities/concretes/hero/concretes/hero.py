from typing import Dict, List

from pygame import Rect, Surface

from src.enums import GameEvent, HeroAction, HeroLevel, HeroState
from src.utils import (
    HERO_ANIMATION_INTERVAL,
    HERO_BIG_RECT_X_PERCENT,
    HERO_NORMAL_RECT_X_PERCENT,
    HERO_RECT_Y_PERCENT,
    INIT_VEL_Y,
    Camera,
    Position,
)

from ....abstractions import Element, Sprite
from ..handlers import (
    ActionsHandler,
    CollisionsHandler,
    DamageHandler,
    IActionsHandler,
    ICollisionsHandler,
    IDamageHandler,
    IMovementHandler,
    MovementHandler,
)
from ..interfaces import IHero


class Hero(Sprite, IHero):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[Surface]]],
        position: Position,
    ) -> None:
        self.__surfaces = surfaces
        self.__hero_level = HeroLevel.NORMAL
        self.__hero_state = HeroState.IDLE
        self.__vel_y = INIT_VEL_Y
        self.__actions: Dict[HeroAction, bool] = {
            HeroAction.JUMPING: True,
            HeroAction.RUNNING: False,
            HeroAction.IDLE: False,
        }
        self.__actions_handler: IActionsHandler = ActionsHandler(self)
        self.__movement_handler: IMovementHandler = MovementHandler(self)
        self.__collisions_handler: ICollisionsHandler = CollisionsHandler(self)
        self.__damage_handler: IDamageHandler = DamageHandler(self)

        super().__init__(
            position,
            animation_interval=HERO_ANIMATION_INTERVAL,
            y_rect_percent=HERO_RECT_Y_PERCENT,
            x_rect_percent=self.__hero_level == HeroLevel.NORMAL
            and HERO_NORMAL_RECT_X_PERCENT
            or HERO_BIG_RECT_X_PERCENT,
        )

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__hero_level][self.__hero_state]

    def get_hero_level(self) -> HeroLevel:
        return self.__hero_level

    def set_hero_level(self, hero_level: HeroLevel) -> None:
        self.__hero_level = hero_level

    def get_hero_state(self) -> HeroState:
        return self.__hero_state

    def set_hero_state(self, hero_state: HeroState) -> None:
        self.__hero_state = hero_state

    def get_vel_y(self) -> float:
        return self.__vel_y

    def set_vel_y(self, vel_y: float) -> None:
        self.__vel_y = vel_y

    def add_vel_y(self, vel_y: float) -> None:
        self.__vel_y += vel_y

    def get_actions(self) -> Dict[HeroAction, bool]:
        return self.__actions

    def set_actions(self, actions: Dict[HeroAction, bool]) -> None:
        self.__actions = actions

    def set_action(self, action: HeroAction, value: bool) -> None:
        self.__actions[action] = value

    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: List[Element],
        camera: Camera,
    ) -> None:
        self.__actions_handler.handle_hero_actions(game_events)

        hero_rect: Rect = self.get_rect()
        dx, dy = self.__movement_handler.handle_hero_movements(
            hero_rect, game_events, camera
        )
        dx, dy = self.__collisions_handler.handle_collisions(
            hero_rect, obstacles, dx, dy
        )
        self.add_x_rect(dx)
        self.add_y_rect(dy)
        self.__damage_handler.handle_damage()
