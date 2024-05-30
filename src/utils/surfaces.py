from typing import Dict, List

from pygame import Surface

from src.enums import ElementSubType, ElementType
from src.utils.assets import (
    BIG_CLOUD,
    BIG_PIPE,
    MEDIUM_CLOUD,
    MEDIUM_PIPE,
    OVERWORLD_BLOCK,
    SMALL_CLOUD,
    SMALL_PIPE,
)

elements: Dict[ElementType, Dict[ElementSubType, List[Surface]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [OVERWORLD_BLOCK],
        ElementSubType.UNDERGROUND_BLOCK: [],
    },
    ElementType.MISTERY_BOX: {ElementSubType.DEFAULT_MISTERY_BOX: []},
    ElementType.PIPE: {
        ElementSubType.SMALL_PIPE: [SMALL_PIPE],
        ElementSubType.MEDIUM_PIPE: [MEDIUM_PIPE],
        ElementSubType.BIG_PIPE: [BIG_PIPE],
    },
    ElementType.CLOUD: {
        ElementSubType.SMALL_CLOUD: [SMALL_CLOUD],
        ElementSubType.MEDIUM_CLOUD: [MEDIUM_CLOUD],
        ElementSubType.BIG_CLOUD: [BIG_CLOUD],
    },
    ElementType.BUSH: {
        ElementSubType.SMALL_BUSH: [],
        ElementSubType.MEDIUM_BUSH: [],
        ElementSubType.BIG_BUSH: [],
    },
    ElementType.CASTLE: {ElementSubType.DEFAULT_CASTLE: []},
    ElementType.FLAG: {ElementSubType.DEFAULT_FLAG: []},
    ElementType.MOUNTAIN: {ElementSubType.DEFAULT_MOUNTAIN: []},
    ElementType.COIN: {ElementSubType.DEFAULT_COIN: []},
}
