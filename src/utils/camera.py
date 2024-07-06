from pygame import Rect

from .constants import SCREEN_INIT_POSITION


class Camera:
    def __init__(
        self,
        width: int,
        viewport_width: int,
        threshold: int,
    ) -> None:
        self.width = width
        self.viewport_width = viewport_width
        self.threshold = threshold
        self.x_offset = 0
        self.last_x_offset = 0

    def reset(self, x_rect: int) -> None:
        self.x_offset = -x_rect + SCREEN_INIT_POSITION
        self.last_x_offset = -x_rect + SCREEN_INIT_POSITION

    def update(self, x_rect: int, width: int) -> None:
        hero_center_x = x_rect + width // 2

        if hero_center_x > self.threshold:
            self.x_offset = -hero_center_x + self.threshold

            if self.x_offset > self.last_x_offset:
                self.x_offset = self.last_x_offset

        self.last_x_offset = self.x_offset

        self.x_offset = min(
            0, max(self.viewport_width - self.width, self.x_offset)
        )

    def apply(self, rect: Rect) -> Rect:
        return rect.move(self.x_offset, 0)

    def get_left_edge(self) -> int:
        return -self.x_offset
