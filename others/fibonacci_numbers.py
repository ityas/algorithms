# возвращает n-ое число Фибоначчи
def fibonacci_num(n):
    first_num = 0
    last_num = 1
    for _ in range(1, n):
        first_num, last_num = last_num, first_num + last_num

    return last_num


# возвращает список с числами Фибоначчи до limit
def fibonacci_list(limit):
    fib_nums = [0, 1]
    while len(fib_nums) <= limit:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)

    return fib_nums
