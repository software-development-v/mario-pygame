from pygame import Surface

from src.entities import CoinIcon
from src.utils import SCREEN_WIDTH, get_format_number, get_message
from src.utils.classes.position import Position
from src.utils.constants import METRICS_BAR_POS_Y, SMALL_SIZE, METRICS_BAR_POS_X


class LevelMetricsRenderer:
    def __init__(self) -> None:
        self.__status_bar_y_pos = METRICS_BAR_POS_Y
        self.__icons_size = SMALL_SIZE[0]
        self.__x_base = METRICS_BAR_POS_X
        self.__spacing = (SCREEN_WIDTH - self.__x_base * 2) // 3
        self.__coin = CoinIcon(
            Position(
                int(
                    self.__x_base
                    + (1 * self.__spacing)
                    - self.__icons_size * 2.6
                ),
                self.__status_bar_y_pos + self.__icons_size,
            )
        )

    def render(
        self,
        surf: Surface,
        name: str,
        time: int,
        score: int,
        coins: int,
        world: int,
        level: int,
    ) -> None:

        format_time = ""
        if time >= 0:
            format_time = get_format_number(time)
        format_score = get_format_number(score, 6)
        format_coin = get_format_number(coins, 2)

        self.__render_messages(
            surf,
            [
                f"{name}\n{format_score}",
                f"\nx{format_coin}",
                f"WORLD\n {world}-{level}",
                f"TIME\n {format_time}",
            ],

        )
        self.__coin.draw(surf)

    def __render_messages(self, surf: Surface, messages: list[str]) -> None:
        x = self.__x_base
        y = self.__status_bar_y_pos
        index = 1
        for message in messages:
            message, message_rect = get_message(message, x, y)
            message_rect.bottom = y + message_rect.height
            surf.blit(message, message_rect)
            x = self.__x_base + (index * self.__spacing)
            index += 1
