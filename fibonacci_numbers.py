# возвращает список с числами Фибоначчи
def fibonacci_list(limit):
    fib_nums = [0, 1]
    while len(fib_nums) <= limit:  # наполнение по условию
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)

    return fib_nums


# возвращает n-ое число Фибоначчи
def fibonacci_num(n):
    first_num = 0
    last_num = 1
    for _ in range(1, n):
        num = first_num + last_num
        first_num = last_num
        last_num = num

    return last_num
