def get_coordinate(data):
    return str(data[1])


def convert_coordinate(coordinate):
    return tuple[coordinate[0], coordinate[1]]


def create_record(azara_list, rui_list):
    if convert_coordinate(get_coordinate(azara_list)) == rui_list[1]:
        tuple_1 = (azara_list[0], azara_list[1], rui_list[0], rui_list[1], rui_list[2])
        return tuple_1
    return "not a match"