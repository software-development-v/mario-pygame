from pygame import Surface

from src.enums import HeroLevel, HeroState
from src.utils import get_centered_message

from ..abstracts import LevelState


class LevelStatusState(LevelState):

    def render(self, screen: Surface) -> None:
        world = self.level_manager.get_world().value
        level = self.level_manager.get_level().value
        message, message_rect = get_centered_message(f"WORLD {world}-{level}")
        lives, lives_rect = get_centered_message(
            f"X {self.level_manager.get_lives()}"
        )
        screen.blit(message, (message_rect.x, message_rect.y - 200))
        screen.blit(lives, (lives_rect.x + 40, lives_rect.y))
        hero = self.game_data.get_hero_data(self.level_manager.get_hero_type())[
            HeroLevel.NORMAL
        ][HeroState.IDLE][0]
        screen.blit(hero, (lives_rect.x - 40, lives_rect.y - 20))
