from typing import Dict, List

from pygame import Surface

from src.enums import ElementSubType, ElementType
from src.utils.assets import (
    BIG_CLOUD,
    MEDIUM_CLOUD,
    SMALL_CLOUD,
    OVERWORLD_BLOCK,
    OVERWORLD_BRICK,
    OVERWORLD_BROKE_BRICK,
    MASTERY_BLOCK_1,
    MASTERY_BLOCK_2,
    PIPE_BODY_STYLE_1,
    PIPE_BODY_STYLE_2,
    PIPE_BODY_STYLE_3,
    PIPE_BODY_STYLE_4,
    PIPE_HEAD,
    COIN_1,
    COIN_2,
    COIN_3,
    COIN_4,
)

elements: Dict[ElementType, Dict[ElementSubType, List[Surface]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [OVERWORLD_BLOCK],
        ElementSubType.UNDERGROUND_BLOCK: [],
        ElementSubType.OVERWORLD_BRICK: [OVERWORLD_BRICK],
        ElementSubType.OVERWORLD_BROKE_BRICK: [OVERWORLD_BROKE_BRICK],
    },
    ElementType.CLOUD: {
        ElementSubType.SMALL_CLOUD: [SMALL_CLOUD],
        ElementSubType.MEDIUM_CLOUD: [MEDIUM_CLOUD],
        ElementSubType.BIG_CLOUD: [BIG_CLOUD],
    },
    ElementType.PIPE: {
        ElementSubType.PIPE_HEAD: [PIPE_HEAD],
        ElementSubType.PIPE_BODY: [
            PIPE_BODY_STYLE_1,
            PIPE_BODY_STYLE_2,
            PIPE_BODY_STYLE_3,
            PIPE_BODY_STYLE_4,
        ],
    },
    ElementType.BUSH: {
        ElementSubType.SMALL_BUSH: [],
        ElementSubType.MEDIUM_BUSH: [],
        ElementSubType.BIG_BUSH: [],
    },
    ElementType.CASTLE: {ElementSubType.DEFAULT_CASTLE: []},
    ElementType.FLAG: {ElementSubType.DEFAULT_FLAG: []},
    ElementType.MOUNTAIN: {ElementSubType.DEFAULT_MOUNTAIN: []},
    ElementType.MISTERY_BOX: {
        ElementSubType.MASTERY_BLOCK: [MASTERY_BLOCK_1, MASTERY_BLOCK_2]
    },
    ElementType.COIN: {ElementSubType.COIN: [COIN_1, COIN_2, COIN_3, COIN_4]}
}
