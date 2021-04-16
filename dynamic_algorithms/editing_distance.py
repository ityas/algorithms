# расстояние редактирования
def editing_distance(first_word, second_word):
    if len(first_word) == 0 or len(second_word) == 0:
        return max(len(second_word), len(first_word))

    second_array = list(range(len(first_word) + 1))
    current_array = [1] + [0] * len(first_word)

    for i in range(1, len(second_word) + 1):
        for k in range(1, len(first_word) + 1):
            current_array[k] = min(second_array[k] + 1, (second_array[k - 1] + int(first_word[k - 1] != second_word[i - 1])),
                                   current_array[k - 1] + 1)

        second_array = current_array
        current_array = [i + 1] + [0] * len(first_word)

    count = second_array[len(first_word)]
    return count
