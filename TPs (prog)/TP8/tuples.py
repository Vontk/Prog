def get_coordinate(data):
    return str(data[1])


def convert_coordinate(coordinate):
    reformat = (str(coordinate[0]), str(coordinate[1]))
    return reformat


def create_record(azara_record, rui_record):
    if convert_coordinate(get_coordinate(azara_record)) == rui_record[1]:
        tuple_1 = (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
        return tuple_1
    return "not a match"