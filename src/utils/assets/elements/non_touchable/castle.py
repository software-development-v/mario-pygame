from pygame import image, transform

from src.utils.directories import CASTLE_DIR

CASTLE = transform.scale(
    image.load(CASTLE_DIR + "motel.png"), (500, 250)
)
