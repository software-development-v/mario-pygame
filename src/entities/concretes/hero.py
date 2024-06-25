from typing import Dict, List

from pygame import Surface

from src.enums import GameEvent, HeroLevel, HeroState
from src.utils import (
    DEAD_FALL_THRESHOLD,
    HERO_SPEED,
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
        self.__vel_y = 0
        self.__jumping = True
        self.__running = False
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__hero_level][self.__hero_state]

    def __handle_hero_states(self, game_events: Dict[GameEvent, bool]):
        if game_events[GameEvent.JUMP] and not self.__jumping:
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
        self, game_events: Dict[GameEvent, bool], camera: Camera
    ) -> tuple[int, int]:
        dx = 0
        dy = 0

        if game_events[GameEvent.RIGHT]:
            dx = HERO_SPEED
            self.set_face_right(True)
        elif (
            game_events[GameEvent.LEFT]
            and self.get_x_rect() > camera.get_left_edge()
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

    def __handle_x_collisions(self, obstacles: List[Element], dx: int) -> int:
        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            if not obstacle.get_rect().colliderect(
                self.get_x_rect() + dx,
                self.get_y_rect(),
                self.get_width(),
                self.get_height(),
            ):
                continue

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers()

            dx = 0
            break

        return dx

    def __handle_y_collisions(self, obstacles: List[Element], dy: int) -> int:
        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            if not obstacle.get_rect().colliderect(
                self.get_x_rect(),
                self.get_y_rect() + dy,
                self.get_width(),
                self.get_height(),
            ):
                continue

            if self.__vel_y < 0:
                dy = obstacle.get_rect().bottom - self.get_rect().top
                self.__vel_y = 0
            elif self.__vel_y >= 0:
                dy = obstacle.get_rect().top - self.get_rect().bottom
                self.__vel_y = 0
                self.__jumping = False

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers()

            break

        return dy

    def __handle_collisions(
        self, obstacles: List[Element], dx: int, dy: int
    ) -> tuple[int, int]:
        dx = self.__handle_x_collisions(obstacles, dx)
        dy = self.__handle_y_collisions(obstacles, dy)
        return dx, dy

    def __check_dead(self) -> None:
        if self.get_rect().top > SCREEN_HEIGHT + DEAD_FALL_THRESHOLD:
            self.__hero_state = HeroState.DEAD

    def get_hero_state(self) -> HeroState:
        return self.__hero_state

    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: List[Element],
        camera: Camera,
    ) -> None:
        self.__handle_hero_states(game_events)
        dx, dy = self.__handle_hero_movement(game_events, camera)
        dx, dy = self.__handle_collisions(obstacles, dx, dy)
        self.set_x_rect(self.get_x_rect() + dx)
        self.set_y_rect(self.get_y_rect() + dy)
        self.__check_dead()
