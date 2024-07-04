from typing import Dict, Tuple

from pygame import Rect

from src.enums import GameEvent, HeroAction
from src.utils import HERO_SPEED, MAX_GRAVITY, Camera

from ....interfaces import IHero
from ..interfaces import IMovementHandler


class MovementHandler(IMovementHandler):
    def __init__(self, hero: IHero) -> None:
        self.__hero = hero

    def handle_hero_movements(
        self,
        hero_rect: Rect,
        game_events: Dict[GameEvent, bool],
        camera: Camera,
    ) -> Tuple[float, float]:
        dx: float = 0.0

        if game_events[GameEvent.RIGHT]:
            dx = HERO_SPEED
            self.__hero.set_face_right(True)
        elif (
            game_events[GameEvent.LEFT] and hero_rect.x > camera.get_left_edge()
        ):
            dx = -HERO_SPEED
            self.__hero.set_face_right(False)
        else:
            self.__hero.set_action(HeroAction.RUNNING, False)
            self.__hero.set_action(HeroAction.IDLE, True)

        self.__hero.add_vel_y(1)

        if self.__hero.get_vel_y() > MAX_GRAVITY:
            self.__hero.set_vel_y(MAX_GRAVITY)

        return dx, self.__hero.get_vel_y()
