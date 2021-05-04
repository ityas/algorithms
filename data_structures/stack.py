# stack = [...]

def push(stack, elem):  # добавление элемента
    stack.append(elem)


def pop(stack):  # удаление элемента
    stack.pop()


def empty(stack):  # проверка на наличие элементов
    return not stack


def size(stack):  # получения количества элементов
    return len(stack)


def peek(stack):  # чтение головного элемента
    return stack[-1]
