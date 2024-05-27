from sys import exit
from typing import Callable, Dict, List, Optional

from pygame import QUIT, Event, display, event, init, mixer, quit, time

from src.data import GameData
from src.enums import GameEvent, GameState
from src.inputs import ControllerInputHandler, IInputHandler, KeyboardInputHandler
from src.utils.assets import ICON
from src.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE


class GameManager:
    def __init__(self) -> None:
        init()

        self.mixer = mixer
        self.display = display
        self.event = event
        self.clock = time.Clock()
        self.initialize()

        self.game_state = GameState.RUNNING
        self.game_events: Dict[GameEvent, bool] = self.reset_game_events()
        self.game_data = GameData()
        self.inputs_handler: List[IInputHandler] = [
            KeyboardInputHandler(),
            ControllerInputHandler(),
        ]

    def initialize(self) -> None:
        self.mixer.init()
        self.display.set_caption(TITLE)
        self.display.set_icon(ICON)
        self.screen = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def reset_game_events(self) -> Dict[GameEvent, bool]:
        return {
            GameEvent.UP: False,
            GameEvent.DOWN: False,
            GameEvent.LEFT: False,
            GameEvent.RIGHT: False,
            GameEvent.JUMP: False,
            GameEvent.RUN: False,
            GameEvent.ATTACK: False,
            GameEvent.PAUSE: False,
        }

    def check_close_event(self, events: Optional[List[Event]] = None) -> None:
        if events is None:
            events = self.event.get()

        for e in events:
            if e.type == QUIT:
                quit()
                exit()

    def handle_events(self) -> None:
        events = self.event.get()

        self.check_close_event(events)

        for handler in self.inputs_handler:
            handler.handle(events, self.game_events)

    def handle_states(self, next_scene: Callable[[], None]) -> None:
        if self.game_state == GameState.NEXT_SCENE:
            next_scene()

        self.game_events = self.reset_game_events()
