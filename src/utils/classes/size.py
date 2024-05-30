from typing import Tuple


class Size:
    def __init__(self, size: Tuple[int, int]):
        self.size = size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Size):
            return NotImplemented

        return self.size == other.size
