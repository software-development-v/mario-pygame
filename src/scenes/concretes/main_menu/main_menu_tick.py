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
        super().__init__(dispatcher)
        self.render = render
        self.last_switch_time = pygame.time.get_ticks()
        self.switch_delay = 100
        self.event_handlers = {
            GameEvent.UP: lambda: self.handle_option_change(-1),
            GameEvent.DOWN: lambda: self.handle_option_change(1),
            GameEvent.LEFT: self.handle_left_right,
            GameEvent.RIGHT: self.handle_left_right,
            GameEvent.JUMP: self.handle_jump,
        }

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        current_time = pygame.time.get_ticks()

        if current_time - self.last_switch_time > self.switch_delay:
            for event, handler in self.event_handlers.items():
                if game_events.get(event):
                    handler()
                    self.last_switch_time = current_time
                    break

        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0] and self.render.handle_mouse_event(mouse_pos):
            self.select_option(self._dispatcher)
            self.last_switch_time = current_time

        if pygame.mouse.get_focused():
            self.render.handle_mouse_event(mouse_pos)
            self.render.render()

    def handle_option_change(self, direction: int) -> None:
        selected_option = self.render.get_selected_option()
        new_option = (selected_option + direction) % 3
        self.render.set_selected_option(new_option)

    def handle_left_right(self) -> None:
        selected_option = self.render.get_selected_option()
        if selected_option == 2:
            self.render.set_selected_option(0)
        else:
            self.render.set_selected_option(2)

    def handle_jump(self) -> None:
        self.select_option(self._dispatcher)

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
