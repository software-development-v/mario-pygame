from src.level import ILevelManager
from src.level.concretes.camera_controller import camera
from ...abstractions import Render
from .level_metrics_renderer import LevelMetricsRenderer

class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        super().__init__()
        self.level_manager = level_manager

        self.camera = camera

        self.level_metrics_renderer = LevelMetricsRenderer(self._screen)

    def render(self) -> None:
        background = self.level_manager.get_background()
        self._screen.blit(background, (0, 0))

        hero = self.level_manager.get_hero()
        self.camera.update(hero)

        obstacle_manager = self.level_manager.get_obstacle_manager()
        obstacle_manager.draw(self._screen, self.camera)
        hero.draw(self._screen, self.camera)

        self.level_metrics_renderer.render(
            self.level_manager.get_current_time(),
            self.level_manager.get_score(),
            0,
            0,
        )
