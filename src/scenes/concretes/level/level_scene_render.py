from src.level import ILevelManager
from .level_metrics_renderer import LevelMetricsRenderer
from src.utils.camera import Camera
from src.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from ...abstractions import Render


class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, 800, 600, 800)
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
            0
        )
