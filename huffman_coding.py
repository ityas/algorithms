# функция, кодирующая строку
def huffman_encoding(string):
    symbols_dict = {}

    for s in string:
        if s in symbols_dict.keys():
            symbols_dict[s] = symbols_dict.get(s) + 1
        else:
            symbols_dict[s] = 1

    symbols_list = list(symbols_dict.items())
    tree = []

    while len(symbols_list) > 1:
        symbols_list.sort(key=lambda l: l[1])  # сортировка для новых значений

        # добавление детей в очередь с приоритетом
        tree.append([symbols_list[0][0], '0'])
        tree.append((symbols_list[1][0], '1'))

        # добавление родителей
        symbol = symbols_list[0][0] + symbols_list[1][0]
        priority = symbols_list[0][1] + symbols_list[1][1]
        symbols_list.append((symbol, priority))

        # удаление детей
        del symbols_list[0], symbols_list[0]

    codes = {}
    for symbol in symbols_dict.keys():
        if len(symbols_dict.keys()) == 1:
            codes[symbol] = '0'
            break

        symbol_code = ''
        for t in tree:
            if symbol in t[0]:
                symbol_code += t[1]
        codes[symbol] = symbol_code[::-1]

    coded_string = ''
    for symbol in string:
        coded_string += codes.get(symbol)

    return coded_string, codes


# функция, декодирующая строку
def huffman_decoding(coded_string, codes):
    string = ''
    num = ''
    for i in coded_string:
        num += i
        for symbol, code in codes.items():
            if num == code:
                string += symbol
                num = ''

    return string
