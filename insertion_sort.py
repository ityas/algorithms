# сортировка вставками
def insertion_sort(nums_list):
    n = len(nums_list)

    for i in range(2, n):
        j = i
        # добавление нового элемента на свое место в массиве
        while j >= 1 and nums_list[j] < nums_list[j - 1]:
            nums_list[j], nums_list[j - 1] = nums_list[j - 1], nums_list[j]
            j -= 1

    return nums_list
