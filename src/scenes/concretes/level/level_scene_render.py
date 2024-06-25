from src.level import ILevelManager

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
        camera.update(hero)

        obstacle_manager = self.__level_manager.get_obstacle_manager()
        obstacle_manager.draw(self._screen, camera)
        hero.draw(self._screen, camera)

        self.__level_metrics_renderer.render(
            self.__level_manager.get_hero_type().value,
            self.__level_manager.get_current_time(),
            self.__level_manager.get_score(),
            0,
            self.__level_manager.get_world().value,
            self.__level_manager.get_level().value
        )
