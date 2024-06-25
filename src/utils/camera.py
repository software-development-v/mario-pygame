from typing import Any


class Camera:
    def __init__(
        self,
        width: int,
        height: int,
        viewport_width: int,
        viewport_height: int,
        threshold: int,
    ) -> None:
        self.width = width
        self.height = height
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.threshold = threshold
        self.x_offset = 0
        self.y_offset = 0
        self.last_x_offset = 0

    def update(self, target: Any) -> None:
        hero_center_x = target.rect.x + target.width // 2

        if hero_center_x > self.threshold:
            self.x_offset = -hero_center_x + self.threshold

            if self.x_offset > self.last_x_offset:
                self.x_offset = self.last_x_offset

        self.last_x_offset = self.x_offset
        self.y_offset = 0

        self.x_offset = min(
            0, max(self.viewport_width - self.width, self.x_offset)
        )

    def apply(self, entity: Any) -> Any:
        return entity.rect.move(self.x_offset, self.y_offset)

    def get_left_edge(self) -> int:
        return -self.x_offset
