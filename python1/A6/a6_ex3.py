def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            # If the value is a dictionary, recurse into it
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            # If the value is not a dictionary, just add it
            items.append((new_key, v))
    return dict(items)