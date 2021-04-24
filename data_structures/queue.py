def push(queue, elem):  # добавление элемента
    queue.append(elem)


def pop(queue):  # удаление элемента
    queue.pop(0)


def empty(queue):  # проверка на наличие элементов
    return not queue


def size(queue):  # получения количества элементов
    return len(queue)


def peek(queue):  # чтение головного элемента
    return queue[0]
