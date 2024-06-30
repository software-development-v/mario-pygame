from src.enums import HeroAction, HeroState

from .....interfaces import IHero
from ..interfaces import IHeroActionStrategy


class HeroActionWin(IHeroActionStrategy):
    def execute(self, hero: IHero):
        hero.set_hero_state(HeroState.DOWN)
        hero.set_actions(
            {
                HeroAction.IDLE: False,
                HeroAction.JUMPING: False,
                HeroAction.RUNNING: False,
                HeroAction.WIN: True,
            }
        )
