from ....constants import FLAG_SIZE, FLAG_SUPPORT_SIZE, PIPE_FLAG_SIZE
from ....directories import FLAG_PIPE_DIR, FLAG_SUPPORT_DIR, FLAG_WIN_DIR
from ...create_images import create_image

FLAG_PIPE = create_image(FLAG_PIPE_DIR + "flag_pipe.png", PIPE_FLAG_SIZE)

FLAG_WIN = create_image(FLAG_WIN_DIR + "flag_win.png", FLAG_SIZE)

FLAG_SUPPORT = create_image(FLAG_SUPPORT_DIR + "support.png", FLAG_SUPPORT_SIZE)
