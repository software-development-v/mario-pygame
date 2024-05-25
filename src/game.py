from sys import exit
from typing import List

from pygame import QUIT, display, event, init, mixer, quit, time

from src.data.background.BackgroundColor import BackgroundColor
from src.data.level_data import LevelData
from src.data.levels import Levels
from src.enums.state import State
from src.events.behaviors.input_handler import IInputHandler
from src.events.control_handler import ControlHandler
from src.events.keyboard_handler import KeyboardHandler


from src.scenes.cinematic.scene import CinematicScene
from src.scenes.interactive.level.level_scene import LevelScene
from src.scenes.interactive.mode_selection.scene import ModeSelectionScene
from src.scenes.scene_deck import SceneDeck
from src.settings.control import ControlSettings
from src.state.game_state import GameState
from src.utils.assets import FINAL_CINEMATIC_AUDIO, FINAL_CINEMATIC_VIDEO, ICON
from src.utils.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE


class Game:
    def __init__(self) -> None:
        init()
        mixer.init()
        display.set_caption(TITLE)
        display.set_icon(ICON)

        self.clock = time.Clock()
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.control_settings = ControlSettings()
        self.game_state = GameState()
        self.events_handler: List[IInputHandler] = [
            KeyboardHandler(),
            ControlHandler(self.control_settings),
        ]

        self.scene_deck = self.setup_scenes()

    def event(self) -> None:
        events = event.get()

        for e in events:
            if e.type == QUIT:
                quit()
                exit()

        for handler in self.events_handler:
            handler.handle(events, self.game_state.events)

    def run(self) -> None:
        while self.game_state.state == State.RUNNING:
            self.event()

            self.scene_deck.display()
            display.update()

            self.clock.tick(FPS)

        if self.game_state.state == State.RESTART:
            self.reset_game()

        if self.game_state.state == State.NEXT:
            self.go_to_next_scene()

    def reset_game(self) -> None:
        self.scene_deck = self.setup_scenes()
        self.reload_game()

    def go_to_next_scene(self) -> None:
        display.flip()

        next_scene = self.scene_deck.next_scene()
        if next_scene is None:
            self.reset_game()
            return

        self.reload_game()

    def reload_game(self) -> None:
        self.game_state.reset()
        self.run()

    def setup_scenes(self) -> SceneDeck:
        deck = SceneDeck()
        deck.add(ModeSelectionScene(self.game_state))
        deck.add(LevelScene(self.game_state, LevelData(Levels.LEVEL_1, 0,BackgroundColor((23, 155, 236)),"",(0,0),)))
        deck.add(CinematicScene(self.game_state,FINAL_CINEMATIC_VIDEO, FINAL_CINEMATIC_AUDIO))
        return deck
