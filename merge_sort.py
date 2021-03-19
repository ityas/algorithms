# сортировка слиянием
def merge_sort(nums_list):
    def merge(left_list, right_list):
        sorted_list = []

        left_list_index = right_list_index = 0
        left_list_len, right_list_len = len(left_list), len(right_list)

        for _ in range(left_list_len + right_list_len):
            # сортируем до остатка
            if left_list_index < left_list_len and right_list_index < right_list_len:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # соединяем остаток
            elif left_list_index == left_list_len:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_len:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    if len(nums_list) <= 1:
        return nums_list

    middle = len(nums_list) // 2
    return merge(merge_sort(nums_list[:middle]), merge_sort(nums_list[middle:]))
