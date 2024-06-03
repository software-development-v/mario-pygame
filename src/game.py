from pygame import init, mixer

from .data import GameData, IGameData
from .inputs import EventManager, IEventManager
from .scenes import ISceneManager, SceneManager


class Game:
    def __init__(self) -> None:
        init()
        mixer.init()

        self.__running = True
        self.__game_data: IGameData = GameData()
        self.__events_manager: IEventManager = EventManager()
        self.__scene_manager: ISceneManager = SceneManager(
            self.__events_manager, self.__game_data
        )

    def run(self) -> None:
        while self.__running:
            self.__events_manager.handle_events()
            self.__scene_manager.display_current_scene()
