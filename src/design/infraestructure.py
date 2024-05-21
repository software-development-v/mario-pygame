from pygame.time import Clock

from src.design.render.game_renderer import GameRenderer
from src.design.settings.settings import Settings
from src.utils.constants import FPS


class Infrastructure:
    def __init__(self, settings_game: Settings, render_game: GameRenderer):
        self.settings_game = settings_game
        self.render_game = render_game

    def save_game(self) -> None:
        # TODO: Implement this method to save the game
        pass

    def stop_game(self) -> None:
        # TODO: Implement this method to stop the game
        pass

    def continue_game(self) -> None:
        # TODO: Implement this method to continue the game
        pass

    def render(self, clock: Clock) -> None:
        clock.tick(FPS)

        self.render_game.render()
