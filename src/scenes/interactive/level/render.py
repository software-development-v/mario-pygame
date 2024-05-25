from src.data.level_data import LevelData
from src.scenes.render import IRender
from src.state.game_state import GameState
from pygame import Surface



class LevelSceneRender(IRender):
    def __init__(self,data:LevelData) -> None:
        self.data = data

    def render(self, game_state: GameState, screen: Surface) -> None:
        background_screen = self.data.background.get_background()
        screen.blit(background_screen, (0, 0))
        super().render(game_state, background_screen)


