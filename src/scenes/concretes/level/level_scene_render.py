from src.level import ILevelManager
from src.utils.camera import Camera
from src.utils.constants import (
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_HEIGHT,
    SCREEN_VIEW_PLAY_WIDTH,
)

from ...abstractions import Render
from .level_metrics_renderer import LevelMetricsRenderer


class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager
        self.camera = Camera(
            self.level_manager.get_screen_width(),
            SCREEN_HEIGHT,
            SCREEN_VIEW_PLAY_WIDTH,
            SCREEN_CAMERA_THRESHOLD,
            SCREEN_VIEW_PLAY_HEIGHT,
        )
        super().__init__()
        self.level_metrics_renderer = LevelMetricsRenderer(self._screen)

    def render(self) -> None:
        background = self.level_manager.get_background()
        self._screen.blit(background, (0, 0))

        obstacle_manager = self.level_manager.get_obstacle_manager()
        hero = self.level_manager.get_hero()

        self.camera.update(hero)

        obstacle_manager.draw(self._screen, self.camera)
        hero.draw(self._screen, self.camera)

        self.level_metrics_renderer.render(
            self.level_manager.get_current_time(),
            self.level_manager.get_score(),
            0,
            0,
        )
