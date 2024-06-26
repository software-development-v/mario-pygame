from src.enums import HeroLevel
from src.enums import HeroState
from ..abstracts import LevelState
from pygame import Surface
from src.utils import get_centered_message



class LevelStatusState(LevelState):

    def render(self, screen: Surface) -> None:
        world = self.level_manager.get_world().value
        level = self.level_manager.get_level().value
        message, message_rect = get_centered_message(
            f"WORLD {world}-{level}"
        )
        lifes, lifes_rect = get_centered_message(
            f"X {self.level_manager.get_lifes()}"
        )
        screen.blit(message, (message_rect.x, message_rect.y - 200))
        screen.blit(lifes, (lifes_rect.x + 40, lifes_rect.y))
        hero = self.game_data.get_hero_data(self.level_manager.get_hero_type())[HeroLevel.NORMAL][HeroState.IDLE][0]
        screen.blit(hero, (lifes_rect.x - 40, lifes_rect.y - 20))

