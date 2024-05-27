from pygame import time

from src.enums import GameState, Level, World
from src.managers import GameManager
from src.utils.colors import BLACK_COLOR, WHITE_COLOR
from src.utils.constants import FPS, TRASITION_DURATION
from src.utils.text import get_centered_message

from ...interfaces import IRender


class TransitionLevelSceneRender(IRender):
    def __init__(self, world: World, level: Level) -> None:
        super().__init__()
        self.world = world
        self.level = level

    def render(self, game_manager: GameManager) -> None:
        start_time = time.get_ticks()
        running = True

        while running:
            game_manager.check_close_event()
            game_manager.screen.fill(BLACK_COLOR)
            text, text_rect = get_centered_message(
                f"Enter to World {self.world} - Level {self.level}",
                text_color=WHITE_COLOR,
            )
            game_manager.screen.blit(text, text_rect)
            game_manager.display.update()

            current_time = time.get_ticks()
            if current_time - start_time >= TRASITION_DURATION:
                running = False

            game_manager.clock.tick(FPS)

        game_manager.game_state = GameState.NEXT_SCENE
