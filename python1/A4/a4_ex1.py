def aggregate(*args, **kwargs):

    frequency = {}

    for key in args:
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1

    for key, value in kwargs.items():
        if key in frequency:
            frequency[key] += value
        else:
            frequency[key] = value

    return frequency

if __name__ == "__main__":
    print(aggregate())
    print(aggregate(a=5, b=10, d=4))
    print(aggregate('a', 'b', 'c', 'b', 'c'))
    print(aggregate('a', 'b', 'c', 'b', 'c', a=5, b=10, d=4))