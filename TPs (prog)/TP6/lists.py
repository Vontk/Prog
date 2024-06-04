def remove_elements(list_to_remove_elements):
    return list_to_remove_elements[1:4] + list_to_remove_elements[6:]


def add_elements(list_to_add_elements):
    return ['Pink'] + list_to_add_elements + ['Yellow']


def is_empty(list_to_check):
    return list_to_check == []


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 3 and len(list_to_compare2) > 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    return [list_of_lists_to_modify[0][:2], list_of_lists_to_modify[1][1:4], list_of_lists_to_modify[2][-2:]]
