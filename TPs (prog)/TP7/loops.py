list_v1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


def index_of_by_index(word, list, index):
    for i, element in enumerate(list):
        if element == word:
            if i >= index:
                return i
    return -1


def index_of_empty(list):
    for index, element in enumerate(list):
        if element == "":
            return index
    return -1


def index_of(word, list):
    for index, search_word in enumerate(list):
        if word in search_word:
            return index
    return -1


def put(word, list):
    for index, element in enumerate(list):
        if element == "":
            del list[index]
            list.insert(index, word)
            return index
    return -1


def remove(word, list):
    n_of_deleted_words = 0
    for i, e in enumerate(list):
        if word in e:
            del list[i]
            list.insert(i, "")
            n_of_deleted_words = n_of_deleted_words + 1
    return n_of_deleted_words

