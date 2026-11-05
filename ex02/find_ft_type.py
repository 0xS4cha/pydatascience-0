from typing import Any

TYPE_NAMES = {
    list: "List",
    tuple: "Tuple",
    set: "Set",
    dict: "Dict",
}


def all_thing_is_obj(object: Any) -> int:
    obj_type = type(object)

    if obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    elif obj_type in TYPE_NAMES:
        print(f"{TYPE_NAMES[obj_type]} : {obj_type}")
    else:
        print("Type not found")

    return 42