from pygame import image, transform
from typing import Text, Tuple

def create_image(path: Text, size: Tuple[float, float]):
    return transform.scale(
        image.load(path), size
    )
