from typing import Dict, List

from src.enums import ElementSubType, ElementType

image_mappings: Dict[ElementType, Dict[ElementSubType, List[str]]] = {
    ElementType.BLOCK: {
        ElementSubType.OVERWORLD_BLOCK: [
            "assets/elements/touchable/block/floor.png",
            "assets/elements/touchable/block/floor.png",
            "assets/elements/touchable/block/floor.png",
            "assets/elements/touchable/block/floor.png",
        ],
        ElementSubType.UNDERGROUND_BLOCK: [
            "assets/elements/touchable/block/floor.png",
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
        ElementSubType.SMALL_PIPE: ["assets/elements/touchable/pipe/small_pipe.png"],
        ElementSubType.MEDIUM_PIPE: ["assets/elements/touchable/pipe/medium_pipe.png"],
        ElementSubType.BIG_PIPE: ["assets/elements/touchable/pipe/big_pipe.png"],
    },
    ElementType.CLOUD: {
        ElementSubType.SMALL_CLOUD: ["assets/elements/non_touchable/cloud/small_cloud.png"],
        ElementSubType.MEDIUM_CLOUD: ["assets/elements/non_touchable/cloud/medium_cloud.png"],
        ElementSubType.BIG_CLOUD: ["assets/elements/non_touchable/cloud/big_cloud.png"],
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
