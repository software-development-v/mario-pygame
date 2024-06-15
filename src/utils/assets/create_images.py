from typing import Text, Tuple

from pygame import image, transform


def create_image(path: Text, size: Tuple[float, float]):
    return transform.scale(image.load(path), size)
