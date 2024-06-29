from pygame import Surface

from src.entities.concretes.elements.touchable.coin import Coin
from src.utils import SCREEN_WIDTH, get_format_number, get_message
from src.utils.classes.position import Position


class LevelMetricsRenderer:
    def __init__(self, surf: Surface) -> None:
        self.surf = surf
        self.status_bar_y_pos = 20
        self.icons_size = 30
        self.x_base = 300
        self.spacing = (SCREEN_WIDTH - self.x_base * 2) // 3
        self.coin = Coin(
            Position(
                int(self.x_base + (1 * self.spacing) - self.icons_size * 2.6),
                self.status_bar_y_pos + self.icons_size,
            )
        )

    def render(
        self,
        name: str,
        time: int,
        score: int,
        coins: int,
        world: int = 1,
        level: int = 1,
    ) -> None:
        format_time = ""
        if time >= 0:
            format_time = get_format_number(time)

        format_score = get_format_number(score, 6)
        format_coin = get_format_number(coins, 2)

        self.set_message_box(
            f"{name}\n{format_score}",
            self.x_base,
            self.status_bar_y_pos,
        )
        self.set_message_box(
            f"\nx{format_coin}",
            self.x_base + (1 * self.spacing),
            self.status_bar_y_pos,
        )
        self.set_message_box(
            f"WORLD\n {world}-{level}",
            self.x_base + (2 * self.spacing),
            self.status_bar_y_pos,
        )
        self.set_message_box(
            f"TIME\n {format_time}",
            self.x_base + (3 * self.spacing),
            self.status_bar_y_pos,
        )

        self.coin.animate()
        self.coin.draw(self.surf)



    def set_message_box(self, text: str, x: int, y: int) -> None:
        message, message_rect = get_message(text, x, y)

        message_rect.bottom = y + message_rect.height

        self.surf.blit(message, message_rect)
