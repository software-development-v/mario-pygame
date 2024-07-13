from typing import Dict, List, Optional, Sequence

from pygame import Rect, Surface, time

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
from ....interfaces import ISprite
from ..handlers import (
    ActionsHandler,
    CheckPointHandler,
    CollisionsHandler,
    DamageHandler,
    DeadHandler,
    IActionsHandler,
    ICollisionsHandler,
    IDamageHandler,
    IMovementHandler,
    JumpHandler,
    MovementHandler,
    WinHandler,
)
from ..interfaces import IHero
from ..managers import CocaBallManager


class Hero(Sprite, IHero):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[Surface]]],
        position: Position,
        check_point: Optional[Position] = None,
    ) -> None:
        self.__surfaces = surfaces
        self.__hero_level = HeroLevel.NORMAL
        self.__hero_state = HeroState.IDLE
        self.__vel_y = INIT_VEL_Y
        self.__vel_x = 0
        self.__actions: Dict[HeroAction, bool] = {
            HeroAction.JUMPING: True,
            HeroAction.RUNNING: False,
            HeroAction.IDLE: False,
            HeroAction.WIN: False,
            HeroAction.DEAD: False,
        }
        self.__actions_handler: IActionsHandler = ActionsHandler(self)
        self.__movement_handler: IMovementHandler = MovementHandler(self)
        self.__collisions_handler: ICollisionsHandler = CollisionsHandler(self)
        self.__damage_handler: IDamageHandler = DamageHandler(self)
        self.__win_handler = WinHandler(self)
        self.__dead_handler = DeadHandler(self)
        self.__check_point_handler = CheckPointHandler(self)
        self.__jump_handler = JumpHandler(self)
        self.__collided_win: bool = False
        self.__is_bouncing: bool = False
        self.__levels = [HeroLevel.NORMAL, HeroLevel.BIG, HeroLevel.COCA]
        self.__is_invulnerable: bool = False
        self.__invulnerable_time: Optional[int] = None
        self.__prev_level: Optional[HeroLevel] = None
        self.__borracho_time: Optional[int] = None
        self.__coca_ball_manager = CocaBallManager()

        super().__init__(
            position,
            animation_interval=HERO_ANIMATION_INTERVAL,
            y_rect_percent=HERO_RECT_Y_PERCENT,
            x_rect_percent=self.__hero_level == HeroLevel.NORMAL
            and HERO_NORMAL_RECT_X_PERCENT
            or HERO_BIG_RECT_X_PERCENT,
            check_point=check_point,
            alpha=True,
        )

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__hero_level][self.__hero_state]

    def get_pre_level(self) -> Optional[HeroLevel]:
        return self.__prev_level

    def get_coca_ball_manager(self) -> CocaBallManager:
        return self.__coca_ball_manager

    def get_hero_level(self) -> HeroLevel:
        return self.__hero_level

    def set_hero_level(self, hero_level: HeroLevel) -> None:
        self.__hero_level = hero_level

    def get_hero_state(self) -> HeroState:
        return self.__hero_state

    def set_hero_state(self, hero_state: HeroState) -> None:
        self.__hero_state = hero_state

    def get_vel_x(self) -> float:
        return self.__vel_x

    def set_vel_x(self, vel_x: float) -> None:
        self.__vel_x = vel_x

    def add_vel_x(self, vel_x: float) -> None:
        self.__vel_x += vel_x

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

    def get_collided_win(self) -> bool:
        return self.__collided_win

    def set_collided_win(self, value: bool) -> None:
        self.__collided_win = value

    def is_bouncing(self) -> bool:
        return self.__is_bouncing

    def set_is_bouncing(self, is_bouncing: bool) -> None:
        self.__is_bouncing = is_bouncing

    def reset(self) -> None:
        self.set_hero_level(HeroLevel.NORMAL)
        self.set_hero_state(HeroState.IDLE)
        self.set_vel_y(INIT_VEL_Y)
        self.set_actions(
            {
                HeroAction.JUMPING: True,
                HeroAction.RUNNING: False,
                HeroAction.IDLE: False,
                HeroAction.WIN: False,
                HeroAction.DEAD: False,
            }
        )
        self.set_is_bouncing(False)
        self.set_face_right(True)
        self.__is_invulnerable = False
        self.__invulnerable_time = None
        self.__borracho_time = None
        self.__prev_level = None
        super().reset()

    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: Sequence[Element],
        enemies: Sequence[ISprite],
        camera: Camera,
    ) -> None:
        self.__coca_ball_manager.update(obstacles, enemies)

        if (
            self.__borracho_time is not None
            and time.get_ticks() > self.__borracho_time
        ):
            if self.__prev_level is not None:
                self.__hero_level = self.__prev_level
                self._prev_level = None

            self.__borracho_time = None

        if (
            self.__invulnerable_time is not None
            and time.get_ticks() > self.__invulnerable_time
        ):
            self.__is_invulnerable = False
            self.set_transparency(255)
            self.__invulnerable_time = None

        self.__actions_handler.handle_hero_actions(game_events)

        if self.__win_handler.handle_win():
            return

        if self.__dead_handler.handle_dead():
            return

        hero_rect: Rect = self.get_rect()

        dx, dy = self.__movement_handler.handle_hero_movements(
            hero_rect, game_events, camera
        )
        dx, dy = self.__collisions_handler.handle_collisions(
            hero_rect, obstacles, dx, dy
        )
        self.add_x_rect(dx)
        self.add_y_rect(dy)
        self.__jump_handler.handle_hero_jump(game_events)
        self.__damage_handler.handle_damage()
        self.__check_point_handler.handle_check_point()

    def is_borracho(self) -> bool:
        return self.__borracho_time is not None

    def is_invulnerable(self) -> bool:
        return self.__is_invulnerable

    def borracho(self) -> None:
        self.__prev_level = self.__hero_level
        self.__borracho_time = time.get_ticks() + 10000

        if self.__hero_level == HeroLevel.NORMAL:
            self.__hero_level = HeroLevel.BORRACHO_SMALL
        else:
            self.__hero_level = HeroLevel.BORRACHO_BIG

    def grow(self, level: HeroLevel) -> None:
        if self.__prev_level is None:
            self.__hero_level = level
            return

        self.__prev_level = level
        self.__hero_level = HeroLevel.BORRACHO_BIG

    def decrease(self) -> None:
        index = self.__levels.index(self.__hero_level)

        if index == 0 and not self.__is_invulnerable:
            self.set_index(0)
            self.set_hero_state(HeroState.DEAD)
            self.set_action(HeroAction.DEAD, True)
            return

        if not self.__is_invulnerable:
            self.__is_invulnerable = True
            self.set_transparency(165)
            self.__invulnerable_time = time.get_ticks() + 3000

        if index != 0:
            self.__hero_level = self.__levels[index - 1]

    def draw(
        self,
        screen: Surface,
        camera: Optional[Camera] = None,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        self.__coca_ball_manager.draw(screen, camera)

        super().draw(screen, camera, x_rect_percent, y_rect_percent)

    def animate(self) -> None:
        self.__coca_ball_manager.animate()

        super().animate()
