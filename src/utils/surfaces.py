from typing import Dict, List

from pygame import Surface

from src.enums import ElementSubType, ElementType
from src.utils.assets import (
    BIG_BUSH,
    BIG_CLOUD,
    BIG_MOUNTAIN,
    BIG_TREE,
    CASTLE,
    COIN_1,
    COIN_2,
    COIN_3,
    COIN_4,
    FLAG_PIPE,
    FLAG_STAND,
    FLAG_SUPPORT_1,
    FLAG_SUPPORT_2,
    FLAG_SUPPORT_3,
    FLAG_WIN,
    MEDIUM_BUSH,
    MEDIUM_CLOUD,
    MEDIUM_MOUNTAIN,
    MEDIUM_TREE,
    MYSTERY_BLOCK_1,
    MYSTERY_BLOCK_2,
    OVERWORLD_BLOCK,
    OVERWORLD_TERRAIN_BLOCK,
    PIPE_BODY_STYLE_1,
    PIPE_BODY_STYLE_2,
    PIPE_BODY_STYLE_3,
    PIPE_BODY_STYLE_4,
    PIPE_HEAD,
    SMALL_BUSH,
    SMALL_CLOUD,
    SMALL_MOUNTAIN,
    SMALL_TREE,
    WALL_BLOCK,
)

elements: Dict[ElementType, Dict[ElementSubType, List[Surface]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [OVERWORLD_BLOCK],
        ElementSubType.WALL_BLOCK: [WALL_BLOCK],
        ElementSubType.OVERWORLD_TERRAIN_BLOCK: [OVERWORLD_TERRAIN_BLOCK],
    },
    ElementType.MISTERY_BOX: {
        ElementSubType.DEFAULT_MISTERY_BOX: [MYSTERY_BLOCK_1, MYSTERY_BLOCK_2]
    },
    ElementType.PIPE: {
        ElementSubType.PIPE_HEAD: [PIPE_HEAD],
        ElementSubType.PIPE_BODY_STYLE_1: [PIPE_BODY_STYLE_1],
        ElementSubType.PIPE_BODY_STYLE_2: [PIPE_BODY_STYLE_2],
        ElementSubType.PIPE_BODY_STYLE_3: [PIPE_BODY_STYLE_3],
        ElementSubType.PIPE_BODY_STYLE_4: [PIPE_BODY_STYLE_4],
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
    ElementType.CASTLE: {ElementSubType.DEFAULT_CASTLE: [CASTLE]},
    ElementType.FLAG: {
        ElementSubType.FLAG_PIPE: [FLAG_PIPE],
        ElementSubType.FLAG_WIN: [FLAG_WIN],
        ElementSubType.FLAG_STAND: [FLAG_STAND],
        ElementSubType.FLAG_SUPPORT_1: [FLAG_SUPPORT_1],
        ElementSubType.FLAG_SUPPORT_2: [FLAG_SUPPORT_2],
        ElementSubType.FLAG_SUPPORT_3: [FLAG_SUPPORT_3],
    },
    ElementType.COIN: {
        ElementSubType.COIN: [COIN_1, COIN_2, COIN_3, COIN_4],
    },
}
