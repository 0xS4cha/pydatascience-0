from typing import Any
table = {
    str(None): "Nothing",
    str(float("NaN")): "Cheese",
    str(0): "Zero",
    "": "Empty",
    str(False): "Fake"
}

def NULL_not_found(object: Any) -> int:
    try: 
        print(f"{table[str(object)]}: {object} {type(object)}")
    except KeyError:
        print("Type not Found")