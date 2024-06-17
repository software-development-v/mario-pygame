from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import PIPE_BODY_DIR, PIPE_HEAD_DIR

PIPE_HEAD = transform.scale(
    image.load(PIPE_HEAD_DIR + "head.png"),
    (GENERAL_WIDTH * 2, GENERAL_HEIGHT * 2),
)

PIPE_BODY_STYLE_1 = transform.scale(
    image.load(PIPE_BODY_DIR + "style_1.png"),
    (GENERAL_WIDTH * 2, (GENERAL_HEIGHT * 2) / 2),
)

PIPE_BODY_STYLE_2 = transform.scale(
    image.load(PIPE_BODY_DIR + "style_2.png"),
    (GENERAL_WIDTH * 2, (GENERAL_HEIGHT * 2) / 2),
)

PIPE_BODY_STYLE_3 = transform.scale(
    image.load(PIPE_BODY_DIR + "style_3.png"),
    (GENERAL_WIDTH * 2, (GENERAL_HEIGHT * 2) / 2),
)

PIPE_BODY_STYLE_4 = transform.scale(
    image.load(PIPE_BODY_DIR + "style_4.png"),
    (GENERAL_WIDTH * 2, (GENERAL_HEIGHT * 2) / 2),
)
