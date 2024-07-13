from src.enums import HeroAction, HeroLevel, HeroState

from .....interfaces import IHero
from ..interfaces import IHeroActionStrategy


class HeroActionDead(IHeroActionStrategy):
    def execute(self, hero: IHero):
        hero.set_hero_level(HeroLevel.NORMAL)
        hero.set_hero_state(HeroState.DEAD)
        hero.set_actions(
            {
                HeroAction.IDLE: False,
                HeroAction.JUMPING: False,
                HeroAction.RUNNING: False,
                HeroAction.WIN: False,
                HeroAction.DEAD: True,
            }
        )
