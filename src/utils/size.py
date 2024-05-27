class Size:
    def __init__(self, width: float = 0, height: float = 0):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Size(width={self.width}, height={self.height})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Size):
            return NotImplemented
        return self.width == other.width and self.height == other.height
