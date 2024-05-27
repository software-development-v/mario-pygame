from src.enums import GameEvent, GameState
from src.managers import GameManager

from ...interfaces import ITick


class ModeSelectionSceneTick(ITick):
    def __init__(self) -> None:
        super().__init__()

    def tick(self, game_manager: GameManager) -> None:
        if game_manager.game_events[GameEvent.JUMP]:
            game_manager.game_state = GameState.NEXT_SCENE
