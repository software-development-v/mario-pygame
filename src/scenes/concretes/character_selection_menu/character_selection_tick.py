# character_selection_tick.py

from typing import Callable, Dict, Tuple

from pygame import mouse, time

from src.enums import GameEvent, HeroType, Level, SceneAction, World

from ...abstractions import Tick
from ..transition_level import TransitionLevelScene
from .character_selection_render import CharacterSelectionRender


class CharacterSelectionTick(Tick):
    def __init__(
        self,
        render: CharacterSelectionRender,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ) -> None:
        super().__init__(dispatcher)
        self.render = render
        self.last_switch_time = time.get_ticks()
        self.switch_delay = 100
        self.event_handlers = {
            GameEvent.UP: lambda: self.handle_character_change(-1),
            GameEvent.DOWN: lambda: self.handle_character_change(1),
            GameEvent.JUMP: self.select_character,
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
            self.select_character()
            self.last_switch_time = current_time

        if mouse.get_focused():
            self.render.handle_mouse_event(mouse_pos)
            self.render.render()

    def handle_character_change(self, direction: int) -> None:
        selected_character = self.render.get_selected_character()
        new_character = (selected_character + direction) % len(
            self.render.character_options
        )
        self.render.set_selected_character(new_character)

    def select_character(self) -> None:
        selected_character = self.render.get_selected_character()
        character_selected = self.render.character_options[selected_character]

        hero_type_map = {
            HeroType.PARIENTE.value: HeroType.PARIENTE,
            HeroType.HIJITA.value: HeroType.HIJITA,
            HeroType.CUMPA.value: HeroType.CUMPA,
        }

        # Obtener el tipo de héroe seleccionado
        selected_hero_type = hero_type_map.get(
            character_selected, HeroType.CUMPA
        )

        # Configurar la siguiente escena con el tipo de héroe seleccionado
        self._dispatcher[SceneAction.SET_NEXT_SCENE](
            TransitionLevelScene(
                selected_hero_type, World.ONE, Level.FIRST, self._dispatcher
            )
        )

        # Finalizar la escena actual
        self._dispatcher[SceneAction.END]()
