from sys import exit
from typing import Callable, Dict, List, Optional

from pygame import QUIT, Event, display, event, init, mixer, quit, time

from src.data import GameData
from src.enums import GameEvent, GameState, HeroType
from src.inputs import ControllerInputHandler, IInputHandler, KeyboardInputHandler
from src.utils.assets import ICON
from src.utils.constants import CURRENT_CHARACTER_INDEX, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE
from src.managers.game.hero import Hero

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

        self.character_names = [HeroType.PARIENTE, HeroType.HIJITA, HeroType.CUMPA]
        self.current_character_index = CURRENT_CHARACTER_INDEX
        self.hero = Hero(self.character_names[self.current_character_index])

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

    def move_hero_left(self) -> None:
        self.hero.move_left()

    def move_hero_right(self) -> None:
        self.hero.move_right()

    def change_hero(self) -> None:
        self.current_character_index = (self.current_character_index + 1) % len(self.character_names)
        self.hero.change_hero(self.character_names[self.current_character_index])
