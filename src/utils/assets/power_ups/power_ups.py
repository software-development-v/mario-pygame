from ...constants import GENERAL_SIZE
from ...directories import ALCOHOL_CAIMAN_DIR, BUNUELO_DIR, PASTEL_DIR
from ..create_images import create_image

ALCOHOL_CAIMAN = create_image(
    ALCOHOL_CAIMAN_DIR + "alcohol_caiman.png", GENERAL_SIZE
)

BUNUELO = create_image(BUNUELO_DIR + "bunuelo.png", GENERAL_SIZE)

PASTEL = create_image(PASTEL_DIR + "pastel.png", GENERAL_SIZE)
