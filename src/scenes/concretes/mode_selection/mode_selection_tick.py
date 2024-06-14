from typing import Callable, Dict

from src.enums import GameEvent, HeroType, Level, SceneAction, World

from ...abstractions import Tick
from ..transition_level import TransitionLevelScene


class ModeSelectionSceneTick(Tick):
    def __init__(self, dispatcher: Dict[SceneAction, Callable[..., None]]):
        super().__init__(dispatcher)

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:

        if game_events[GameEvent.JUMP]:
            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                TransitionLevelScene(
                    HeroType.CUMPA, World.ONE, Level.FIRST, self._dispatcher
                )
            )
            self._dispatcher[SceneAction.END]()
