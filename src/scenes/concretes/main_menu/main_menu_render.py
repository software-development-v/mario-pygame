from typing import List, Tuple
import pygame
from src.utils.classes.button import Button
from src.utils.colors import BLACK_COLOR, ORANGE_COLOR
from src.utils.assets.fonts import GAME_FONT
from src.utils.assets.backgrounds.menu import MENU_BACKGROUND

from ...abstractions import Render


class MainMenuRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.menu_options_left = ["Quit"]
        self.menu_options_center = ["Start Game", "Saved Game"]
        self.menu_options_right = ["Settinqs"]
        self.selected_option = 0
        self.selected_section = 1

        screen_width = self._screen.get_width()
        screen_height = self._screen.get_height()

        self.background_image = MENU_BACKGROUND

        self.button_quit = Button(
            self.menu_options_left[0],
            pygame.font.Font(GAME_FONT, 30),
            (200, 140),
            ORANGE_COLOR,
            BLACK_COLOR,
        )

        option_height = 100
        self.buttons_center: List[Button] = []
        for index, option in enumerate(self.menu_options_center):
            position = (
                screen_width // 2,
                (
                    screen_height // 2
                    - (len(self.menu_options_center) // 2 * option_height)
                    + index * option_height
                )
                - 50,
            )
            button = Button(
                option,
                pygame.font.Font(GAME_FONT, 40),
                position,
                ORANGE_COLOR,
                BLACK_COLOR,
            )
            self.buttons_center.append(button)
        self.button_options = Button(
            self.menu_options_right[0],
            pygame.font.Font(GAME_FONT, 25),
            (1400, 140),
            ORANGE_COLOR,
            BLACK_COLOR,
        )

    def render(
        self,
    ) -> None:
        self._screen.blit(self.background_image, (0, 0))
        self.button_quit.render(self._screen, self.selected_section == 0)
        for index, button in enumerate(self.buttons_center):
            button.render(
                self._screen,
                self.selected_section == 1 and index == self.selected_option,
            )
        self.button_options.render(self._screen, self.selected_section == 2)
        pygame.display.flip()

    def get_selected_option(self) -> int:
        if self.selected_section == 0:
            return 0
        elif self.selected_section == 1:
            return self.selected_option
        elif self.selected_section == 2:
            return 0
        else:
            return 0

    def set_selected_option(self, option: int):
        if self.selected_section == 1:
            self.selected_option = option % len(self.menu_options_center)

    def handle_mouse_event(self, mouse_pos: Tuple[int, int]) -> bool:
        if (
            self.button_quit.is_hovered(mouse_pos)
            and self.selected_section == 0
        ):
            self.selected_option = 0
            return True

        if (
            self.button_options.is_hovered(mouse_pos)
            and self.selected_section == 2
        ):
            self.selected_option = 0
            return True

        if self.selected_section == 1:
            for index, button in enumerate(self.buttons_center):
                if button.is_hovered(mouse_pos):
                    self.selected_option = index
                    return True

        return False

    def set_selected_section(self, section: int):
        self.selected_section = section
        self.selected_option = 0

    def switch_section(self, direction: int):
        if direction == -1:
            self.selected_section = max(self.selected_section - 1, 0)
        elif direction == 1:
            self.selected_section = min(self.selected_section + 1, 2)
        self.selected_option = 0
