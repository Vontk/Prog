def average_list(list):
    total = 0
    for num in list:
        total += num
    avg = (total / len(list))
    return avg


def count_first_characters(map):
    output_map = dict()
    first_characters = list()
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ' 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    for lists in map.values():
        for strings in lists:
            first_characters.append(strings[0])
    for character in abc:
        if character in first_characters:
            output_map[character] = 0
            for element in first_characters:
                if element.lower() == character:
                    output_map[character] += 1
    return output_map


def sum_expenses_by_category(tuplist):
    exp = dict()
    for tuple in tuplist:
        if tuple[0] not in exp.keys():
            exp[tuple[0]] = tuple[1]
        else:
            exp[tuple[0]] += tuple[1]
    return exp


def ex_sets(set1, set2):
    non_repeated = (set1 - set2).union(set2 - set1)  ##aca use + en vez de .union, lo cual no funciona
    value = 0
    for num in non_repeated:
        value += num
    return value


print(average_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(count_first_characters({"jorgito": ['alfredp', 'Ñaka', 'pedo', 'Pis', 'culo', 'teta'],
                              "lala": ['orto', 'ñaña', 'pedo', 'ladilla']}))
print(ex_sets({1, 2, 3, 4, 5, 6}, {5, 6, 7}))
print(sum_expenses_by_category([('Putas', 100), ('Casino', 10000), ('Droga', 500),
                                ('DildoExpress', 80), ('Droga', 800), ('Casino', 764)]))
