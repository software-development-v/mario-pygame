from typing import Dict, List

from pygame import Surface

from src.enums import ElementSubType, ElementType
from src.utils.assets import (
    BIG_BUSH,
    MEDIUM_BUSH,
    SMALL_BUSH,
    BIG_CLOUD,
    MEDIUM_CLOUD,
    SMALL_CLOUD,
    BIG_MOUNTAIN,
    MEDIUM_MOUNTAIN,
    SMALL_MOUNTAIN,
    BIG_TREE,
    MEDIUM_TREE,
    SMALL_TREE,
    OVERWORLD_BLOCK,
    WALL_BLOCK,
    MYSTERY_BLOCK,
    PIPE_HEAD,
    PIPE_BODY,
    CASTLE,
    FLAG_STAND,
    FLAG_PIPE,
    FLAG_WIN,
    FLAG_SUPPORT_2
)

elements: Dict[ElementType, Dict[ElementSubType, List[Surface]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [OVERWORLD_BLOCK],
        ElementSubType.WALL_BLOCK: [WALL_BLOCK],
        ElementSubType.UNDERGROUND_BLOCK: [],
    },
    ElementType.MISTERY_BOX: {
        ElementSubType.DEFAULT_MISTERY_BOX: [MYSTERY_BLOCK]
    },
    ElementType.PIPE: {
        ElementSubType.PIPE_HEAD: [PIPE_HEAD],
        ElementSubType.PIPE_BODY: [PIPE_BODY],
    },
    ElementType.CLOUD: {
        ElementSubType.SMALL_CLOUD: [SMALL_CLOUD],
        ElementSubType.MEDIUM_CLOUD: [MEDIUM_CLOUD],
        ElementSubType.BIG_CLOUD: [BIG_CLOUD],
    },
    ElementType.BUSH: {
        ElementSubType.SMALL_BUSH: [SMALL_BUSH],
        ElementSubType.MEDIUM_BUSH: [MEDIUM_BUSH],
        ElementSubType.BIG_BUSH: [BIG_BUSH],
    },
    ElementType.MOUNTAIN: {
        ElementSubType.SMALL_MOUNTAIN: [SMALL_MOUNTAIN],
        ElementSubType.MEDIUM_MOUNTAIN: [MEDIUM_MOUNTAIN],
        ElementSubType.BIG_MOUNTAIN: [BIG_MOUNTAIN],
    },
    ElementType.TREE: {
        ElementSubType.SMALL_TREE: [SMALL_TREE],
        ElementSubType.MEDIUM_TREE: [MEDIUM_TREE],
        ElementSubType.BIG_TREE: [BIG_TREE],
    },
    ElementType.CASTLE: {
        ElementSubType.DEFAULT_CASTLE: [CASTLE]
    },
    ElementType.FLAG: {
        ElementSubType.FLAG_PIPE: [FLAG_PIPE],
        ElementSubType.FLAG_WIN: [FLAG_WIN],
        ElementSubType.FLAG_STAND: [FLAG_STAND],
        ElementSubType.FLAG_SUPPORT: [FLAG_SUPPORT_2],
    },
    ElementType.COIN: {ElementSubType.DEFAULT_COIN: []},
}



