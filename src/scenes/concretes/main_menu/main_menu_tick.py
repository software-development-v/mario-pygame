from typing import Callable, Dict, Tuple

from pygame import mouse, quit, time

from src.enums import GameEvent, HeroType, Level, SceneAction, World

from ...abstractions import Tick
from .main_menu_render import MainMenuRender


class MainMenuTick(Tick):
    def __init__(
        self,
        render: MainMenuRender,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ) -> None:
        super().__init__(dispatcher)
        self.render = render
        self.last_switch_time = time.get_ticks()
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
        current_time = time.get_ticks()

        if current_time - self.last_switch_time > self.switch_delay:
            for event, handler in self.event_handlers.items():
                if game_events.get(event):
                    handler()
                    self.last_switch_time = current_time
                    break

        mouse_pos: Tuple[int, int] = mouse.get_pos()
        mouse_click = mouse.get_pressed()

        if mouse_click[0] and self.render.handle_mouse_event(mouse_pos):
            self.select_option()
            self.last_switch_time = current_time

        if mouse.get_focused():
            self.render.handle_mouse_event(mouse_pos)
            self.render.render()

    def handle_option_change(self, direction: int) -> None:
        selected_option = self.render.get_selected_option()
        new_option = (selected_option + direction) % 2
        self.render.set_selected_option(new_option)

    def handle_left_right(self) -> None:
        selected_option = self.render.get_selected_option()
        self.render.set_selected_option(1 if selected_option == 0 else 0)

    def handle_jump(self) -> None:
        self.select_option()

    def select_option(self):
        selected_option = self.render.get_selected_option()
        selected = self.render.menu_options[selected_option]

        if selected == "Quit":
            quit()
            exit()
        else:
            from ..transition_level import TransitionLevelScene
            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                TransitionLevelScene(
                    HeroType.CUMPA, World.ONE, Level.FIRST, self._dispatcher
                )
            )
            self._dispatcher[SceneAction.END]()
