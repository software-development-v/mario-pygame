from ....constants import BIG_SIZE, PIPE_HEAD_SIZE
from ....directories import PIPE_BODY_DIR, PIPE_HEAD_DIR
from ...create_images import create_image

PIPE_HEAD_SMALL = create_image(PIPE_HEAD_DIR + "head_small.png", PIPE_HEAD_SIZE)

PIPE_HEAD_BIG = create_image(PIPE_HEAD_DIR + "head_big.png", BIG_SIZE)

PIPE_BODY_STYLE_1 = create_image(PIPE_BODY_DIR + "style_1.png", BIG_SIZE)

PIPE_BODY_STYLE_2 = create_image(PIPE_BODY_DIR + "style_2.png", BIG_SIZE)

PIPE_BODY_STYLE_3 = create_image(PIPE_BODY_DIR + "style_3.png", BIG_SIZE)

PIPE_BODY_STYLE_4 = create_image(PIPE_BODY_DIR + "style_4.png", BIG_SIZE)

PIPE_BODY_STYLE_5 = create_image(PIPE_BODY_DIR + "style_5.png", BIG_SIZE)
