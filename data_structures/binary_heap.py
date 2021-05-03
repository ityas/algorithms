# heap должен быть списком

def insert(heap, elem):  # добавление элемента
    heap.append(elem)
    sift(heap)


def extract_min(heap):  # возвращение минимального элемента
    return heap[0]


def remove(heap, index_elem):  # удаление элемента
    del heap[index_elem]
    sift(heap)


def change_elem(heap, index_elem, new_value):  # изменение элемента
    heap[index_elem] = new_value
    sift(heap)


def sift(nums_list):
    def heapify(heap, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # если левый потомок больше, чем текущий наибольший и имеет допустимый индекс
        if left_child < heap_size and heap[left_child] > heap[largest]:
            largest = left_child

        # если правый потомок больше, чем текущий наибольший и имеет допустимый индекс
        if right_child < heap_size and heap[right_child] > heap[largest]:
            largest = right_child

        # если наибольший элемент уже не корневой, они меняются местами
        if largest != root_index:
            heap[root_index], heap[largest] = heap[largest], heap[root_index]
            heapify(heap, heap_size, largest)

    n = len(nums_list)

    # создание max-кучи из списка
    for i in range(n, -1, -1):
        heapify(nums_list, n, i)

    # перемещение корня в конец списка
    for i in range(n - 1, 0, -1):
        nums_list[i], nums_list[0] = nums_list[0], nums_list[i]
        heapify(nums_list, i, 0)
