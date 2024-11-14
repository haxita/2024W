elements = []

while True:
    print("Enter element or 'x' when done: ", end='')
    elem = input()

    if elem == 'x':
        break
    else:
        elements.append(elem)

print("All: ", elements)

n = len(elements)

split_index = n // 2

first_half = elements[:split_index]
second_half = elements[split_index:]

print("First half: ", first_half)

print("Second half: ", second_half)

common_words = sorted(set(first_half) & set(second_half))

print("Sorted common words: ", common_words)