from typing import Callable, Dict, Optional

from pygame.mixer import Sound

from src.enums import GameEvent, SceneAction

from ...interfaces import IScene
from ..tick import Tick


class CinematicSceneTick(Tick):
    def __init__(
        self,
        get_success: Callable[[], bool],
        audio: Sound,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        next_scene: Optional[IScene] = None,
    ):
        self.__get_success = get_success
        self.__audio = audio
        self.__next_scene = next_scene
        super().__init__(dispatcher)

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        if game_events[GameEvent.PAUSE] or not self.__get_success():
            self.__audio.stop()
            if self.__next_scene is not None:
                self._dispatcher[SceneAction.SET_NEXT_SCENE](self.__next_scene)
            self._dispatcher[SceneAction.END]()
