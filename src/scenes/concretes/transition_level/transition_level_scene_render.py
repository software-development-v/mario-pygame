from typing import Tuple
from pygame import Rect, Surface
from src.data.game_data import GameData
from src.enums.hero_level import HeroLevel
from src.enums.hero_state import HeroState
from src.level import ILevelManager
from ..level.level_metrics_renderer import LevelMetricsRenderer
from src.utils.colors import BLACK_COLOR, WHITE_COLOR
from src.utils.text import get_centered_message

from ...abstractions import Render


class TransitionLevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager, game: GameData) -> None:
        self.__level_manager = level_manager
        self.game = game
        super().__init__()
        self.level_metrics_renderer = LevelMetricsRenderer(self._screen)
        self.time = -1

    def render(self) -> None:
        world = self.__level_manager.get_world().value
        level = self.__level_manager.get_level().value
        self._screen.fill(BLACK_COLOR)

        self.level_metrics_renderer.render(
            self.__level_manager.get_hero_type().value,
            -1,
            self.__level_manager.get_score(),
            0,
            world,
            level,
        )

        if self.time == -1 and self.__level_manager.get_current_time() <= 0:
            self.time = 50

        if self.time > 0:
            self.time -= 1
            message, message_rect = self.render_text("TIME OUT")
            self._screen.blit(message, (message_rect.x, message_rect.y))
        else:
            self.__level_manager.set_current_time(
                self.__level_manager.get_start_time()
            )
            self.render_status_game()

    def render_status_game(self):
        world = self.__level_manager.get_world().value
        level = self.__level_manager.get_level().value
        if self.__level_manager.get_lifes() == 0:
            message, message_rect = self.render_text("GAME OVER")
            self._screen.blit(message, (message_rect.x, message_rect.y))

        else:

            message, message_rect = self.render_text(f"WORLD {world}-{level}")
            lifes, lifes_rect = self.render_text(
                f"X {self.__level_manager.get_lifes()}"
            )
            self._screen.blit(message, (message_rect.x, message_rect.y - 200))
            self._screen.blit(lifes, (lifes_rect.x + 40, lifes_rect.y))

            hero = self.game.heroes_data[self.__level_manager.get_hero_type()][
                HeroLevel.NORMAL
            ][HeroState.IDLE][0]

            self._screen.blit(hero, (lifes_rect.x - 40, lifes_rect.y - 20))

    def render_text(self, message: str) -> Tuple[Surface, Rect]:
        return get_centered_message(message, text_color=WHITE_COLOR, size=30)
