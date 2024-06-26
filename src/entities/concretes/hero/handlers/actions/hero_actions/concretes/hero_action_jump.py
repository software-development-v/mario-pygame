from pygame import mixer

from src.enums import HeroAction, HeroState
from src.utils import JUMP_SOUND, JUMP_VELOCITY

from .....interfaces import IHero
from ..interfaces import IHeroActionStrategy


class HeroActionJump(IHeroActionStrategy):
    def __init__(self) -> None:
        self.sound = mixer.Sound(JUMP_SOUND)

    def execute(self, hero: IHero):
        self.sound.play()
        hero.set_vel_y(-JUMP_VELOCITY)
        hero.set_hero_state(HeroState.JUMP)
        hero.set_actions(
            {
                HeroAction.JUMPING: True,
                HeroAction.RUNNING: False,
                HeroAction.IDLE: False,
            }
        )
