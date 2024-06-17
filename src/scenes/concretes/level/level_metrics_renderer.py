from pygame import Surface
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_format_number, get_message


class LevelMetricsRenderer:
    STATUS_BAR_WIDTH = 1600

    def __init__(self, surf: Surface) -> None:
        self.surf = surf

    def render(self, time: int, score: int, coins: int, world: int) -> None:
        self.time = time
        self.score = score
        self.coins = coins
        self.world = world
        self.set_status_bar()

    def set_status_bar(self) -> None:
        format_time = get_format_number(self.time)
        format_score = get_format_number(self.score,6)

        x_base = 300
        spacing = (self.STATUS_BAR_WIDTH - x_base * 2) // 3

        self.set_message_box(f"SCORE\n{format_score}", x_base, 35)
        self.set_message_box(f"TIME\n {format_time}", x_base + (3 * spacing), 35)

    def set_message_box(self, text: str, x: int, y: int) -> None:
        message, message_rect = get_message(
            text, x, y, text_color=WHITE_COLOR, size=30
        )

        message_rect.bottom = y + message_rect.height

        self.surf.blit(message, message_rect)
