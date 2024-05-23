from src.enums.custom_event import CustomEvent
from src.enums.state import State
from src.scene_abstraction.behaviors.tick import ITick
from src.state.game_state import GameState


class ModeSelectionSceneTick(ITick):
    def __init__(self) -> None:
        return

    def tick(self, game_state: GameState) -> None:
        if game_state.events[CustomEvent.JUMP]:
            game_state.state = State.NEXT
