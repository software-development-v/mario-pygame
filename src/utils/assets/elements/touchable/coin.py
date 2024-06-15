from pygame import image, transform

from src.utils.constants import GENERAL_SIZE
from src.utils.directories import COIN_DIR

COIN_1 = transform.scale(
    image.load(COIN_DIR + "coin_1.png"), GENERAL_SIZE
)

COIN_2 = transform.scale(
    image.load(COIN_DIR + "coin_2.png"), GENERAL_SIZE
)

COIN_3 = transform.scale(
    image.load(COIN_DIR + "coin_3.png"), GENERAL_SIZE
)

COIN_4 = transform.scale(
    image.load(COIN_DIR + "coin_4.png"), GENERAL_SIZE
)
