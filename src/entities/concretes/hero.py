from typing import Dict, List

from pygame import Surface, time, transform

from src.enums import GameEvent, HeroLevel, HeroState
from src.utils import Camera, Position
from src.utils.constants import (
    ANIMATION_INTERVAL,
    DEAD_FALL_THRESHOLD,
    HERO_SPEED,
    INIT_IMAGE_INDEX,
    JUMP_VELOCITY,
    MAX_GRAVITY,
    SCREEN_HEIGHT,
)

from ..abstractions import Element, InteractiveElement
from ..interfaces import IDrawable


class Hero(IDrawable):
    def __init__(
        self,
        surfaces: Dict[HeroLevel, Dict[HeroState, List[Surface]]],
        position: Position,
    ) -> None:
        self.surfaces = surfaces
        self.hero_level = HeroLevel.NORMAL
        self.hero_state = HeroState.IDLE
        self.index = INIT_IMAGE_INDEX
        self.image = self.surfaces[self.hero_level][self.hero_state][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = position.x
        self.rect.y = position.y
        self.rect.width = self.rect.width
        self.width = self.rect.width
        self.height = self.rect.height
        self.vel_y = 0
        self.face_right = True
        self.jumping = False
        self.running = False
        self.last_update = time.get_ticks()

    def draw(self, screen: Surface, camera: Camera) -> None:
        if not self.face_right:
            self.image = transform.flip(self.image, True, False)

        screen.blit(self.image, camera.apply(self))

    def __handle_hero_states(self, game_events: Dict[GameEvent, bool]):
        if game_events[GameEvent.UP] and not self.jumping:
            self.vel_y = -JUMP_VELOCITY
            self.index = INIT_IMAGE_INDEX
            self.hero_state = HeroState.JUMP
            self.jumping = True
            self.running = False
        elif (
            (game_events[GameEvent.LEFT] or game_events[GameEvent.RIGHT])
            and not self.jumping
            and not self.running
        ):
            self.index = INIT_IMAGE_INDEX
            self.hero_state = HeroState.RUN
            self.running = True
        elif not self.running and not self.jumping:
            self.index = INIT_IMAGE_INDEX
            self.hero_state = HeroState.IDLE

    def __handle_hero_movement(
        self, game_events: Dict[GameEvent, bool], camera: Camera
    ) -> tuple[int, int]:
        dx = 0
        dy = 0

        if game_events[GameEvent.RIGHT]:
            self.face_right = True
            dx = HERO_SPEED
        elif (
            game_events[GameEvent.LEFT] and self.rect.x > camera.get_left_edge()
        ):
            self.face_right = False
            dx = -HERO_SPEED
        else:
            self.running = False

        dy += self.vel_y

        self.vel_y += 1

        if self.vel_y > MAX_GRAVITY:
            self.vel_y = MAX_GRAVITY

        return dx, dy

    def __handle_x_collisions(self, obstacles: List[Element], dx: int) -> int:
        for obstacle in obstacles:
            if not obstacle.is_touchable:
                continue

            if not obstacle.get_rect().colliderect(
                self.rect.x + dx, self.rect.y, self.width, self.height
            ):
                continue

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers()

            dx = 0
            break

        return dx

    def __handle_y_collisions(self, obstacles: List[Element], dy: int) -> int:
        for obstacle in obstacles:
            if not obstacle.is_touchable:
                continue

            if not obstacle.get_rect().colliderect(
                self.rect.x, self.rect.y + dy, self.width, self.height
            ):
                continue

            if self.vel_y < 0:
                dy = obstacle.get_rect().bottom - self.rect.top
                self.vel_y = 0
            elif self.vel_y >= 0:
                dy = obstacle.get_rect().top - self.rect.bottom
                self.vel_y = 0
                self.jumping = False

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
        if self.rect.top > SCREEN_HEIGHT + DEAD_FALL_THRESHOLD:
            self.index = INIT_IMAGE_INDEX
            self.hero_state = HeroState.DEAD

    def __update_image(self) -> None:
        images = self.surfaces[self.hero_level][self.hero_state]
        current_time = time.get_ticks()

        if current_time - self.last_update > ANIMATION_INTERVAL:
            self.last_update = current_time
            self.index = (self.index + 1) % len(images)

        self.image = images[self.index]

    def update(
        self,
        game_events: Dict[GameEvent, bool],
        obstacles: List[Element],
        camera: Camera,
    ) -> None:
        self.__handle_hero_states(game_events)
        dx, dy = self.__handle_hero_movement(game_events, camera)
        dx, dy = self.__handle_collisions(obstacles, dx, dy)
        self.rect.x += dx
        self.rect.y += dy
        self.__check_dead()
        self.__update_image()
