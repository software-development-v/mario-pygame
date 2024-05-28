from typing import Callable
import pygame
from src.enums import GameState
from src.enums.game_event import GameEvent
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE
from .player import Player

class GameManager:
    def __init__(self) -> None:
        pygame.init()
        self.mixer = pygame.mixer
        self.display = pygame.display
        self.event = pygame.event
        self.clock = pygame.time.Clock()
        self.initialize()

        self.game_state = GameState.RUNNING
        self.player = Player(100, 100, [
            pygame.image.load("assets/mario/mario1.png"),
            pygame.image.load("assets/mario/mario2.png"),
            pygame.image.load("assets/mario/mario3.png")
        ])

    def initialize(self) -> None:
        self.mixer.init()
        self.display.set_caption(TITLE)
        self.screen = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def handle_events(self) -> None:
        events = self.event.get()

        self.check_close_event(events) # type: ignore

        for handler in self.inputs_handler: # type: ignore
            handler.handle(events, self.game_events) # type: ignore
            if self.game_events[GameEvent.LEFT]: # type: ignore
                self.player.move_left()
            if self.game_events[GameEvent.RIGHT]: # type: ignore
                self.player.move_right()

    def handle_states(self, next_scene: Callable[[], None]) -> None:
        if self.game_state == GameState.NEXT_SCENE:
            next_scene()

        self.player.update() 
