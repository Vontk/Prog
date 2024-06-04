list_v1 = ["Red", "Green", "", "White", "Black", "Blue"]
list_v2 = list_v1


def enumerate_list(list):
    # para no modificar la lista, creamos una nueva
    enumerated_list = []
    for elemento in list:
        if elemento != "":
            enumerated_list.append(f'{len(enumerated_list)}. {elemento}')
    return enumerated_list


def enumerate_backwards(other_list):
    enumerated_list_backwards = []
    for index, color in enumerate(other_list):
        if other_list[index] != "":
            enumerated_list_backwards.append(f'{len(enumerated_list_backwards)}. {color[::-1]}')
    return enumerated_list_backwards


print(list_v2, list_v1)
print(enumerate_list(list_v1))
print(enumerate_backwards(list_v2))