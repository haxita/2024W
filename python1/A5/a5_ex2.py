def safe_lookup(d, keys, expected_type):
    try:
        current = d
        for key in keys:
            current = current[key]
        if not isinstance(current, expected_type):
            raise TypeError(f"Expected type {expected_type.__name__}, but got {type(current).__name__}")
        return current
    except KeyError:
        return "Key not found"