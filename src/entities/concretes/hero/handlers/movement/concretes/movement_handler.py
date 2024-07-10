from typing import Dict, Tuple

from pygame import Rect

from src.enums import GameEvent, HeroAction, HeroState
from src.utils import (
    ACCELERATION,
    FRICCION,
    HERO_SPEED,
    LEFT_LIMIT_LENGTH,
    MAX_BRAKE_STATUS,
    MAX_GRAVITY,
    Camera,
)

from ....interfaces import IHero
from ..interfaces import IMovementHandler


class MovementHandler(IMovementHandler):

    # Movement constants
    NONE = 0
    LEFT = 1
    RIGHT = 2
    BRAKE = 3

    TOTAL_CLICKS = 30

    def __init__(self, hero: IHero) -> None:
        self.__hero = hero
        self.__last_movement: int = self.NONE
        self.__hero_acceleration = 0
        self.__hero_speed = 0
        self.__brake_status = 0
        self.__clicks = 0

    def handle_hero_movements(
        self,
        hero_rect: Rect,
        game_events: Dict[GameEvent, bool],
        camera: Camera,
    ) -> Tuple[float, float]:
        self.__hero_speed = self.__hero.get_vel_x()

        self.__handle_input(hero_rect, game_events, camera)

        if self.__last_movement == self.BRAKE:
            self.__brake_hero()
            return 0, 0

        self.__update_hero_action()
        self.__handle_speed_bounds()
        self.__apply_gravity()
        self.__handle_left_camera_limit(camera)
        self.__hero.set_vel_x(self.__hero_speed)
        return self.__hero_speed, self.__hero.get_vel_y()

    def __handle_input(
        self,
        hero_rect: Rect,
        input: Dict[GameEvent, bool],
        camera: Camera,
    ) -> None:
        if self.__last_movement == self.BRAKE:
            return
        if self.__hero_speed == 0:
            self.__last_movement = self.NONE
        self.__handle_side_movements(hero_rect, input, camera)
        self.__hero_speed += self.__hero_acceleration

    def __handle_side_movements(
        self, hero_rect: Rect, input: Dict[GameEvent, bool], camera: Camera
    ) -> None:

        if input[GameEvent.RIGHT]:
            self.__handle_right_movement()
        elif (
            input[GameEvent.LEFT]
            and hero_rect.x >= camera.get_left_edge() + LEFT_LIMIT_LENGTH
        ):
            self.__handle_left_movement()
        else:
            self.__handle_no_movement()

    def __handle_right_movement(self) -> None:
        if not self.__hero.get_actions()[HeroAction.JUMPING]:
            self.__hero.set_face_right(True)

        if self.__hero_speed != 0 and (
            self.__last_movement == self.LEFT
            or self.__last_movement == self.NONE
        ):
            self.__brake()
        else:
            self.__hero_acceleration = ACCELERATION
            self.__update_clicks(self.RIGHT)
            self.__last_movement = self.RIGHT

    def __handle_left_movement(self) -> None:
        if not self.__hero.get_actions()[HeroAction.JUMPING]:
            self.__hero.set_face_right(False)

        if self.__hero_speed != 0 and (
            self.__last_movement == self.RIGHT
            or self.__last_movement == self.NONE
        ):
            self.__brake()
        else:
            self.__hero_acceleration = -ACCELERATION
            self.__update_clicks(self.LEFT)
            self.__last_movement = self.LEFT

    def __brake(self) -> None:
        if self.__clicks > self.TOTAL_CLICKS and (
            not self.__hero.get_actions()[HeroAction.JUMPING]
        ):
            self.__last_movement = self.BRAKE
            self.__brake_status = MAX_BRAKE_STATUS
        self.__clicks = 0
        self.__stop_hero()

    def __update_clicks(self, direction: int) -> None:
        if self.__last_movement == direction:
            self.__clicks += 1
        else:
            self.__clicks = 0

    def __handle_no_movement(self) -> None:
        if self.__last_movement == self.LEFT:
            self.__hero_acceleration = FRICCION
        elif self.__last_movement == self.RIGHT:
            self.__hero_acceleration = -FRICCION
        else:
            self.__hero_acceleration = 0

    def __brake_hero(self) -> None:
        if self.__brake_status > 0:
            self.__brake_status -= 1
            self.__hero.set_hero_state(HeroState.BRAKE)
            self.__hero.set_action(HeroAction.RUNNING, False)
            self.__hero.set_vel_x(0)
            self.__last_movement = self.BRAKE
            self.__stop_hero()
        else:
            self.__last_movement = self.NONE

    def __stop_hero(self) -> None:
        self.__hero_speed = 0
        self.__hero_acceleration = 0

    def __update_hero_action(self) -> None:
        if (
            self.__hero_speed != 0
            and not self.__hero.get_actions()[HeroAction.JUMPING]
        ):
            self.__hero.set_action(HeroAction.IDLE, False)
            self.__hero.set_action(HeroAction.RUNNING, True)
            if self.__hero_speed > 0:
                self.__hero.set_face_right(True)
            else:
                self.__hero.set_face_right(False)

    def __handle_speed_bounds(self) -> None:
        if abs(self.__hero_speed) > HERO_SPEED:
            self.__hero_speed = HERO_SPEED * (
                1 if self.__hero_speed > 0 else -1
            )

        if abs(self.__hero_speed) < FRICCION:
            self.__hero_speed = 0
            self.__hero.set_action(HeroAction.RUNNING, False)
            self.__hero.set_action(HeroAction.IDLE, True)
            self.__last_movement = self.NONE

    def __apply_gravity(self) -> None:
        self.__hero.add_vel_y(1)
        if self.__hero.get_vel_y() > MAX_GRAVITY:
            self.__hero.set_vel_y(MAX_GRAVITY)

    def __handle_left_camera_limit(self, camera: Camera) -> None:
        if (
            self.__hero.get_rect().x + self.__hero_acceleration
        ) < camera.get_left_edge() + LEFT_LIMIT_LENGTH:
            self.__hero.add_x_rect(-self.__hero.get_rect().x)
            self.__hero.add_x_rect(camera.get_left_edge() + LEFT_LIMIT_LENGTH)
            self.__hero_speed = 0
