from typing import Dict, List

from src.enums import ElementSubType, ElementType

image_mappings: Dict[ElementType, Dict[ElementSubType, List[str]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [
            "block1_level1.png",
            "block2_level1.png",
            "block3_level1.png",
            "block4_level1.png",
        ],
        ElementSubType.UNDERGROUND_BLOCK: [
            "block1_level2.png",
            "block2_level2.png",
            "block3_level2.png",
            "block4_level2.png",
        ],
    },
    ElementType.MISTERY_BOX: {
        ElementSubType.DEFAULT_MISTERY_BOX: [
            "mistery_box_asset_1.png",
            "mistery_box_asset_2.png",
            "mistery_box_asset_3.png",
        ]
    },
    ElementType.PIPE: {
        ElementSubType.SMALL_PIPE: ["small_pipe.png"],
        ElementSubType.MEDIUM_PIPE: ["medium_pipe.png"],
        ElementSubType.BIG_PIPE: ["big_pipe.png"],
    },
    ElementType.CLOUD: {
        ElementSubType.SMALL_CLOUD: ["small_cloud.png"],
        ElementSubType.MEDIUM_CLOUD: ["medium_cloud.png"],
        ElementSubType.BIG_CLOUD: ["big_cloud.png"],
    },
    ElementType.BUSH: {
        ElementSubType.SMALL_BUSH: ["small_bush.png"],
        ElementSubType.MEDIUM_BUSH: ["medium_bush.png"],
        ElementSubType.BIG_BUSH: ["big_bush.png"],
    },
    ElementType.CASTLE: {ElementSubType.DEFAULT_CASTLE: ["castle.png"]},
    ElementType.FLAG: {ElementSubType.DEFAULT_FLAG: ["flag.png"]},
    ElementType.MOUNTAIN: {ElementSubType.DEFAULT_MOUNTAIN: ["mountain.png"]},
    ElementType.COIN: {
        ElementSubType.DEFAULT_COIN: [
            "coin1.png",
            "coin2.png",
            "coin3.png",
            "coin4.png",
        ]
    },
}
