from typing import  Any

def parse_response(text: str) -> { str, Any }:
    lines = text.strip().splitlines()

    if "Card is not inserted" in lines:
        raise Exception("Card is not inserted")
    
    data = {}
    for line in lines:
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        data[key] = value
    
    return data