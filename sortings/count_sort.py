# сортировка подсчетом(поразрядная сортировка)
def count_sort(nums_list):
    n = max(nums_list) + 1
    count_list = [0] * n

    for x in nums_list:
        count_list[x] += 1

    nums_list[:] = []
    for number in range(n):
        nums_list += [number] * count_list[number]

    return count_list
