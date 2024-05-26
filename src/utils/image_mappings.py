from typing import Dict, List

image_configurations: Dict[str, Dict[int, List[str]]] = {
    "Block": {
        1: [
            "block1_level1.png",
            "block2_level1.png",
            "block3_level1.png",
            "block4_level1.png",
        ],
        2: [
            "block1_level2.png",
            "block2_level2.png",
            "block3_level2.png",
            "block4_level2.png",
        ],
    },
    "MisteryBox": {
        1: [
            "mistery_box_asset_1.png",
            "mistery_box_asset_2.png",
            "mistery_box_asset_3.png",
        ]
    },
    "Castle": {1: ["castle.png"]},
    "Flag": {1: ["flag.png"]},
    "Pipe": {1: ["small_pipe.png"]},
    "Cloud": {1: ["medium_cloud.png"]},
    "Bush": {1: ["bush.png"]},
    "Mountain": {1: ["mountain.png"]},
    "Coin": {1: ["coin1.png", "coin2.png", "coin3.png", "coin4.png"]},
}
