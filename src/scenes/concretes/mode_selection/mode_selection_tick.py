from typing import Callable, Dict, Tuple
import pygame
from src.enums import GameEvent, SceneAction, HeroType, Level, World

from ...interfaces import IScene, ITick
from ..transition_level import TransitionLevelScene
from .mode_selection_render import ModeSelectionSceneRender


class ModeSelectionSceneTick(ITick):
    def __init__(self, render: "ModeSelectionSceneRender") -> None:
        self.render = render

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        selected_option = self.render.get_selected_option()
        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if game_events.get(GameEvent.UP):
            if self.render.selected_section == 1:
                self.render.set_selected_option(selected_option - 1)
        elif game_events.get(GameEvent.DOWN):
            if self.render.selected_section == 1:
                self.render.set_selected_option(selected_option + 1)
        elif game_events.get(GameEvent.LEFT):
            self.render.switch_section(-1)
        elif game_events.get(GameEvent.RIGHT):
            self.render.switch_section(1)
        elif game_events.get(GameEvent.JUMP):
            self.select_option(set_next_scene, dispatcher)

        if self.render.handle_mouse_event(mouse_pos) and mouse_click[0]:
            self.select_option(set_next_scene, dispatcher)

    def select_option(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ):
        selected_option = self.render.get_selected_option()
        selected_section = self.render.selected_section

        if selected_section == 0:
            selected = self.render.menu_options_left[selected_option]
        elif selected_section == 1:
            selected = self.render.menu_options_center[selected_option]
        elif selected_section == 2:
            selected = self.render.menu_options_right[selected_option]

        if selected == "Quit":  # type: ignore
            pygame.quit()
            exit()
        else:
            set_next_scene(
                TransitionLevelScene(HeroType.CUMPA, World.ONE, Level.FIRST)
            )
            dispatcher[SceneAction.END]()
