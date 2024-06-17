from typing import Callable, Dict, Tuple
import pygame
from src.enums import GameEvent, SceneAction, HeroType, Level, World

from ...abstractions import Tick
from ..transition_level import TransitionLevelScene
from .main_menu_render import MainMenuRender


class MainMenuTick(Tick):
    def __init__(
        self,
        render: MainMenuRender,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ) -> None:
        self._dispatcher = dispatcher
        super().__init__(dispatcher)
        self.render = render
        self.last_switch_time = pygame.time.get_ticks()
        self.switch_delay = 100

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        selected_option = self.render.get_selected_option()
        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time > self.switch_delay:
            if game_events.get(GameEvent.UP) or game_events.get(GameEvent.LEFT):
                self.render.set_selected_option(selected_option - 1)
                self.last_switch_time = current_time
            elif game_events.get(GameEvent.DOWN) or game_events.get(
                GameEvent.RIGHT
            ):
                self.render.set_selected_option(selected_option + 1)
                self.last_switch_time = current_time
            elif game_events.get(GameEvent.JUMP):
                self.select_option(self._dispatcher)
                self.last_switch_time = current_time

        if mouse_click[0]:
            if self.render.handle_mouse_event(mouse_pos):
                self.select_option(self._dispatcher)
                self.last_switch_time = current_time

    def select_option(self, dispatcher: Dict[SceneAction, Callable[[], None]]):
        selected_option = self.render.get_selected_option()
        selected = self.render.menu_options[selected_option]

        if selected == "Quit":
            pygame.quit()
            exit()
        else:
            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                TransitionLevelScene(
                    HeroType.CUMPA, World.ONE, Level.FIRST, self._dispatcher
                )
            )
            self._dispatcher[SceneAction.END]()
