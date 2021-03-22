# быстрая сортировка
def quick_sort(nums_list):
    def partition(nums_list, low, high):
        m = nums_list[((low + high) // 2)]  # опорный элемент
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while nums_list[i] < m:
                i += 1

            j -= 1
            while nums_list[j] > m:
                j -= 1

            if i >= j:
                return j

            # если элемент с индексом i(слева от опорного) больше, чем элемент с индексом j(справа от опорного)
            nums_list[i], nums_list[j] = nums_list[j], nums_list[i]

    def sort(nums_list, low, high):
        if low < high:
            m = partition(nums_list, low, high)
            sort(nums_list, low, m)
            sort(nums_list, m + 1, high)

            return nums_list

    return sort(nums_list, 0, len(nums_list) - 1)
