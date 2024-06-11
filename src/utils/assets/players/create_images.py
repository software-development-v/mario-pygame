from pygame import image, transform
from typing import Text, Tuple

def create_image(path: Text, size: Tuple[int, int]):
    return transform.scale(
        image.load(path), size
    )
