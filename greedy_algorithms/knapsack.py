# решение задачи о рюкзаке(c делением вещей на части)
def knapsack_with_proportion(things, knapsack_weight):
    # result_list = []
    things.sort(key=lambda l: l[0] / l[1], reverse=True)  # сортировка по c/w

    price = 0
    weight = 0
    for thing in things:
        if thing[0] == 0:  # для предметов с нулевой ценой
            continue

        future_weight = thing[1] + weight
        if future_weight <= knapsack_weight:
            # result_list.append([thing[0], thing[1]])

            price += thing[0]
            weight += thing[1]
        elif future_weight > knapsack_weight:
            proportion = (knapsack_weight - weight) / thing[1]
            proportion_price = thing[0] * proportion

            price += proportion_price
            weight += knapsack_weight - weight

            # result_list.append([proportion_price, thing[1]])
            break

    return price  # , result_list


# решение задачи о рюкзаке(c повторением вещей)
def knapsack_with_reps(things, knapsack_weight):
    n = len(things)
    d = [0] * (knapsack_weight + 1)

    weight = [i[1] for i in things[:n]]
    price = [i[0] for i in things[:n]]

    for w in range(0, knapsack_weight + 1):
        for i in range(0, n):
            if weight[i] <= w:
                d[w] = max(d[w], d[w - weight[i]] + price[i])

    return d[-1]


# решение задачи о рюкзаке(без повторений вещей)
def knapsack_without_reps(things, knapsack_weight):
    n = len(things)
    d = [0] * (knapsack_weight + 1)

    weight = [i[1] for i in things[:n]]
    price = [i[0] for i in things[:n]]


if __name__ == '__main__':
    knapsack_w = 10
    # things = [[60, 20], [100, 50], [120, 30]]  # and [20, 50, 30], [60, 100, 120], 50
    # things = [[20, 20], [25, 30], [10, 10]]
    things = [[30, 6], [14, 3], [16, 4], [9, 2]]

    print('knapsack_with_proportion() ==', knapsack_with_proportion(things, knapsack_w))
    print('knapsack_with_reps() ==', knapsack_with_reps(things, knapsack_w))
    print('knapsack_without_reps() ==', knapsack_without_reps(things, knapsack_w))
