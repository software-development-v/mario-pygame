from typing import Dict, List

image_configurations: Dict[str, Dict[str, List[str]]] = {
    "Block": {
        "overworld-block": [
            "block1_level1.png",
            "block2_level1.png",
            "block3_level1.png",
            "block4_level1.png",
        ],
        "underground-block": [
            "block1_level2.png",
            "block2_level2.png",
            "block3_level2.png",
            "block4_level2.png",
        ],
    },
    "MisteryBox": {
        "default-mistery-box": [
            "mistery_box_asset_1.png",
            "mistery_box_asset_2.png",
            "mistery_box_asset_3.png",
        ]
    },
    "Pipe": {
        "small-pipe": ["small_pipe.png"],
        "medium-pipe": ["medium_pipe.png"],
        "big-pipe": ["big_pipe.png"],
    },
    "Cloud": {
        "small-cloud": ["small_cloud.png"],
        "medium-cloud": ["medium_cloud.png"],
        "big-cloud": ["big_cloud.png"],
    },
    "Bush": {
        "small-bush": ["small_bush.png"],
        "medium-bush": ["medium_bush.png"],
        "big-bush": ["big_bush.png"],
    },
    "Castle": {"default-castle": ["castle.png"]},
    "Flag": {"default-flag": ["flag.png"]},
    "Mountain": {"default-mountain": ["mountain.png"]},
    "Coin": {
        "default-coin": ["coin1.png", "coin2.png", "coin3.png", "coin4.png"]
    },
}
