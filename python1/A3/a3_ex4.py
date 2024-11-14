print("Enter text (space separated): ", end='')
input_str = input()

len_to_words = {}

if input_str.strip() == '':
    len_to_words[0] = ['']
else:
    words = input_str.split()

    for word in words:
        length = len(word)
        if length not in len_to_words:
            len_to_words[length] = []
        len_to_words[length].append(word)

for length in sorted(len_to_words.keys()):
    word_list = len_to_words[length]
    count = len(word_list)

    if count == 1:
        word_plural = "word"
    else:
        word_plural = "words"

    if length == 0 and word_list == ['']:
        words_str = ''
    else:
        words_str = ', '.join(word_list)

    print(f"length {length}: {count} {word_plural} ({words_str})")