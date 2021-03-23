# алгоритм Евклида
def euclid_algorithm(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return euclid_algorithm(a % b, b)
    elif b >= a:
        return euclid_algorithm(a, b % a)
