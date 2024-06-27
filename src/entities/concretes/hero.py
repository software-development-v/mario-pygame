from typing import Dict, List

from pygame import Rect, Surface

from src.enums import GameEvent, HeroLevel, HeroState
from src.utils import (
    DEAD_FALL_THRESHOLD,
    HERO_BIG_RECT_X_PERCENT,
    HERO_NORMAL_RECT_X_PERCENT,
    HERO_RECT_Y_PERCENT,
    HERO_SPEED,
    INIT_VEL_Y,
    JUMP_VELOCITY,
    MAX_GRAVITY,
    SCREEN_HEIGHT,
    Camera,
    Position,
)

from ..abstractions import Element, InteractiveElement, Sprite


class Hero(Sprite):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[Surface]]],
        position: Position,
    ) -> None:
        self.__surfaces = surfaces
        self.__hero_level = HeroLevel.NORMAL
        self.__hero_state = HeroState.IDLE
        self.__vel_y = INIT_VEL_Y
        self.__jumping = True
        self.__running = False
        super().__init__(
            position,
            y_rect_percent=HERO_RECT_Y_PERCENT,
            x_rect_percent=self.__hero_level == HeroLevel.NORMAL
            and HERO_NORMAL_RECT_X_PERCENT
            or HERO_BIG_RECT_X_PERCENT,
        )

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__hero_level][self.__hero_state]

    def __handle_hero_states(self, game_events: Dict[GameEvent, bool]):
        if game_events[GameEvent.UP] and not self.__jumping:
            self.__vel_y = -JUMP_VELOCITY
            self.__hero_state = HeroState.JUMP
            self.__jumping = True
            self.__running = False
        elif (
            (game_events[GameEvent.LEFT] or game_events[GameEvent.RIGHT])
            and not self.__jumping
            and not self.__running
        ):
            self.__hero_state = HeroState.RUN
            self.__running = True
        elif not self.__running and not self.__jumping:
            self.__hero_state = HeroState.IDLE

    def __handle_hero_movement(
        self,
        hero_rect: Rect,
        game_events: Dict[GameEvent, bool],
        camera: Camera,
    ) -> tuple[float, float]:
        dx: float = 0.0
        dy: float = 0.0

        if game_events[GameEvent.RIGHT]:
            dx = HERO_SPEED
            self.set_face_right(True)
        elif (
            game_events[GameEvent.LEFT] and hero_rect.x > camera.get_left_edge()
        ):
            dx = -HERO_SPEED
            self.set_face_right(False)
        else:
            self.__running = False

        dy += self.__vel_y

        self.__vel_y += 1

        if self.__vel_y > MAX_GRAVITY:
            self.__vel_y = MAX_GRAVITY

        return dx, dy

    def __handle_x_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dx: float
    ) -> float:
        if dx == 0:
            return dx

        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            obstacle_rect: Rect = obstacle.get_rect()

            if not obstacle_rect.colliderect(
                hero_rect.x + dx, hero_rect.y, hero_rect.width, hero_rect.height
            ):
                continue

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers()

            if dx > 0:
                dx = obstacle_rect.left - hero_rect.right
            elif dx < 0:
                dx = obstacle_rect.right - hero_rect.left

            break

        return dx

    def __handle_y_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dy: float
    ) -> float:
        if dy == 0:
            return dy

        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            obstacle_rect: Rect = obstacle.get_rect()

            if not obstacle_rect.colliderect(
                hero_rect.x, hero_rect.y + dy, hero_rect.width, hero_rect.height
            ):
                continue

            if self.__vel_y < 0:
                dy = obstacle_rect.bottom - hero_rect.top
                self.__vel_y = 0
            elif self.__vel_y >= 0:
                dy = obstacle_rect.top - hero_rect.bottom
                self.__vel_y = 0
                self.__jumping = False

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers()

            break

        return dy

    def __handle_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dx: float, dy: float
    ) -> tuple[float, float]:
        dx = self.__handle_x_collisions(hero_rect, obstacles, dx)
        dy = self.__handle_y_collisions(hero_rect, obstacles, dy)
        return dx, dy

    def __check_dead(self) -> None:
        if self.get_rect().top > SCREEN_HEIGHT + DEAD_FALL_THRESHOLD:
            self.__hero_state = HeroState.DEAD

    def get_hero_level(self) -> HeroLevel:
        return self.__hero_level

    def get_hero_state(self) -> HeroState:
        return self.__hero_state

    def set_hero_level(self, level: HeroLevel) -> None:
        self.__hero_level = level

    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: List[Element],
        camera: Camera,
    ) -> None:
        hero_rect: Rect = self.get_rect()

        self.__handle_hero_states(game_events)
        dx, dy = self.__handle_hero_movement(hero_rect, game_events, camera)
        dx, dy = self.__handle_collisions(hero_rect, obstacles, dx, dy)
        self.add_x_rect(dx)
        self.add_y_rect(dy)
        self.__check_dead()
