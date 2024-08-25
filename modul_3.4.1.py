def single_root_words(root_word, *other_words):
    same_words = []

    root_word = root_word.lower()

    other_words_1 = list(other_words)
    other_words_2 = other_words_1.copy()

    for i in range(len(other_words_1)):
        other_words_1[i] = other_words_1[i].lower()

    for i in range(len(other_words_1)):
        if root_word in other_words_1[i]:
            same_words.append(other_words_2[i])
        elif other_words_1[i] in root_word:
            same_words.append(other_words_2[i])

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
