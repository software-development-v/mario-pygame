from typing import Callable, Dict

from src.enums import GameEvent, HeroType, Level, SceneAction, World

from ...interfaces import IScene, ITick
from ..transition_level import TransitionLevelScene


class ModeSelectionSceneTick(ITick):
    def tick(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:

        if game_events[GameEvent.JUMP]:
            set_next_scene(
                TransitionLevelScene(HeroType.CUMPA, World.ONE, Level.FIRST)
            )
            dispatcher[SceneAction.END]()
