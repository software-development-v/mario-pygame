from src.enums import HeroAction, HeroState

from .....interfaces import IHero
from ..interfaces import IHeroActionStrategy


class HeroActionRun(IHeroActionStrategy):
    def execute(self, hero: IHero):
        hero.set_hero_state(HeroState.RUN)
        hero.set_actions(
            {
                HeroAction.JUMPING: False,
                HeroAction.RUNNING: True,
                HeroAction.IDLE: False,
                HeroAction.WIN: False,
            }
        )
