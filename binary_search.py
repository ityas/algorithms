# бинарный поиск
def binary_search(k, nums_list):
    left = 0
    right = len(nums_list)

    while left <= right:
        middle = (left + right) // 2

        if nums_list[middle] == k:
            return middle  # возвращает индекс числа k в списке num_list
        elif nums_list[middle] > k:
            right = middle - 1
        else:
            left = middle + 1

    return -1
