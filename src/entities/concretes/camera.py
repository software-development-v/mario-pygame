# camera.py
from typing import Any


class Camera:
    def __init__(
        self, width: int, height: int, viewport_width: int, viewport_height: int
    ) -> None:
        self.width = width
        self.height = height
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.x_offset = 0
        self.y_offset = 0

    def update(self, target: Any) -> None:
        self.x_offset = (
            -target.rect.x + self.viewport_width // 2 - target.width // 2
        )
        self.y_offset = 0

        self.x_offset = min(
            0, max(self.viewport_width - self.width, self.x_offset)
        )

    def apply(self, entity: Any) -> Any:
        return entity.rect.move(self.x_offset, self.y_offset)
