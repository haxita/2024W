def power_set(L):
    # L is empty, return empty subset
    if not L:
        return {()}

    # Recursive case: get the power set of the list excluding the first element
    rest_power_set = power_set(L[1:])

    # For each subset of the rest, create a new subset including the first element of L
    current_power_set = {subset for subset in rest_power_set}
    for subset in rest_power_set:
        current_power_set.add(tuple(sorted((L[0],) + subset)))

    return current_power_set