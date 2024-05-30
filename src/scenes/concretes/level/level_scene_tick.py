from src.enums import GameEvent, GameState
from src.managers import GameManager

from ...interfaces import ITick


class LevelSceneTick(ITick):
    def __init__(self) -> None:
        super().__init__()

    def tick(self, game_manager: GameManager) -> None:
        if game_manager.game_events[GameEvent.JUMP]:
            game_manager.game_state = GameState.NEXT_SCENE

        if game_manager.hero:
            game_manager.hero.update(game_manager.game_events)

        if game_manager.elements_manager:
            game_manager.elements_manager.update()
