#!/usr/bin/python3

def class_to_json(obj):
    """Converts an object to a JSON serializable dictionary."""
    if isinstance(obj, dict):
        return {k: class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    else:
        attributes = {}
        for attr in dir(obj):
            if not attr.startswith('__') and not callable(getattr(obj, attr)):
                attributes[attr] = class_to_json(getattr(obj, attr))
        return attributes
