# возвращает индекс числа k в списке n
def binary_search(k, num_list):
    left = 0
    right = len(num_list)

    while left <= right:
        middle = (left + right) // 2

        if num_list[middle] == k:
            return middle
        elif num_list[middle] > k:
            right = middle - 1
        else:
            left = middle + 1

    return -1
