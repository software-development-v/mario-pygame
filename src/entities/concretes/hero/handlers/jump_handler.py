from typing import Dict

from pygame import mixer

from src.enums import GameEvent
from src.enums.hero_action import HeroAction
from src.utils import JUMP_SOUND

from ..interfaces import IHero


class JumpHandler:

    FROM = 0
    TO = 1
    HEIGHT = 2
    TAKEN = 3
    MAX_CLICKS_PER_JUMP = 16

    def __init__(self, hero: IHero) -> None:
        self.__hero = hero
        self.sound = mixer.Sound(JUMP_SOUND)
        self.__clicks_counter = 0
        self.__is_jumping = False
        self.__jump_heights: list[list[int]] = [
            [0, 5, -17, False],
            [6, 11, -6, False],
            [12, 16, -3, False],
        ]

    def handle_hero_jump(self, input: Dict[GameEvent, bool]) -> None:
        if not input[GameEvent.UP]:
            if not self.__hero.get_actions()[HeroAction.JUMPING]:
                self.__is_jumping = False
            return

        if (
            input[GameEvent.UP]
            and not self.__hero.get_actions()[HeroAction.JUMPING]
            and not self.__is_jumping
        ):
            self.sound.play()
            self.__is_jumping = True
            self.__clicks_counter = 0
            self.__reset_jumps_taken()

        if (
            self.__is_jumping
            and self.__clicks_counter < self.MAX_CLICKS_PER_JUMP
        ):
            self.__handle_precision_jump_timing(self.__hero)
            self.__clicks_counter += 1

    def __reset_jumps_taken(self) -> None:
        for jump in self.__jump_heights:
            jump[self.TAKEN] = False

    def __handle_precision_jump_timing(self, hero: IHero) -> None:
        for jump in self.__jump_heights:
            if jump[self.FROM] <= self.__clicks_counter <= jump[self.TO]:
                if not jump[self.TAKEN]:
                    hero.add_vel_y(jump[self.HEIGHT])
                    jump[self.TAKEN] = True
                break
