from typing import Callable, Dict

from pygame import time

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
            GameEvent.LEFT: lambda: self.handle_character_change(-1),
            GameEvent.RIGHT: lambda: self.handle_character_change(1),
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
            HeroType.CUMPA.value: HeroType.CUMPA,
            HeroType.HIJITA.value: HeroType.HIJITA,
            HeroType.PARIENTE.value: HeroType.PARIENTE,
        }

        selected_hero_type = hero_type_map.get(
            character_selected, HeroType.CUMPA
        )

        self._dispatcher[SceneAction.SET_NEXT_SCENE](
            TransitionLevelScene(
                selected_hero_type, World.ONE, Level.FIRST, self._dispatcher
            )
        )

        self._dispatcher[SceneAction.END]()
