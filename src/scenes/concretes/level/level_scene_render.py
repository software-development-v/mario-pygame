from pygame import Rect

from src.enums import HeroLevel
from src.level import ILevelManager
from src.utils import (
    HERO_BIG_RECT_X_PERCENT,
    HERO_NORMAL_RECT_X_PERCENT,
    HERO_RECT_Y_PERCENT,
)

from ...abstractions import Render
from .level_metrics_renderer import LevelMetricsRenderer


class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        super().__init__()
        self.__level_manager = level_manager
        self.__level_metrics_renderer = LevelMetricsRenderer(self._screen)

    def render(self) -> None:
        background = self.__level_manager.get_background()
        self._screen.blit(background, (0, 0))

        hero = self.__level_manager.get_hero()
        camera = self.__level_manager.get_camera()

        hero_rect: Rect = hero.get_rect()
        camera.update(hero_rect.x, hero_rect.width)

        obstacle_manager = self.__level_manager.get_obstacles_manager()
        obstacle_manager.draw(self._screen, camera)

        hero_x_rect_percent = (
            hero.get_hero_level() == HeroLevel.NORMAL
            and HERO_NORMAL_RECT_X_PERCENT
            or HERO_BIG_RECT_X_PERCENT
        )
        hero_y_rect_percent = HERO_RECT_Y_PERCENT

        hero.draw(
            self._screen, camera, hero_x_rect_percent, hero_y_rect_percent
        )
        self.__level_metrics_renderer.render(
            self.__level_manager.get_hero_type().value,
            self.__level_manager.get_current_time(),
            self.__level_manager.get_score(),
            0,
            self.__level_manager.get_world().value,
            self.__level_manager.get_level().value,
        )
