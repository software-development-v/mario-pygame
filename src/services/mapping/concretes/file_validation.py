from typing import Any, Dict


def validate_level_data(data: Dict[str, Any]):
    required_fields = ["level", "world", "time", "background","background_music", "start_player_position", "enemies", "elements", "power_ups"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing '{field}' field in level data")

    validate_field_type(data["level"], str, "level")
    validate_field_type(data["world"], str, "world")
    validate_field_type(data["time"], int, "time", positive=True)
    validate_background(data["background"])
    validate_field_type(data["background_music"], str, "background_music")

    validate_start_player_position(data["start_player_position"])
    validate_list_of_entitie_dicts(data["enemies"], "enemies")
    validate_list_of_entitie_dicts(data["elements"], "elements")
    validate_list_of_entitie_dicts(data["power_ups"], "power_ups")


def validate_field_type(value: Any, expected_type: type, field_name: str, positive: bool = False):
    if not isinstance(value, expected_type):
        raise ValueError(f"Invalid '{field_name}' field: must be a {expected_type.__name__}")
    if positive and value <= 0:
        raise ValueError(f"Invalid '{field_name}' field: must be a positive {expected_type.__name__}")


def validate_background(background: Dict[str, Any]):
    validate_field_type(background, dict, "background")
    validate_field_type(background.get("type"), str, "background['type']")
    if background["type"] == "COLOR":
        validate_field_type(background.get("resource"), list, "background['resource']")
        if len(background["resource"]) != 3:
            raise ValueError("Invalid 'background' field: 'resource' must be a list with 3 elements")
        if any(value < 0 or value > 255 for value in background["resource"]):
            raise ValueError("Invalid 'background' field: 'resource' must be a list with values between 0 and 255")
    else:
        raise ValueError("Invalid 'background' field: 'type' must be a valid background type")


def validate_start_player_position(start_player_position: Dict[str, Any]):
    validate_field_type(start_player_position, dict, "start_player_position")
    validate_field_type(start_player_position.get("x"), int, "start_player_position['x']", positive=True)
    validate_field_type(start_player_position.get("y"), int, "start_player_position['y']", positive=True)


def validate_element(element: Dict[str, Any]):
    validate_field_type(element["position"], list, "position")
    if len(element["position"]) != 2:
        raise ValueError("Invalid 'position' field: must be a list with 2 elements")
    validate_field_type(element["position"][0], int, "position[0]", positive=False)
    validate_field_type(element["position"][1], int, "position[1]", positive=False)
    validate_field_type(element["type"], str, "type")
    validate_field_type(element["subtype"], str, "subtype")


def validate_list_of_entitie_dicts(lst: Dict[str, Any], field_name: str):
    validate_field_type(lst, list, field_name)
    for idx, item in enumerate(lst, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Invalid '{field_name}' field: element at index {idx} must be a dictionary")
        else:
            validate_element(item)
