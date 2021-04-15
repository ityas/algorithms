# things = [[price, weight], [price, weight]]

# решение задачи о рюкзаке(c делением вещей на части)
def knapsack_with_proportion(things, knapsack_weight):
    things.sort(key=lambda l: l[0] / l[1], reverse=True)  # сортировка по c/w

    price = 0
    weight = 0
    for thing in things:
        if thing[0] == 0:  # для предметов с нулевой ценой
            continue

        future_weight = thing[1] + weight
        if future_weight <= knapsack_weight:
            price += thing[0]
            weight += thing[1]
        elif future_weight > knapsack_weight:
            proportion = (knapsack_weight - weight) / thing[1]
            proportion_price = thing[0] * proportion

            price += proportion_price
            weight += knapsack_weight - weight
            break

    return price


# решение задачи о рюкзаке(c повторением вещей)
def knapsack_with_reps(things, knapsack_weight):
    things.sort(key=lambda l: l[0] / l[1], reverse=True)  # сортировка по c/w

    n = len(things)
    matrix = [0] * (knapsack_weight + 1)

    weight = [i[1] for i in things[:n]]
    price = [i[0] for i in things[:n]]

    for w in range(0, knapsack_weight + 1):
        for i in range(0, n):
            if weight[i] <= w:
                matrix[w] = max(matrix[w], matrix[w - weight[i]] + price[i])

    return matrix[-1]


# решение задачи о рюкзаке(без повторений вещей)
def knapsack_without_reps(things, knapsack_weight):
    things.sort(key=lambda l: l[0] / l[1], reverse=True)  # сортировка по c/w

    n = len(things)
    matrix = [[0] * (knapsack_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, knapsack_weight + 1):
            matrix[i][w] = matrix[i - 1][w]

            if w >= things[i - 1][1]:
                matrix[i][w] = max(matrix[i][w], matrix[i - 1][w - things[i - 1][1]] + things[i - 1][0])

    return matrix[-1][-1]
