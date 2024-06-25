from pygame import Surface, transform

from src.utils import (
    COIN_1,
    SCREEN_WIDTH,
    WHITE_COLOR,
    get_format_number,
    get_message,
)


class LevelMetricsRenderer:
    def __init__(self, surf: Surface) -> None:
        self.surf = surf
        self.status_bar_y_pos = 20
        self.icons_size = 30

    def render(
        self,
        name: str,
        time: int,
        score: int,
        coins: int,
        world: int = 1,
        level: int = 1,
    ) -> None:
        self.character_name = name
        self.time = time
        self.score = score
        self.coins = coins
        self.world = world
        self.level = level
        self.set_status_bar()

    def set_status_bar(self) -> None:
        format_time= ""
        if self.time >= 0:
              format_time = get_format_number(self.time)

        format_score = get_format_number(self.score, 6)

        x_base = 300
        spacing = (SCREEN_WIDTH - x_base * 2) // 3

        self.set_message_box(
            f"{self.character_name}\n{format_score}",
            x_base,
            self.status_bar_y_pos,
        )
        self.set_message_box(
            f"\nx{self.coins}", x_base + (1 * spacing), self.status_bar_y_pos
        )
        self.set_message_box(
            f"WORLD\n {self.world}-{self.level}",
            x_base + (2 * spacing),
            self.status_bar_y_pos,
        )
        self.set_message_box(
            f"TIME\n {format_time}",
            x_base + (3 * spacing),
            self.status_bar_y_pos,
        )

        self.surf.blit(
            transform.scale(COIN_1, (self.icons_size, self.icons_size)),
            (
                x_base + (1 * spacing) - self.icons_size * 2.3,
                self.status_bar_y_pos + self.icons_size,
            ),
        )

    def set_message_box(self, text: str, x: int, y: int) -> None:
        message, message_rect = get_message(
            text, x, y, text_color=WHITE_COLOR, size=30
        )

        message_rect.bottom = y + message_rect.height

        self.surf.blit(message, message_rect)
