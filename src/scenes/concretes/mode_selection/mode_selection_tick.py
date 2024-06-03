from src.enums import GameEvent
from src.inputs import IEventManager

from ...interfaces import ISceneManager, ITick


class ModeSelectionSceneTick(ITick):
    def tick(
        self, events_manager: IEventManager, scene_manager: ISceneManager
    ) -> None:
        events = events_manager.get_events()

        if events[GameEvent.JUMP]:
            scene_manager.next_scene()
