def numerical_sequence():
    i = 1
    current_sum = 0
    while True:
        current_sum += i
        yield current_sum
        i += 1
