from src.level import ILevelManager

from ...abstractions import Render
from .level_metrics_renderer import LevelMetricsRenderer


class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        super().__init__()
        self.level_manager = level_manager
        self.level_metrics_renderer = LevelMetricsRenderer(self._screen)

    def render(self) -> None:
        background = self.level_manager.get_background()
        self._screen.blit(background, (0, 0))

        hero = self.level_manager.get_hero()
        camera = self.level_manager.get_camera()
        camera.update(hero.get_x_rect(), hero.get_width())

        obstacles_manager = self.level_manager.get_obstacles_manager()
        obstacles_manager.draw(self._screen, camera)

        hero.draw(self._screen, camera)

        self.level_metrics_renderer.render(
            self.level_manager.get_hero_type().value,
            self.level_manager.get_current_time(),
            self.level_manager.get_score(),
            0,
        )
