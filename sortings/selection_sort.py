# сортировка выбором
def selection_sort(nums_list):
    n = len(nums_list)

    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums_list[j] < nums_list[min_index]:
                min_index = j

        nums_list[i], nums_list[min_index] = nums_list[min_index], nums_list[i]

    return nums_list
